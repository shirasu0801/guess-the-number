from flask import Flask, render_template, request, jsonify, session
import random
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # セッション管理用
CORS(app)

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(0, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    user_guess = int(data['guess'])
    number = session.get('number', random.randint(0, 100))
    
    if user_guess < number:
        return jsonify(result="Too low!")
    elif user_guess > number:
        return jsonify(result="Too high!")
    else:
        session.pop('number', None)  # 正解時はセッションリセット
        return jsonify(result="Correct!")

if __name__ == '__main__':
    app.run(debug=True)