import Login
from flask import Flask,render_template,request,jsonify,session,g,url_for,redirect
app=Flask(__name__)
app.secret_key = "key_hash"
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        data=request.get_json()
        aux = data['data']
        if Login.Login(aux[0],aux[1]).search():
            session.pop('user', None)
            session["user"] = aux[1]
            return jsonify({'response':True})
        else:
            return jsonify({'response':False})
    return render_template('login.html')

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
@app.route('/home')
def home():
    if g.user:
        return render_template('home.html')
    return redirect(url_for('login'))
if __name__ =='__main__':
    app.run(debug=True)
