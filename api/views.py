from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import joblib
import os

# Loads the trained pipeline
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ml_models', 'fertilizer_pipeline.pkl')
pipeline = joblib.load(model_path)


class PredictFertilizer(APIView):
    def post(self, request):
        try:
            # Convert JSON input to DataFrame
            df = pd.DataFrame([request.data])
            # Predicts the fertilizer code
            pred = pipeline.predict(df)[0]
            # Mapping fertilizer codes to names
            fertilizer_map = {
                0: "Balanced NPK Fertilizer",
                1: "Compost",
                2: "DAP",
                3: "General Purpose Fertilizer",
                4: "Gypsum",
                5: "Lime",
                6: "Muriate of Potash",
                7: "Organic Fertilizer",
                8: "Urea",
                9: "Water Retaining Fertilizer"
            }
            return Response({
                "fertilizer_code": int(pred),
                "fertilizer_name": fertilizer_map[pred]
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render

# Voew for rendering the HTML form
def home(request):
    return render(request, 'predict_form.html')

