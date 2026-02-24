from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_tasks():
    data = request.json
    tasks = data.get('tasks', [])
    sort_field = data.get('sort_field', 'title')
    order = data.get('order', 'asc')

    # Lógica de ordenamiento
    reverse = True if order == 'desc' else False
    sorted_list = sorted(tasks, key=lambda x: x.get(sort_field, '').lower(), reverse=reverse)

    return jsonify({"status": "success", "sorted_tasks": sorted_list})

if __name__ == '__main__':
    print("Microservicio de Ordenamiento corriendo en http://localhost:5000")
    app.run(port=5000)