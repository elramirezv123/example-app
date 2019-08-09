from flask import Flask
app = Flask(__name__)
deploy = False

@app.route('/')
def hello_world():
    return 'Hola mundito, estoy arriba!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    if not deploy:
        app.run(debug=True)