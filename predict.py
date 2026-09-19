import joblib

model = joblib.load("model.pkl")

print("Model loaded successfully!")
import pandas as pd

study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous score: "))

new_student = pd.DataFrame(
    [[study_hours, attendance, previous_score]],
    columns=["study_hours", "attendance", "previous_score"]
)

prediction = model.predict(new_student)

print("Prediction:", prediction[0])


probability = model.predict_proba(new_student)

print("Fail probability:", probability[0][0])
print("Pass probability:", probability[0][1])