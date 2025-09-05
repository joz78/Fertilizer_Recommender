##  Prediction Routes

Users can make predictions through either of the following interfaces:

### 1. Django REST Framework Route  
**URL:** `http://127.0.0.1:8000/api/predict/`  
This endpoint accepts JSON input via POST requests and returns fertilizer recommendations in JSON format. It’s ideal for integration with other systems or testing via tools like Postman or curl.
example:
{
  "Temperature": 30,
  "Moisture": 45,
  "Rainfall": 80,
  "PH": 5.8,
  "Nitrogen": 40,
  "Phosphorous": 20,
  "Potassium": 25,
  "Carbon": 0.9,
  "Soil": "Acidic_Soil",
  "Crop": "Rice"
}


### 2. Frontend Template Route  
**URL:** `http://127.0.0.1:8000/api/`  
This route renders a user-friendly HTML form where users can manually enter input values and view the predicted fertilizer directly on the page.

Both routes are powered by the same machine learning model and offer flexible access depending on the user’s preference or technical setup.

Thank you for using the Fertilizer Recommendation API!
