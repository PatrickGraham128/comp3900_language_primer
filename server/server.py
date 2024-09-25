from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json

data = {
  "groups": [],
  "students": []
}

app = Flask(__name__)
CORS(app)

@app.route('/api/groups', methods=['GET'])
def get_groups():
    # TODO: (sample response below)
    return jsonify(data['groups'])

@app.route('/api/students', methods=['GET'])
def get_students():
    """
    Route to get all students
    return: Array of student objects
    """
    # TODO: (sample response below)
    return jsonify(data['students'])

@app.route('/api/groups', methods=['POST'])
def create_group():
    """
    Route to add a new group
    param groupName: The name of the group (from request body)
    param members: Array of member names (from request body)
    return: The created group object
    """
    
    # Getting the request body (DO NOT MODIFY)
    group_data = request.json
    group_name = group_data.get("groupName")
    group_members = group_data.get("members")
    
    # TODO: implement storage of a new group and return their info (sample response below)
    id = data['groups'][-1]['id'] + 1 if len(data['groups']) > 0 else 0

    students = []

    for member in group_members:
        if (len(data['students']) > 0):
            student = {"id": data['students'][-1]['id'] + 1, "name": member}
        else:
            student = {"id": 0, "name": member}
        students.append(student)
        data['students'].append(student)

    group = {
        "id": id,
        "groupName": group_name,
        "members": students,
    }

    print(group)

    data['groups'].append(group)

    return jsonify(group), 201

@app.route('/api/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    """
    Route to delete a group by ID
    param group_id: The ID of the group to delete
    return: Empty response with status code 204
    """
    # TODO: (delete the group with the specified id)
    for group in data['groups']:
        if group['id'] == group_id:
            data['groups'].remove(group)

    return '', 204  # Return 204 (do not modify this line)

@app.route('/api/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    """
    Route to get a group by ID (for fetching group members)
    param group_id: The ID of the group to retrieve
    return: The group object with member details
    """
    # TODO: (sample response below)
    for group in data['groups']:
        if group['id'] == group_id:
            return jsonify(group)
    
    abort(404, "Group not found")

if __name__ == '__main__':
    app.run(port=3902, debug=True)


# edge case - if two students have the same name