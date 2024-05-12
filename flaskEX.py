from flask import Flask
app = Flask(__name__)

import random

@app.route('/')

def rand_num():
    return str(random.randint(0,100))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
