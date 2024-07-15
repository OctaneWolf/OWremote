from flask import Flask, request, jsonify
import subprocess
app = Flask(__name__)


@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({"output": result.stdout, "error": result.stderr})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
