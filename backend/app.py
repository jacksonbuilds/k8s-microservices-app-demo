from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/products")
def get_products():
    products = [
        {"id": 1, "name": "Product 1", "price": 9.99},
        {"id": 2, "name": "Product 2", "price": 12.49},
        {"id": 3, "name": "Product 3", "price": 7.95}
    ]
    return jsonify(products)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
