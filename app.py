from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def just_run():
    return render_template('index.html')


app.run(host='0.0.0.0')     # bindati all'indirizzo ip 0, cioè a ciò che docker ti indirizzerà a runtime
# Così binda anche su http://10.0.2.15:5000/ e non solo localhost!





