from flask import Flask, request

app = Flask(__name__)

vocales = ["a", "e", "i", "o", "u"]

@app.route("/")
def home():
    return """
    <h1>Comprobador de Vocales</h1>
    <p>Escribe un carácter y pulsa comprobar:</p>
    <form action="/comprobar" method="get">
        <input type="text" name="caracter" maxlength="1" required>
        <button type="submit">Comprobar</button>
    </form>
    """

@app.route("/comprobar")
def comprobar():
    caracter = request.args.get("caracter", "").lower()

    if caracter == "":
        return "<p style='color:red;'>No has escrito ningún carácter</p>"

    # 👉 NUEVO: comprobar si es un punto
    if caracter == ".":
        return "<p style='color:black; font-size:24px;'>Que te jodan Ancor</p>" \
               "<a href='/'>Volver</a>"

    # Comprobar si es letra
    if not caracter.isalpha():
        return f"<p style='color:orange; font-size:24px;'>{caracter} no es una letra</p>" \
               "<a href='/'>Volver</a>"

    if carac
