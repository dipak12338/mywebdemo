from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Extract JSON data from the request
    data = request.json

    if data is None:
        # If no JSON data is provided, respond with 400 Bad Request
        return jsonify({'error': 'Bad Request', 'message': 'No JSON data provided'}), 400

    # Log the received data (or process it as needed)
    print('Received data:', data)

    # Example condition: Check for forbidden content
    if 'forbidden_field' in data and data['forbidden_field'] == 'forbidden_value':
        # If forbidden content is detected, respond with 403 Forbidden
        return jsonify({'error': 'Forbidden', 'message': 'Forbidden content detected'}), 403

    # Example condition: Check for a valid endpoint or valid content
    if data.get('endpoint') != 'valid_endpoint':
        # If the endpoint is invalid, respond with 404 Not Found
        return jsonify({'error': 'Not Found', 'message': 'Invalid endpoint'}), 404

    # Example condition: Check for a specific name
    if data.get('name') != 'Sahil':
        # If the name is invalid, respond with 404 Not Found
        return jsonify({'error': 'Not Found', 'message': 'Invalid name'}), 404

    # If all checks pass, process the request and respond with 200 OK
    print('Received valid webhook data:', data)
    return jsonify({'status': 'success', 'message': 'Request processed successfully'}), 200

@app.route('/test', methods=['GET'])
def test():
    print('Received the GET request successfully.....')
    return jsonify({'Message': 'Received the GET request successfullya at User End'}), 200

    



if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
