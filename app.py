from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario de precios
precios = {
    "GRAN BURGUER": 9000,
    "CHESSE FULL": 8800,
    "BURGUER CLASSIC": 8300,
    "BURGUER CRIOLLA": 8700,
    "BURGUER MEX": 9000,
    "CHESSE BURGUER": 8500,
    "KIDS": 5900,
    "PAPAS SOLTERAS": 6000,
    "PAPAS CHEDDAR": 6500,
    "PAPAS HUEVONAS": 6500
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actualizar')
def actualizar():
    return render_template('actualizar.html')

@app.route('/pedido', methods=['POST'])
def pedido():
    pedido = request.form['pedido']
    bebida = request.form['bebida']
    cliente = request.form['cliente']
    direccion = request.form['direccion']

    pedidos = pedido.split(',')
    bebidas = bebida.split(',')

    total_pedido = sum(precios.get(p.strip(), 0) for p in pedidos)
    total_bebida = sum(precios.get(b.strip(), 0) for b in bebidas)
    total = total_pedido + total_bebida

    return jsonify({"pedido": pedido, "bebida": bebida, "cliente": cliente, "direccion": direccion, "total": total})

@app.route('/actualizar-precio', methods=['POST'])
def actualizar_precio():
    producto = request.form['producto']
    nuevo_precio = float(request.form['nuevo_precio'])
    precios[producto] = nuevo_precio
    return jsonify({"producto": producto, "nuevo_precio": nuevo_precio})

if __name__ == '__main__':
    app.run(debug=True)
