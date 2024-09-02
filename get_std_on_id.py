from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data storage
data_storage = []


@app.route('/addstudent', methods=['POST'])
def webhook():
    
    data = request.json             # Extract JSON data from the request

    if data is None:
        # If no JSON data is provided, respond with 400 Bad Request
        return jsonify({'error': 'Bad Request', 'message': 'No JSON data provided'}), 400

    data_storage.append(data)

    # If all checks pass, process the request and respond with 200 OK
    print('Received valid webhook data:', data)    

    return jsonify({
        'status': 'Inseret Successfully...',
        'message': 'Request processed successfully...',
        'Inserted Record': data
    }), 200


@app.route('/getstudents', methods=['GET'])
def getstudents():

    #data = request.args.to_dict()

    x = len(data_storage)
    print('Length{(Data_storage) : ', x)

    print('Received the GET request successfully.....')
    return jsonify(
            {'status': 'success','message': 'GET request processed successfully','Data': data_storage

        #'Data2': data_storage[1],
        #'Data3': data_storage[2]
    }), 200




@app.route('/getstudent/<int:id>', methods=['GET'])
def get_student_by_id(id):
    # Search for the student with the specified ID
    for student in data_storage:
        if student[id] == id:
            return jsonify(student), 200
    
    # If the student with the given ID is not found
    return jsonify({
        'status': 'error',
        'message': 'Student not found'
    }), 404

if __name__ == '__main__':
    app.run(host='localhost', port=4000)
