from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)   
app.secret_key="minirobot123"

# Definición de la tabla 5x5 con coordenadas
tabla = [
    [(0,0), (0,1), (0,2), (0,3), (0,4)],
    [(1,0), (1,1), (1,2), (1,3), (1,4)],
    [(2,0), (2,1), (2,2), (2,3), (2,4)],
    [(3,0), (3,1), (3,2), (3,3), (3,4)],
    [(4,0), (4,1), (4,2), (4,3), (4,4)]
]

rojos = [(0,2), (2,1), (4,3)]
verdes = [(0,1), (3,0), (4,4)]

@app.route('/', methods=['GET', 'POST'])
def index():
    if "posicion" not in session:
        session["posicion"] = [0, 0]
        session["points"] = 0

    posicion = session["posicion"]
    puntos = session["points"]

    x, y = posicion

    if request.method == 'POST':
        direccion = request.form['direccion']
        if direccion == 'arriba' and x > 0:
            x -= 1
        elif direccion == 'abajo' and x < 4:
            x += 1
        elif direccion == 'izquierda' and y > 0:
            y -= 1
        elif direccion == 'derecha' and y < 4:
            y += 1
        
        nueva_pos = [x, y]
        

        session["posicion"] = nueva_pos
        #session["points"] = puntos

        valor = tabla[x][y]
        if valor in verdes:  # verde
            session["points"] = session.get("points", 0) + 5
        elif valor in rojos:  # rojo
            session["points"] = session.get("points", 0) - 2

        print("Valor actual:", valor)
        print("Verdes:", verdes)
        print("Rojos:", rojos)
        print("Puntos actuales:", session["points"])

    return render_template("index.html", 
                           puntos=session.get("points", 0),
                           posicion=session["posicion"], 
                           verdes=verdes, 
                           rojos=rojos,
                           tabla=tabla)



if __name__ == '__main__':
    app.run(debug=True)
