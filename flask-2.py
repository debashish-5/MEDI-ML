from flask import Flask, request, render_template_string
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained pipeline and feature list
model_pipeline = joblib.load("model.pkl")
pipeline = joblib.load("pipeline.pkl")

# HTML Template (1 page, inline CSS)
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>MEDI STORE</title>
    <style>
      body { font-family: Arial, sans-serif; background:#1b7a1b; margin:0; padding:20px; }
      .container { background: #a3fba3; border-radius: 10px; padding: 30px; max-width:600px; margin:auto; box-shadow: 0 3px 8px rgba(0,0,0,0.2); }
      h1 { text-align:center;font-family: emoji;font-style: revert; }
      input[type=text], input[type=file] { width:100%; padding:10px; margin-top:8px; border:1px solid #ccc; border-radius:5px; }
      button { background:#1e90ff; color:white; padding:10px; border:none; width:100%; margin-top:10px; border-radius:5px; cursor:pointer; }
      button:hover { opacity:0.9; }
      .result { margin-top:20px; padding:10px; background:#e1ffe1; border:1px solid #3bb13b; border-radius:5px; }
    </style>
</head>
<body>
<div class="container">
    <h1>MEDI STORE</h1>

    <form method="POST" enctype="multipart/form-data">

      <h3>Enter the Product Name:</h3>
      <input type="text" placeholder="Product Name" name="a"><br>
      
      <button type="submit">Predict</button>
    </form>

    {% if result %}
       <div class="result">{{ result }}</div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":

        # If one-by-one values are given
        request.form.get("a")
        a = request.form['a']


        input_features = [a]
        input_features = pipeline.transform(input_features)
        pred_class = model_pipeline.predict(input_features)[0]
       # pred_proba = model_pipeline.predict_proba(input_features)[0][1]
                
        result = f"Prediction:--> <b>Discount Price: {pred_class[0]} || Actual Price: {pred_class[1]} || Discount Percentage: {pred_class[2]} || Rating: {pred_class[3]} || Users: {pred_class[4]}</b>"   

    return render_template_string(html_page, result=result)


if __name__ == "__main__":
    app.run(debug=True)
