from flask import Flask, request, jsonify

app = Flask(__name__)

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
def test():

    #data = request.args.to_dict()

    x = len(data_storage)
    print('Length{(Data_storage) : ', x)

    print('Received the GET request successfully.....')
    return jsonify({'status': 'success','message': 'GET request processed successfully','Data': data_storage
        #'Data2': data_storage[1],
        #'Data3': data_storage[2]
    }), 200



@app.route('/updatestudent/<int:index>', methods=['PUT'])
def update_student(index):
    
    data = request.json             # Extract JSON data from the request

    # Check if the index is valid
    if index < 0 or index >= len(data_storage):
        print('INDEX VALUE : ', index)
        return jsonify({
            'status': 'error',
            'message': 'Index out of range'
        }), 404
        
    # Update the student data at the given index
    data_storage[index] = data

    # Log the updated data
    print('Updated data at index', index, ':', data)

    # Respond with a success message and the updated record
    return jsonify({
        'status': 'Updated Successfully',
        'message': 'Record updated successfully',
        'Updated Record': data
    }), 200

@app.route('/deletestudent/<int:index>', methods=['DELETE'])
def delete_student(index):
    # Check if the index is valid
    if index < 0 or index >= len(data_storage):
        return jsonify({
            'status': 'error',
            'message': 'Index out of range'
        }), 404

    # Remove the student data at the given index
    removed_data = data_storage.pop(index)

    # Log the removed data
    print('Removed data:', removed_data)

    # Respond with a success message and the removed record
    return jsonify({
        'status': 'Deleted Successfully',
        'message': 'Record removed successfully',
        'Removed Record': removed_data
    }), 200


@app.route('/updatestudent/<int:index>', methods=['PATCH'])
def update_student_partial(index):
    # Extract JSON data from the request
    data = request.json

    # Check if the index is valid
    if index < 0 or index >= len(data_storage):
        print('INDEX VALUE : ', index)
        return jsonify({
            'status': 'error',
            'message': 'Index out of range'
        }), 404
        
    #removed_data = data_storage.pop(index)    test
    # Retrieve the current record
    #current_data = data_storage.update(index)
    
    # Update the student data at the given index
    data_storage[index] = data

    # Apply the partial updates
    #current_data.update(data)              already here

    # Log the updated data
    print('Partially updated data at index', index, ':', data_storage)

    # Respond with the success message and the updated record
    return jsonify({
        'status': 'Updated Successfully',
        'message': 'Record partially updated successfully',
        'Updated Record': data_storage
    }), 200




if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='localhost', port=5000)
