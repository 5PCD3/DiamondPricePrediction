from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'POST':
            data = CustomData(
                carat=float(request.form.get("carat")),
                depth=float(request.form.get("depth")),
                table=float(request.form.get("table")),
                x=float(request.form.get("x")),
                y=float(request.form.get("y")),
                z=float(request.form.get("z")),
                cut=float(request.form.get("cut")),
                colour=float(request.form.get("colour")),
                clarity=float(request.form.get("clarity")),
                # price=float(request.form.get("price"))
            )
            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)

            # Calculate the predicted price
            results = round(pred[0], 2)

            # Pass the predicted price to the template
            return render_template('index.html', result=results)
        else:
            return render_template('index.html')
    except Exception as e:
        print("Error:", e)
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
