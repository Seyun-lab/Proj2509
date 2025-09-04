# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import pickle
from django.conf import settings
from pathlib import Path
from django.templatetags.static import static

def result(request):
    # static_app_dir = Path(settings.BASE_DIR) / 'static'
    # img_path1 = static_app_dir/'averagepurchase_heatmap.png'
    # img_path2 = static_app_dir/'kidhomepurchase_boxplot.png'
    # img_path3 = static_app_dir/'importance.png'
    # img_path4 = static_app_dir/'confusionmatrix.png'
    return render(request, 'result.html', {
        'img_heatmap': static('averagepurchase_heatmap.png'),
        'img_kidhome_box': static('kidhomepurchase_boxplot.png'),
        'img_importance': static('importance.png'),
        'img_confusion': static('confusionmatrix.png'),
    })

def predictModel(request):
    result = None
    if request.method == 'POST':
        try:
            # Get input values from the form
            features = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
            
            input_data = []
            for feature in features:
                input_data.append(float(request.POST.get(feature.lower(), 0)))

            # Prepare the data for the model
            data = pd.DataFrame([input_data], columns=features)
            
            # Load the model and make a prediction
            candidate_paths = [
            Path(__file__).resolve().parent / 'model.pkl',       # myapp/model.pkl
            Path(settings.BASE_DIR) / 'myapp' / 'model.pkl',     # lm13_Quiz/myapp/model.pkl
            ]
            model_path = None
            for p in candidate_paths:
                if p.exists():
                    model_path = p
                    break
            if model_path is None:
                raise FileNotFoundError(f"model.pkl not found. Checked: {candidate_paths}")
            
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
            
            prediction = model.predict(data)
            result = prediction[0]

        except FileNotFoundError:
            result = "Error: Model file not found."
        except Exception as e:
            result = f"An error occurred: {e}"
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # numpy.float 같은 타입은 Python 기본 타입으로 변환 필요
            if hasattr(result, "item"):
                result = result.item()
            return JsonResponse({'result': f"예상 유아 수 {result}명 입니다."})
            
    
    context = {
        'result': result
    }
    return render(request, 'customers.html', context)