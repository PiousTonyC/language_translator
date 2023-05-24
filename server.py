from flask import Flask, request, render_template
from translate import english_to_french,french_to_english
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/english-french', methods=['POST'])
def e2f():
    data = request.get_json()
    txt = data.get('txt')
    translated_txt = english_to_french(txt)
    return translated_txt

@app.route('/french-english', methods=['POST'])
def f2e():
    data = request.get_json()
    txt = data.get('txt')
    translated_txt = french_to_english(txt)
    return translated_txt
    
if __name__ == '__main__':
    app.run(debug = True)