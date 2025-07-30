import pickle
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.sql import func
app = Flask(__name__, template_folder='templates', static_folder='static')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class student(db.Model):
    id = db.Column(db.Integer, db.Sequence('seq_reg_id', start=1, increment=1),
               primary_key=True)
    q1=db.Column(db.Integer)
    q2=db.Column(db.Integer)
    q3=db.Column(db.Integer)
    q4=db.Column(db.Integer)
    q5=db.Column(db.Integer)
    q6=db.Column(db.Integer)
    q7=db.Column(db.Integer)
    q8=db.Column(db.Integer)
    q9=db.Column(db.Integer)
    q10=db.Column(db.Integer)
    q11=db.Column(db.Integer)
    q12=db.Column(db.Integer)
    q13=db.Column(db.Integer)
    q14=db.Column(db.Integer)
    q15=db.Column(db.Integer)
    q16=db.Column(db.Integer)
    q17=db.Column(db.Integer)
    q18=db.Column(db.Integer)
    q19=db.Column(db.Integer)
    q20=db.Column(db.Integer)
    q21=db.Column(db.Integer)
    q22=db.Column(db.Integer)
    q23=db.Column(db.Integer)
    q24=db.Column(db.Integer)
    q25=db.Column(db.Integer)
    q26=db.Column(db.Integer)
    q27=db.Column(db.Integer)
    prediction=db.Column(db.Integer)

#col_list=student.__table__.columns.keys()


@app.route('/')

def home():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')
@app.route('/about')
def about():
    return render_template('about.html')   
@app.route('/service')
def service():
    context=['I am currently employed at least part-time', 'Education',
       'I have my own computer separate from a smart phone',
       'I have been hospitalized before for my mental illness',
       'How many days were you hospitalized for your mental illness',
       'I am legally disabled', 'I have my regular access to the internet',
       'I live with my parents', 'I have a gap in my resume',
       'Total length of any gaps in my resume in months.', 'Income',
       'Unemployed', 'I read outside of work and school',
       'Annual income from social welfare programs', 'I receive food stamps',
       'I am on section 8 housing',
       'How many times were you hospitalized for your mental illness',
       'Lack of concentration', 'Anxiety', 'Depression', 'Obsessive thinking',
       'Mood swings', 'Panic attacks', 'Compulsive behavior', 'Tiredness',
       'Age', 'Gender']
    return render_template('home.html',context=context)
    
@app.route('/team')
def team():
    return render_template('team.html')
    
def ValuePredictor(to_predict_list):
    # Extract related symptom scores
    lack_of_concentration = to_predict_list[17]
    anxiety = to_predict_list[18]
    depression = to_predict_list[19]
    obsessive_thinking = to_predict_list[20]
    mood_swings = to_predict_list[21]
    panic_attacks = to_predict_list[22]
    compulsive_behavior = to_predict_list[23]

    # Calculate scores properly
    depression_score = lack_of_concentration + depression
    anxiety_score = anxiety + depression + obsessive_thinking + mood_swings
    ocd_score = panic_attacks + compulsive_behavior

    # Check minimum threshold
    if depression_score >= 2 and depression_score >= anxiety_score and depression_score >= ocd_score:
        return "Depression"
    elif anxiety_score >= 2 and anxiety_score >= depression_score and anxiety_score >= ocd_score:
        return "Anxiety"
    elif ocd_score >= 2 and ocd_score >= depression_score and ocd_score >= anxiety_score:
        return "Obsessive-Compulsive Disorder (OCD)"
    else:
        return "You seem mentally healthy"



@app.route('/result1', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))

        result = ValuePredictor(to_predict_list)  # Get illness type

        if result == "You seem mentally healthy":
            tips = "Tips: Go to the gym, dance, listen to music, wake up early, eat healthy, and stay social! 😊"
            message = f"Congratulations! You don't show significant signs of mental illness. {tips}"
        else:
            tips = "Suggestion: Please consult a mental health professional. Meanwhile, practice mindfulness, maintain a daily routine, stay connected with loved ones, and avoid self-isolation."
            message = f'You may have {result}. {tips}'

        return render_template("result1.html", prediction=message)

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/Read_more')
def Read_more():
    return render_template('Read_more.html')

        
if __name__ == '__main__':
    app.run(debug=True)
