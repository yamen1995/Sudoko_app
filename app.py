from flask import Flask, render_template, jsonify, request
from logic import *

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_board')
def new_board():
    board = generate_puzzle_board()
    return jsonify({"board": board})

@app.route('/solve', methods=['POST'])
def solve():
    try:
        board = request.json.get('board')
        solved_board = solve_sudoku(board)[1]
        return jsonify({"solved_board": solved_board})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/check', methods=['POST'])
def check():
    try:
        data = request.get_json()
        board = data.get('board')
        if not isinstance(board, list) or len(board) != 9:
            return jsonify({"valid": False, "error": "Invalid board format"})
        is_valid = check_board(board)
        return jsonify({"valid": is_valid})
    except Exception as e:
        return jsonify({"valid": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)