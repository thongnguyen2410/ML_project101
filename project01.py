# Dependencies
import sys
import traceback

import pandas as pd
from flask import Flask, request, jsonify
import joblib

from SVM import create_dummies

# Your API definition
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'SVM model!'


@app.route('/predict', methods=['POST'])
def predict():
    if svm_model:
        try:
            json_ = request.json
            print(json_)
            # query = pd.get_dummies(pd.DataFrame(json_))
            # query = query.reindex(columns=model_columns, fill_value=0)
            df = pd.DataFrame(json_)
            columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
            df = create_dummies(df, columns)
            df = df.reindex(columns=model_columns, fill_value=0)

            prediction = list(svm_model.predict(df))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return 'No model here to use'


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # This is for a command-line input
    except:
        port = 12345  # If you don't provide any port the port will be set to 12345

    svm_model = joblib.load("SVM.pkl")  # Load "model.pkl"
    print('Model loaded')
    model_columns = joblib.load("SVM_columns.pkl")  # Load "model_columns.pkl"
    print('Model columns loaded')

    app.run(port=port, debug=True)

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
#
