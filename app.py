from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    return jsonify({"message": "Webhook recibido correctamente"}), 200

if __name__ == "__main__":
    app.run(debug=False)



