
#This is the webhook/API that will receive the request from any website 
# And sent the response with status code 


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
         # Log the received data (or process it as needed)
        print('Received data:', data)
    
        # Respond with a 200 OK status
        return jsonify({'Test Succided ': 'This is the custom message generated by user 21'}), 200

        if data is None:
            # If no JSON data is provided, respond with 400 Bad Request
            return jsonify({'error': 'Bad Request', 'message': 'No JSON data provided'}), 400
    
        # Example condition: Check for forbidden content
        if 'forbidden_field' in data and data['forbidden_field'] == 'forbidden_value':
            # If forbidden content is detected, respond with 403 Forbidden
            return jsonify({'error': 'Forbidden', 'message': 'Forbidden content detected'}), 403

        # Example condition: Check for a valid endpoint or valid content
        if data.get('endpoint') != 'valid_endpoint':
            # If the endpoint is invalid, respond with 404 Not Found
            return jsonify({'error': 'Not Found', 'message': 'Invalid endpoint'}), 404

        # If all checks pass, process the request and respond with 200 OK
        # (Here you can add the logic to process the valid request)
        print('Received valid webhook data:', data)
        return jsonify({'status': 'success', 'message': 'Request processed successfully'}), 200

        test = data.get('name')

        if data.get('name') != 'Sahil':
            # If the endpoint is invalid, respond with 404 Not Found
            return jsonify({'error': 'Not Found', 'message': 'Invalid endpoint'}), 404

            print("TEST value : " ,  test)


        callback_function(data)

@app.route('/test', methods=['POST'])
def test():
        data1 = request.json
        # Log the received data (or process it as needed)
        print('Received data:', data1)
        #print('Received the GET request successfully.....')
        return jsonify({'This is the RETURN statement : Received the POST request successfully.....'}), 200


if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='172.1.0.133', port=5000)


###################################################################################


