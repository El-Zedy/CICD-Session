from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome To CICD World'

if __name__ == '__main__':
    # Change the host and port to 0.0.0.0:5001
    app.run(debug=True, host='0.0.0.0', port=5001)
