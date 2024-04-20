from flask import Flask


app = Flask(__name__)



@app.route("/")
def hello_world():
return "<p>Product gone Live!!!</p>"



port_number = 8080


if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0', port=port_number)
