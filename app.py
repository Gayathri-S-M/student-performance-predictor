from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_score = float(request.form["previous_score"])

    if study_hours < 0:
        return render_template(
            "index.html",
            error="Study hours cannot be negative."
        )

    if attendance < 0 or attendance > 100:
        return render_template(
            "index.html",
            error="Attendance must be between 0 and 100."
        )

    if previous_score < 0 or previous_score > 100:
        return render_template(
            "index.html",
            error="Previous score must be between 0 and 100."
        )

    new_student = pd.DataFrame(
        [[study_hours, attendance, previous_score]],
        columns=["study_hours", "attendance", "previous_score"]
    )

    prediction = model.predict(new_student)[0]

    probability = model.predict_proba(new_student)

    fail_probability = probability[0][0]
    pass_probability = probability[0][1]

    return render_template(
        "index.html",
        prediction=prediction,
        fail_probability=fail_probability,
        pass_probability=pass_probability
    )


if __name__ == "__main__":
    app.run(debug=True)