# Car Price Prediction

A machine learning web application that predicts used car prices based on car details such as name, company, year, kilometers driven, and fuel type.

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* HTML
* CSS
* JavaScript

## How It Works

The trained machine learning model is served through a FastAPI backend. The frontend collects user inputs and sends them to the API to receive the predicted car price.

The target variable is log-transformed during training and converted back using `np.exp()` during prediction.

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Author

Rida Sohail
