from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/pagina1', methods=['GET', 'POST'])
def pagina1():
    pnotas = None
    estado = ""

    if request.method == 'POST':
        num1 = int(request.form['nuno'])
        num2 = int(request.form['ndos'])
        num3 = int(request.form['ntres'])
        asistencia = int(request.form['asis'])

        # Validación de rango de notas y asistencia
        if 10 <= num1 <= 70 and 10 <= num2 <= 70 and 10 <= num3 <= 70 and 0 <= asistencia <= 100:
            pnotas = round((num1 + num2 + num3) / 3, 1)
            if pnotas >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"
        else:
            estado = "Valores fuera del rango permitido"

    return render_template('ejercicio 01.html', pnotas=pnotas, estado=estado)

@app.route('/pagina2', methods=['GET', 'POST'])
def pagina2():
    nombre_mas_largo = ""
    longitud_mas_larga = 0

    if request.method == 'POST':
        nombre1 = request.form['nuno']
        nombre2 = request.form['ndos']
        nombre3 = request.form['ntres']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud_mas_larga = len(nombre_mas_largo)

    return render_template('ejercicio 02.html', nombre_mas_largo=nombre_mas_largo, longitud_mas_larga=longitud_mas_larga)

if __name__ == '__main__':
    app.run(debug=True)
