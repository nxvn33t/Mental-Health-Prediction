# Mental Illness Prediction

This project predicts the likelihood of mental illness based on user input using a machine learning model. It includes a Flask-based web app, trained model, and a Jupyter notebook for data exploration and model training.

## 🧠 Features

- Predict mental health risk using machine learning
- Cleaned dataset used for training
- Web-based interface built with Flask
- Trained model saved as `.pkl`
- SQLite database integration

## 📁 Project Structure

Mentalillness_prediction/
├── app.py # Flask app entry point
├── flask_template.py # Additional Flask templates
├── mental-health-prediction.ipynb # Jupyter notebook for EDA + modeling
├── model.py # Model training script
├── model.pkl # Saved ML model
├── Cleaned Data.xlsx # Dataset
├── database.db # SQLite database
├── requirements.txt # Python dependencies

bash
Copy
Edit

## 🚀 How to Run

1.  Clone the repository: 
   ```bash
   git clone https://github.com/nxvn33t/Mental-Health-Prediction.git
   cd Mental-Health-Prediction
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to http://localhost:5000

📊 Dataset
The dataset is included in Cleaned Data.xlsx and contains features related to mental health indicators.

Preprocessed and used to train the model in the Jupyter notebook.

🛠 Tech Stack
Python

Flask

Pandas, NumPy, Scikit-learn

Jupyter Notebook

SQLite

🧪 Model
Trained using supervised ML algorithm (check mental-health-prediction.ipynb)

Final model is saved as model.pkl and used by the Flask app
