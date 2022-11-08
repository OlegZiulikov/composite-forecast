import flask
from flask import render_template
import tensorflow as tf
from tensorflow import keras
import sklearn

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def main():
    temp = 1
    param_lst = []

    if flask.request.method == 'GET':
        return render_template('site.html')
        
    if flask.request.method == 'POST':
        loaded_model = keras.models.load_model("itog_model")
        for i in range(1,13,1):
            experience = float(flask.request.form.get(f'experience{i}'))
            param_lst.append(experience)
        
        temp = loaded_model.predict([param_lst])
        return render_template('site.html', result = temp)

if __name__ == '__main__':
    app.run()