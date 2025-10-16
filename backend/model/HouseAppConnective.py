from flask import Flask,render_template,url_for,redirect,request
import joblib as jb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


app=Flask(__name__)
app.secret_key="supersecret"


@app.route("/")
def predict():
    return render_template('Predict.html')
@app.route("/submit",methods=["POST"])
def submit():
 if request.method=="POST": 
    status=request.form.get("Status")
    area=request.form.get("tarea")
    btroom=request.form.get("nbathe")
    floor=request.form.get("nfloor")
    x=[[area,4,btroom,1,floor,1,status]]
    model=jb.load("house.pkl")
    y=model.predict(x)
    return f''' <h1>prediction is {y}</h1> '''
 return "hei"
