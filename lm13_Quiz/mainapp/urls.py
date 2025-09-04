# config/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 페이지
    path('', views.predict_page, name='predict_page'),  # / → predict.html

    # API(JSON)
    path('api/predict/', views.api_predict, name='api_predict'),
    path('api/summary/', views.api_summary, name='api_summary'),
]
