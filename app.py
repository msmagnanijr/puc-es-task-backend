from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_cors import CORS
import requests



app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

swagger = Swagger(app, template_file='swagger.yaml')

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]
    return jsonify({'tasks': task_list})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify({'task': {'id': task.id, 'title': task.title, 'description': task.description}})
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(title=data['title'], description=data.get('description'))
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully', 'task': {'id': task.id, 'title': task.title, 'description': task.description}}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.json
    task.title = data['title']
    task.description = data.get('description')
    db.session.commit()
    return jsonify({'message': 'Task updated successfully', 'task': {'id': task.id, 'title': task.title, 'description': task.description}})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})


@app.route('/tasks/get_news', methods=['GET'])
def get_news():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Keyword parameter is missing'}), 400

    response = requests.get(f'http://localhost:6000/get_news?keyword={keyword}')

    if response.status_code == 200:
        news_data = response.json()
        return jsonify({'news': news_data})

    return jsonify({'error': 'Failed to fetch news data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
