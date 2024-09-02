from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data storage
data_storage = []

    # {"id": 1, "name": "Aarav Sharma", "age": 20, "email": "aarav.sharma@example.com", "grade": "A"},
    # {"id": 2, "name": "Ishita Patel", "age": 21, "email": "ishita.patel@example.com", "grade": "B"},
    # {"id": 3, "name": "Rohan Gupta", "age": 22, "email": "rohan.gupta@example.com", "grade": "C"}

@app.route('/addstudent', methods=['POST'])
def add_students():
    
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


#Body Data for POST request
# http://localhost:4000/addstudent
            # {
            #     "age": 20,
            #     "email": "aarav.sharma@example.com",
            #     "grade": "A",
            #     "id": 1,
            #     "name": "Aarav Sharma"
            # }




@app.route('/editstudent/<int:index>', methods=['PUT'])
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


# Body Data for PUT request
# http://localhost:4000/editstudent/1

            # {
            #     "age": 23,
            #     "email": "kiara.joshi@example.com",
            #     "grade": "A",
            #     "id": 8,
            #     "name": "Kiara Joshi"
            # }


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

# Body Data for PUT request
# http://localhost:4000/getstudents



@app.route('/getstudent/<int:id>', methods=['GET'])
def get_student_by_id(id):
    # Search for the student with the specified ID
    for student in data_storage:
        if student['id'] == id:
            return jsonify(student), 200
    
    # If the student with the given ID is not found
    return jsonify({
        'status': 'error',
        'message': 'Student not found'
    }), 404

# Body Data for GET request - individual records
# http://localhost:4000/getstudent/1
# http://localhost:4000/getstudent/2
# http://localhost:4000/getstudent/3


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

# Body Data for DELETE request - individual records
# http://localhost:4000/deletestudent/1
# http://localhost:4000/deletestudent/2
# http://localhost:4000/deletestudent/3


if __name__ == '__main__':
    app.run(host='localhost', port=4000)



#   Make sure the POST method contain only one [] brackates and multiple {} bracket in it.
#   like  - [{"age":20,"email":"aarav.sharma@example.com","grade":"A","id":1,"name":"ATISH PANDE"},
#            {"age":20,"email":"aarav.sharma@example.com","grade":"A","id":2,"name":"Bhushan Shahare"}
#           ]

