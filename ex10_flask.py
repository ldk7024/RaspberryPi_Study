from flask import Flask
import led18

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/led/on')
def led_on():
    led18.led18on()
    return 'LED ON'

@ app.route('/led/off')
def led_off():
    led18.led18off()
    return 'LED OFF'

if __name__ == '__main__':
    app.run(host='59.0.129.182', port = 8888)     # app.run은 맨 하단에 있어야한다.