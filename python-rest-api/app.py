from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {'id': 0, 'title': 'Data Engineering'},
    {'id': 1, 'title': 'Data Science'},
    {'id': 2, 'title': 'Project Management'},
    {'id': 3, 'title': 'Software Engineering'},
    {'id': 4, 'title': 'Web Development'}
    ]

@app.route('/')
def index():
    return "Welcome to Python API Tutorial"

@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'courses': courses})

@app.route('/courses/<int:id>', methods=['GET'])
def get_courses(id):
    return jsonify({'courses': courses[id]})

@app.route('/courses', methods=['POST'])
def create_course():
    course = {'id': 5, 'title': 'Human Resources'}
    courses.append(course)
    return jsonify({'courses': courses})

@app.route('/courses/<int:id>', methods=['PUT'])
def course_update(id):
    courses[id]['title']="Project and Product Management"
    return jsonify({'courses': courses[id]})

@app.route('/courses/<int:id>', methods=['DELETE'])
def course_delete(id):
    courses.remove(courses[id])
    return jsonify({'courses': courses})

if __name__ == "__main__":
    app.run(debug=True)