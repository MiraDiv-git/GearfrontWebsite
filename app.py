from flask import Flask, jsonify
from flask import request
from flask import render_template,send_from_directory
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/downloads/<path:filename>')
def downloads(filename):
    return send_from_directory('downloads', filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)