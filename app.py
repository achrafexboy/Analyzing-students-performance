import pickle
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

filename = "Models/modelSVM-StdPerformance.sav" # Model Random Forest regressor
model = pickle.load(open(filename,'rb'))

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict",methods=['GET','POST'])
def predict():
    features = [float(x) for x in request.form.values()]

    lis_state=[]
    lis_parent=[]
    if(features[-2]==0):
        lis_state=[1,0,0,0,0]
    elif(features[-2]==1):
        lis_state=[0,1,0,0,0]
    elif(features[-2]==2):
        lis_state=[0,0,1,0,0]
    elif(features[-2]==3):
        lis_state=[0,0,0,1,0]
    elif(features[-2]==4):
        lis_state=[0,0,0,0,1]

    if(features[-1]==0):
        lis_parent=[1,0,0,0,0,0]
    elif(features[-2]==1):
        lis_parent=[0,1,0,0,0,0]
    elif(features[-2]==2):
        lis_parent=[0,0,1,0,0,0]
    elif(features[-2]==3):
        lis_parent=[0,0,0,1,0,0]
    elif(features[-2]==4):
        lis_parent=[0,0,0,0,1,0]
    elif(features[-2]==5):
        lis_parent=[0,0,0,0,0,1]

    features = features[:3] + lis_parent + lis_state

    f_features = [np.array(features)]
    prediction = model.predict(f_features)

    if prediction == 1 : prediction = 'Succeed'
    else : prediction = 'Not Succeed'

    print(prediction)
    
    return render_template('index.html', prediction_text= "The Student will " + prediction)

#"Student's overall score out of 100 will be : "

if __name__ == "__main__":
    app.run(debug=True)



