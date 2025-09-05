from django.urls import path
#from .views import PredictAPIView

"""
urlpatterns = [
    path('predict/', PredictAPIView.as_view(), name='predict_api'),
]
"""
from django.urls import path
from .views import PredictFertilizer , home

urlpatterns = [
   path('', home, name='home'),# route to a web form
    path('predict/', PredictFertilizer.as_view(), name='predict_fertilizer'), # route to Django Rest Framework Browsable API
     
]

