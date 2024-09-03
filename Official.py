from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data storage
data_storage = []

    # {"id": 1, "name": "Aarav Sharma", "age": 20, "email": "aarav.sharma@example.com", "grade": "A"},
    # {"id": 2, "name": "Ishita Patel", "age": 21, "email": "ishita.patel@example.com", "grade": "B"},
    # {"id": 3, "name": "Rohan Gupta", "age": 22, "email": "rohan.gupta@example.com", "grade": "C"}

@app.route('/addemployees', methods=['POST'])
def add_employee():
    
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
# http://localhost:4000/addemployees
           
@app.route('/editemployee/<int:id>', methods=['PUT'])
def update_employee(id):
    
    data = request.json             
    

    for emp in data_storage:
        if emp['id'] == id:
            print('EMP  = ' , emp)
            # data_storage[id] = emp
            print('DATA_STORAGE= ', data_storage)
            emp = data
            #data_storage = emp
            #data_storage['id']=emp
            print('DATA_STORAGE= ', emp)
            return jsonify({'status': 'DATA UPDATED','message': emp}), 200 
        
    data_storage[id] = emp  

    print('DATA_STORAGE[id]=')
 
    # Respond with a success message and the updated record
    # return jsonify({
    #     'status': 'Updated Successfully',
    #     'message': 'Record updated successfully',
    #     'Updated Record': data
    # }), 200


# Body Data for PUT request
# http://localhost:4000/editemployee/1

            # {
            #     "age": 23,
            #     "email": "kiara.joshi@example.com",
            #     "grade": "A",
            #     "id": 8,
            #     "name": "Kiara Joshi"
            # }


@app.route('/getemployees', methods=['GET'])
def getemployees():

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
# http://localhost:4000/getemployees



@app.route('/getemployee/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    # Search for the employee with the specified ID
    for emp in data_storage:
        if emp['id'] == id:
            return jsonify(emp), 200
    
    # If the employee with the given ID is not found
    return jsonify({
        'status': 'error',
        'message': 'employee not found'
    }), 404

# Body Data for GET request - individual records
# http://localhost:4000/getemployee/1



@app.route('/deleteemployee/<int:index>', methods=['DELETE'])
def delete_employee(index):
    # Check if the index is valid
    if index < 0 or index >= len(data_storage):
        return jsonify({
            'status': 'error',
            'message': 'Index out of range'
        }), 404

    # Remove the employee data at the given index
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
# http://localhost:4000/deleteemployee/1



if __name__ == '__main__':
    app.run(host='localhost', port=3000)



#   Make sure the POST method contain only one [] brackates and multiple {} bracket in it.
#   like  - [{"age":20,"email":"aarav.sharma@example.com","grade":"A","id":1,"name":"ATISH PANDE"},
#            {"age":20,"email":"aarav.sharma@example.com","grade":"A","id":2,"name":"Bhushan Shahare"}
#           ]

