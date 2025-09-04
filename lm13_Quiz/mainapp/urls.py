# config/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 페이지
    path('2/', views.predictModel, name='model_page'), # 예측 모델 페이지
    path('', views.result, name='result'), # 시각화 이미지 출력 페이지

]
