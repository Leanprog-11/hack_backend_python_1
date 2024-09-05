from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#1
@app.route("/users", methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})

#2
@app.route("/user", methods=['POST'])
def post_user():
    return jsonify({'payload': 'success'})

#3  
@app.route("/user", methods=['DELETE'])
def delete_user():
    return jsonify({'payload': 'success'})

#4  
@app.route("/user", methods=['PUT'])
def put_user():
    return jsonify({'payload': 'success',
    'error': False
    })

#5
@app.route("/api/v1/users", methods=['GET'])
def get_users_api():
    return jsonify({'payload': [] })

#6
@app.route("/api/v1/user", methods=['POST'])
def post_users_api():
    email = request.args.get('email')
    name = request.args.get('name')
    if not email or not name:
        return jsonify({'error': 'Invalid input, missing email or name'}), 400
    response = {
        'payload': {
            'email': email,
            'name': name,
        }
    }
    return jsonify(response), 200

#7
@app.route("/api/v1/user/add", methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')

    if not email or not name or not user_id:
        return jsonify({'error': 'Invalid input, missing email, name, or id'}), 400

    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': user_id,
        }
    }
    return jsonify(response), 200

#8
@app.route("/api/v1/user/create", methods=['POST'])
def create_user():
    data = request.get_json()

    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')

    if not email or not name or not user_id:
        return jsonify({'error': 'Invalid input, missing email, name, or id'}), 400
    
    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': user_id,
        }
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)