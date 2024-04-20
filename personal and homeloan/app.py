import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import yagmail

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
modelloan = pickle.load(open('model_rf.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/homeloan')
def homeloan():
    return render_template('index.html')
@app.route('/personalloan')
def personalloan():
    return render_template('indexloan.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output==1:
        try:
            user = 'loanprediction9@gmail.com'
            app_password = 'tlkivhrkmqpdgntj' # a token for gmail
            # to = 'akbarpasha0696@gmail.com'
            to = "anshukondawar04@gmail.com"
            subject = 'Loan Prediction using Machine Learning'
            content = '''
            <p>Dear User,</p>
            <p>Congratuations, we are thrilled to share the fantastic news with you. Your home loan application has been officially accepted!
            </p>
            <p> Thank you for using our service </p>
            <p>Regards,</p>
            <p>Team Loan Prediction</p>
            </table>
                '''
            with yagmail.SMTP(user, app_password) as yag:
                yag.send(to, subject, content)
                print('Sent email successfully')
                messages.success(request, 'You are at mid risk')
                return render(request, 'users/predict1.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
        except:
            pass

    #return render_template('index.html', prediction_text='PROBABILITY THAT YOUR LOAN WILL GET APPROVED IS ; {}'.format(output))

    else:
        try:
            user = 'loanprediction9@gmail.com'
            app_password = 'tlkivhrkmqpdgntj' # a token for gmail
            # to = 'akbarpasha0696@gmail.com'
            to = "anshukondawar04@gmail.com"
            subject = 'Loan Prediction using Machine Learning'
            content = '''
            <p>Dear User,</p>
            
            <p>We regret to inform you that after a thorough review of your home loan application, we are unable to proceed with the approval of your loan at this time.
            </p>
            <p> Thank you for using our service </p>
            <p>Regards,</p>
            <p>Team Loan Prediction</p>
            </table>
                '''
            with yagmail.SMTP(user, app_password) as yag:
                yag.send(to, subject, content)
                print('Sent email successfully')
                messages.success(request, 'You are at mid risk')
                return render(request, 'users/predict1.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
        except:
            pass

    return render_template('index.html', prediction_text='PROBABILITY THAT YOUR LOAN WILL GET APPROVED IS ; {}'.format(output))



@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

@app.route('/predictloan',methods=['POST'])
def predictloan():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = modelloan.predict(final_features)

    output = round(prediction[0], 2)
    if output==1:
        try:
            user = 'loanprediction9@gmail.com'
            app_password = 'tlkivhrkmqpdgntj' # a token for gmail
            # to = 'akbarpasha0696@gmail.com'
            to = "anshukondawar04@gmail.com"
            subject = 'Loan Prediction using Machine Learning'
            content = '''
            <p>Dear User,</p>
            
            <p>Congratuations, we are thrilled to share the fantastic news with you. Your personal loan application has been officially accepted!
            </p>
            <p> Thank you for using our service </p>
            <p>Regards,</p>
            <p>Team Loan Prediction</p>
            </table>
                '''
            with yagmail.SMTP(user, app_password) as yag:
                yag.send(to, subject, content)
                print('Sent email successfully')
                messages.success(request, 'You are at mid risk')
                return render(request, 'users/predict1.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
        except:
            pass
    
    else:
        try:
            user = 'loanprediction9@gmail.com'
            app_password = 'tlkivhrkmqpdgntj' # a token for gmail
            # to = 'akbarpasha0696@gmail.com'
            to = "anshukondawar04@gmail.com"
            subject = 'Loan Prediction using Machine Learning'
            content = '''
            <p>Dear User,</p>
            <p>We regret to inform you that after a thorough review of your personal loan application, we are unable to proceed with the approval of your loan at this time.
            </p>
            <p> Thank you for using our service </p>
            <p>Regards,</p>
            <p>Team Loan Prediction</p>
            </table>
                '''
            with yagmail.SMTP(user, app_password) as yag:
                yag.send(to, subject, content)
                print('Sent email successfully')
                messages.success(request, 'You are at mid risk')
                return render(request, 'users/predict1.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
        except:
            pass

    return render_template('index.html', prediction_text='PROBABILITY THAT YOUR LOAN WILL GET APPROVED IS ; {}'.format(output))

@app.route('/resultsloan',methods=['POST'])
def resultsloan():

    data = request.get_json(force=True)
    prediction = modelloan.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)