import base64
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'root'



@app.route('/')
def home():
    if 'count' in session:
        print('key exists')
    else:
        session['count'] = 0
    if 'count_value' in session:
        print('key exists')
    else: session['count_value'] = 1
    if 'page_views' in session:
        print('key exists')
    else:
        session['page_views'] = 0
    session['count'] += 1
    session['page_views'] += 1
    return render_template('index.html', count = session['count'], page_views = session['page_views'])

@app.route('/+2')
def increment_by_2():
    session['count'] += session['count_value']
    return redirect('/')

@app.route('/change_counter_increment', methods = ['POST'] )
def change_counter():
    session['count_value'] = int(request.form['increment_value']) - 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.pop('count')
    session.pop('page_views')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5002)
