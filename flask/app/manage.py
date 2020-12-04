from app import app



@app.route("/predict")
def predict():
    return "this method will you the prediction model"
