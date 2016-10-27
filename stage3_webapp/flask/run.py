from flask import Flask, render_template, request

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/todos', methods=['POST', 'GET'])
def add_new_todo():
    if request.method == 'POST':
        new_todo = request.form.get('new_todo')
        print("You have a new todo: " + str(new_todo))
        todo_list.append(new_todo)

    return render_template('list_todos.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)
