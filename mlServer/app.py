from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from flask_cors import CORS
from functions import process_tld, abnormal_url, digit_count, httpSecure, letter_count, Shortining_Service, having_ip_address  # noqa

app = Flask(__name__)
model1 = load('model1.joblib')
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/analyze', methods=['POST'])  # noqa
def predict():
    data = request.get_json()
    url = data['url']
    ip = url.replace('www.', '')
    iplen = len(ip)
    process_tld(ip)
    a_url = abnormal_url(ip)  # noqa
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    a11 = 0
    a12 = 0
    a13 = 0
    for a in ip:
        if a == '@':
            a1 += 1
        if a == '?':
            a2 += 1
        if a == '-':
            a3 += 1
        if a == '=':
            a4 += 1
        if a == '.':
            a5 += 1
        if a == '#':
            a6 += 1
        if a == '%':
            a7 += 1
        if a == '+':
            a8 += 1
        if a == '$':
            a9 += 1
        if a == '!':
            a10 += 1
        if a == '*':
            a11 += 1
        if a == ',':
            a12 += 1
        if a == '//':
            a13 += 1
    http_s = httpSecure(ip)
    dc = digit_count(ip)
    lc = letter_count(ip)
    ss = Shortining_Service(ip)
    is_ip = having_ip_address(ip)
    input = np.array([[iplen, a1, a2, a3, a4, a5, a6, a7, a8,
                     a9, a10, a11, a12, a13, http_s, dc, lc, ss, is_ip]])
    prediction = model1.predict(input)
    output = int(prediction[0])
    print(prediction)
    return jsonify({'result': 'Success', 'output': output})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
