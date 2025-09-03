# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.utils import timezone
import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso, Ridge

from .models import Jikwon


def predict_page(request):
    """predict.html 렌더 (폼 + 결과영역)"""
    return render(request, "predict.html")


def _years_of_service(ibsail):
    """입사일 -> 근무년수(년)"""
    if ibsail is None or pd.isna(ibsail):
        return np.nan
    if not hasattr(ibsail, "year"):
        ibsail = pd.to_datetime(ibsail, errors="coerce")
    if pd.isna(ibsail):
        return np.nan
    today = timezone.now().date()
    return max(0.0, (today - ibsail.date()).days / 365.25)

# 여기서 증명
from sklearn.linear_model import LinearRegression, Ridge, Lasso

def _fit_model_and_summary(use_model="linear"):
    """
    DB → DataFrame → 전처리 → 선택한 모델 학습
    use_model: "linear", "ridge", "lasso"
    """
    qs = Jikwon.objects.values("jikwonibsail", "jikwonpay", "jikwonjik")
    df = pd.DataFrame(qs)
    if df.empty:
        print("⚠️ DB에서 불러온 데이터가 없습니다.")
        return None, None, []

    df["jikwonibsail"] = pd.to_datetime(df["jikwonibsail"], errors="coerce")
    df["years"] = df["jikwonibsail"].apply(_years_of_service)
    df["jikwonpay"] = pd.to_numeric(df["jikwonpay"], errors="coerce")

    df = df.dropna(subset=["years", "jikwonpay"])
    df = df[df["jikwonpay"] > 0]

    if len(df) < 2:
        print("⚠️ 유효한 데이터가 부족합니다.")
        return None, None, []

    X = df[["years"]].to_numpy()
    y = df["jikwonpay"].to_numpy()

    # --- 모델 선택 ---
    if use_model == "ridge":
        model = Ridge(alpha=1.0).fit(X, y)
        print("\n>>> Ridge 모델 학습 완료")
    elif use_model == "lasso":
        model = Lasso(alpha=0.1).fit(X, y)
        print("\n>>> Lasso 모델 학습 완료")
    else:
        model = LinearRegression().fit(X, y)
        print("\n>>> LinearRegression 모델 학습 완료")

    # 설명력
    r2 = float(model.score(X, y))

    # 🔎 확인용 출력
    print(f"계수(coef_): {model.coef_}")
    print(f"절편(intercept_): {model.intercept_}")
    print(f"설명력(R²): {r2:.4f}")

    # 직급별 평균
    by_rank = (
        df.groupby("jikwonjik", dropna=False)["jikwonpay"]
          .mean()
          .reset_index()
          .rename(columns={"jikwonjik": "rank", "jikwonpay": "avg_pay"})
          .sort_values("avg_pay", ascending=False)
    )
    by_rank["rank"] = by_rank["rank"].fillna("미정")
    by_rank["avg_pay"] = by_rank["avg_pay"].round(0).astype(int)
    by_rank_list = by_rank.to_dict(orient="records")

    return model, r2, by_rank_list


@require_http_methods(["GET"])
def api_summary(request):
    """설명력(R²) + 직급별 연봉평균 → JSON"""
    model, r2, by_rank = _fit_model_and_summary()
    if model is None:
        return JsonResponse({"error": "데이터가 부족합니다."}, status=500)
    return JsonResponse({"r2": r2, "by_rank": by_rank})


@require_http_methods(["GET", "POST"])
def api_predict(request):
    """
    근무년수 → 예상 연봉 예측 → JSON

    - GET:  /api/predict/?years=3.5
    - POST: {"years": 3.5}
    """
    years = None
    if request.method == "GET":
        years = request.GET.get("years")
    else:
        try:
            payload = json.loads(request.body.decode("utf-8") or "{}")
            years = payload.get("years")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("잘못된 JSON")

    try:
        years = float(years)
        if years < 0:
            return HttpResponseBadRequest("근무년수는 0 이상이어야 합니다.")
    except (TypeError, ValueError):
        return HttpResponseBadRequest("근무년수를 숫자로 입력하세요.")

    model, r2, _ = _fit_model_and_summary()
    if model is None:
        return JsonResponse({"error": "모델 학습 데이터가 부족합니다."}, status=500)

    pred = float(model.predict(np.array([[years]]))[0])
    pred = max(0.0, pred)   # 음수면 0으로 고정 
    
    # ✅ json으로 전송하기 (두 방식 중 하나 사용)
    return JsonResponse({"years": years, "predicted_pay": round(pred, 0), "r2": r2})
    # 또는
    # return HttpResponse(
    #     json.dumps({"years": years, "predicted_pay": round(pred, 0), "r2": r2}, ensure_ascii=False),
    #     content_type="application/json",
    # )
