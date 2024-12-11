from flask import Flask, request, jsonify
from flasgger import Swagger
from zeep import Client

app = Flask(__name__)
swagger = Swagger(app)

# Servicio SOAP
SOAP_URL = "http://www.dneonline.com/calculator.asmx?WSDL"
client = Client(SOAP_URL)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    Responde con un mensaje de Hola Mundo.
    ---
    responses:
      200:
        description: Un mensaje de Hola Mundo.
        content:
          text/plain:
            example: "Hola Mundo desde un servicio SOAP"
    """
    return "Hola Mundo desde un servicio SOAP"

@app.route('/add', methods=['GET'])
def add_numbers():
    """
    Suma dos números usando un servicio SOAP.
    ---
    parameters:
      - name: num1
        in: query
        type: integer
        required: true
        description: El primer número.
      - name: num2
        in: query
        type: integer
        required: true
        description: El segundo número.
    responses:
      200:
        description: El resultado de la suma.
        content:
          application/json:
            example: { "result": 10 }
    """
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    
    # Llamada SOAP para la suma
    result = client.service.Add(num1, num2)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
