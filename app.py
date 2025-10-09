from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)   
app.secret_key="minirobot123"


posicion =[0,0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if "posicion" not in session:
        session["posicion"] = [0, 0]

    posicion = session["posicion"]

    if request.method == 'POST':
        direccion = request.form['direccion']
        if direccion == 'arriba' and posicion[0] > 0:
            posicion[0] -= 1
        elif direccion == 'abajo' and posicion[0] < 4:
            posicion[0] += 1
        elif direccion == 'izquierda' and posicion[1] > 0:
            posicion[1] -= 1
        elif direccion == 'derecha' and posicion[1] < 4:
            posicion[1] += 1
        
        session["posicion"] = posicion
    return render_template('index.html', posicion=posicion)

if __name__ == '__main__':
    app.run(debug=True)
