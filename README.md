# Student Performance Predictor

A simple machine learning web application that predicts whether a student is likely to Pass or Fail based on study hours, attendance, and previous score.

## Features

- Student performance prediction
- Logistic Regression machine learning model
- Pass/Fail probability
- Input validation
- Probability visualization
- Flask backend
- HTML, CSS and JavaScript frontend

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS
- JavaScript

## How It Works

1. Student enters study hours, attendance and previous score.
2. Flask receives the input.
3. The trained Logistic Regression model processes the data.
4. The application predicts Pass or Fail.
5. The model's probabilities are displayed on the webpage.

## Project Structure

student-performance-predictor/
├── app.py
├── train_model.py
├── predict.py
├── students.csv
├── model.pkl
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css

## How to Run

Create and activate a virtual environment:

```bash
python -m venv venv