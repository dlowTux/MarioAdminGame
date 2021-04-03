import Login
from flask import Flask,render_template,request,jsonify,session
app=Flask(__name__)
@app.route('/')
def home():
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
if __name__ =='__main__':
    app.run(debug=True)
