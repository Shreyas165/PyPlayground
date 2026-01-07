from flask import Flask, request, render_template, send_from_directory
import pandas as pd
import os

app = Flask(__name__)
data_dir = 'static/data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    country = request.form.get('country')
    message = request.form.get('message')

    # Define the path to the Excel file
    excel_path = os.path.join(data_dir, 'Book1.xlsx')

    # Load existing data or create a new DataFrame
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path, engine='openpyxl')
    else:
        df = pd.DataFrame(columns=['Name', 'Email', 'Country', 'Message'])

    # Append new data (using pd.concat instead of deprecated append)
    new_row = pd.DataFrame([{'Name': name, 'Email': email, 'Country': country, 'Message': message}])
    df = pd.concat([df, new_row], ignore_index=True)

    # Save the DataFrame to the Excel file
    df.to_excel(excel_path, index=False, engine='openpyxl')

    return 'Form submitted successfully!'

# Game routes - serve HTML files instead of running Python scripts
@app.route('/run-script')
def run_script():
    return send_from_directory('static/games', 'snake1.html')

@app.route('/run-script2')
def run_script2():
    return send_from_directory('static/games', 'snake2.html')

@app.route('/run-script3')
def run_script3():
    return send_from_directory('static/games', 'tictactoe.html')

@app.route('/run-script7')
def run_script7():
    return send_from_directory('static/games', 'breakout.html')

@app.route('/run-script77')
def run_script77():
    return send_from_directory('static/games', 'breakout2.html')

@app.route('/run-script8')
def run_script8():
    return send_from_directory('static/games', 'dodge.html')

@app.route('/run-script9')
def run_script9():
    return send_from_directory('static/games', 'shootmaster.html')

@app.route('/run-script10')
def run_script10():
    return send_from_directory('static/games', 'tetris.html')


if __name__ == '__main__':
    app.run(debug=True)