import csv
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

column_names = ["EMAIL", "MOBILE NUMBER", "USERNAME", "PASSWORD"]
csv_file = "user_data.csv"


def create_csv_file():
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)


def register_user(email, mobile_number, username, password):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, mobile_number, username, password])


def login_user(username, password):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            saved_username, saved_password = row[2], row[3]
            if username == saved_username and password == saved_password:
                return True
    return False


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    mobile_number = data.get('mobile_number')
    username = data.get('username')
    password = data.get('password')
    register_user(email, mobile_number, username, password)
    return jsonify({"message": "User registered successfully!"})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if login_user(username, password):
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Login failed. Invalid username or password."})


if __name__ == "__main__":
    app.run(debug=True)
