from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time
webpage = "living.html"
app= Flask(__name__,template_folder='Templates', static_folder='Templates/Static')

led1,led2,led3,led4,led5= 3,5,7,11,13

rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(led1, rpi.OUT)
rpi.setup(led2, rpi.OUT)
rpi.setup(led3, rpi.OUT)
rpi.setup(led4, rpi.OUT)
rpi.setup(led5, rpi.OUT)
rpi.output(led1, 0)
rpi.output(led2, 0)
rpi.output(led3, 0)
rpi.output(led4, 0)
rpi.output(led5, 0)
print("Done")

@app.route('/')
def index():
    return render_template(webpage)



@app.route('/P')
def led1on():
    rpi.output(led1,1)
    return render_template(webpage)

@app.route('/p')
def led1off():
    rpi.output(led1,0)
    return render_template(webpage)

@app.route('/E1L')
def e1l():

    return render_template("livingap1.html")
@app.route('/E1K')
def e1k():

    return render_template("kitchen.html")

@app.route('/E1G')
def led2on():
    rpi.output(led2,1)
    return render_template("livingap1.html")

@app.route('/e1g')
def led2off():
    rpi.output(led2,0)
    return render_template("livingap1.html")


@app.route('/E1A')
def led3on():
    rpi.output(led3,1)
    return render_template('kitchen.html')

@app.route('/e1a')
def led3off():
    rpi.output(led3,0)
    return render_template('kitchen.html')
@app.route('/E2L')
def e2l():

    return render_template("livingap2.html")
@app.route('/E2B')
def e2b():

    return render_template("bedroom.html")


@app.route('/E2G')
def led4on():
    rpi.output(led4,1)
    return render_template('livingap2.html')

@app.route('/e2g')
def led4off():
    rpi.output(led4,0)
    return render_template('livingap2.html')

@app.route('/E2A')
def led5on():
    rpi.output(led5,1)
    return render_template('bedroom.html')

@app.route('/e2a')
def led5off():
    rpi.output(led5,0)
    return render_template('bedroom.html')

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='iphere')