from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'eu_amo_o_luiz' 

@app.route('/')
def index():
    if 'tasks' not in session:
        session['tasks'] = []
    
    return render_template('index.html', tasks=session['tasks'])

@app.route('/add', methods=['POST'])
def add():
    new_task = request.form.get('task')
    
    if new_task:
        session['tasks'].append(new_task)
        session.modified = True
        
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 'tasks' in session and 0 <= task_id < len(session['tasks']):
        session['tasks'].pop(task_id)
        session.modified = True
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)