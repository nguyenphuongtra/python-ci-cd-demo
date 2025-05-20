from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []  # Danh sách lưu các todo

@app.route('/')
def home():
    return "Todo List Flask App!"

@app.route('/todos', methods=['GET'])
def get_todos():
    """Lấy danh sách todo."""
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    """Thêm một todo mới."""
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({'error': 'Missing task'}), 400
    todo = {'id': len(todos) + 1, 'task': data['task']}
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Xóa một todo theo id."""
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'result': 'Deleted'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)