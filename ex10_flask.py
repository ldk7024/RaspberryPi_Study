from flask import Flask, render_template
import led18
import ex09_select as slt

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/led/on')
def led_on():
    led18.led18on()
    return 'LED ON'

@ app.route('/led/off')
def led_off():
    led18.led18off()
    return 'LED OFF'

@app.route('/select')
def select():
    r= slt.sel()
    return r

if __name__ == '__main__':
    app.run(host='59.0.129.182', port = 8888)     # app.run은 맨 하단에 있어야한다.