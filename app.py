from flask import Flask, render_template
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_scripts')
def run_scripts():
    # Execute main.py
    main_result = subprocess.run(['python3', 'main.py'], capture_output=True, text=True)

    # Execute Program.java

    java_result = subprocess.run(['python3', 'Checkbox.py'], capture_output=True, text=True)

    # Combine results
    combined_output = main_result.stdout + '\n' + java_result.stdout

    return combined_output


if __name__ == '__main__':
    app.run(debug=True)
