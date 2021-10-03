import pickle
from flask import Flask , request, render_template
app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/input')
def indput():
	return render_template('input-pagec.html')
@app.route('/predict',methods = ['GET','POST'])
def admin():
    dist=eval(request.form["district"])
    season=eval(request.form["season"])
    crop=eval(request.form["crop"])
    rain=eval(request.form["rainfall"])
    preds=[[dist,season,crop,rain]]
    xx=model.predict(preds)
    return render_template("input-pagec.html",p="yield is {} metric tonnes per hectare".format(xx[0]))
if __name__ == '__main__':
    app.run(debug = False, port=4000)
