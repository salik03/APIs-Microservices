from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Initialize data
csv_file_name = "ArticleData.csv"
try:
    existing_data = pd.read_csv(csv_file_name)
except FileNotFoundError:
    existing_data = pd.DataFrame(columns=["AID", "Article", "NAME", "INSURED", "PRODUCT TYPE", "GROSS WT", "COUNTRY"])


@app.route('/add_row', methods=['POST'])
def add_row():
    new_row = {}
    for column in existing_data.columns:
        value = request.json.get(column)
        new_row[column] = value

    global existing_data
    existing_data = existing_data.append(new_row, ignore_index=True)
    existing_data.to_csv(csv_file_name, mode='w', index=False)
    
    return jsonify({"message": "Data has been saved to {}".format(csv_file_name)})


if __name__ == '__main__':
    app.run(debug=True)
