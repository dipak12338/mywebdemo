from flask import Flask, request, jsonify

app = Flask(__name__)

def callback_function(data):
    # This is the callback function that performs an action after processing
    print("Callback function called with data:", data)
    # Perform any additional actions here, like logging to a database, sending a notification, etc.

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



   

    # Call the callback function with the received data
    callback_function(data)

    # If all checks pass, process the request and respond with 200 OK
    print('Received valid webhook data:', data)
    return jsonify({'status': 'success', 'message': 'Request processed successfully'}), 200

@app.route('/test', methods=['POST'])
def test():
    data1 = request.json
    # Log the received data (or process it as needed)
    print('Received data:', data1)
    return jsonify({'message': 'Received the POST request successfully'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
