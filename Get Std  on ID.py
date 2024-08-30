from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data storage
data_storage = [
    {"id": 1, "name": "Aarav Sharma", "age": 20, "email": "aarav.sharma@example.com", "grade": "A"},
    {"id": 2, "name": "Ishita Patel", "age": 21, "email": "ishita.patel@example.com", "grade": "B"},
    {"id": 3, "name": "Rohan Gupta", "age": 22, "email": "rohan.gupta@example.com", "grade": "C"}
]

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

if __name__ == '__main__':
    app.run(host='localhost', port=4000)
