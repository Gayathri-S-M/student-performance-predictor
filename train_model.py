import joblib
import pandas as pd

data = pd.read_csv("students.csv")

X = data[["study_hours", "attendance", "previous_score"]]
y = data["result"]

print("Features:")
print(X)

print("\nTarget:")
print(y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)
joblib.dump(model, "model.pkl")
print("Model saved successfully!")

print("Model training completed!")
from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Predictions:", predictions)
print("Actual:", y_test.values)
print("Accuracy:", accuracy)
new_student = pd.DataFrame(
    [[1, 50, 30]],
    columns=["study_hours", "attendance", "previous_score"]
)
prediction = model.predict(new_student)

print("New student prediction:", prediction[0])
print("\nTest Results:")

for actual, predicted in zip(y_test, predictions):
    print("Actual:", actual, "| Predicted:", predicted)

probability = model.predict_proba(new_student)


print("\nPrediction probabilities:")
print("Fail:", probability[0][0])
print("Pass:", probability[0][1])
import matplotlib.pyplot as plt

for result in ["Pass", "Fail"]:
    subset = data[data["result"] == result]
    plt.scatter(
        subset["study_hours"],
        subset["previous_score"],
        label=result
    )

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")
plt.legend()
plt.show()

study_hours = 5
attendance = 82
previous_score = 68

