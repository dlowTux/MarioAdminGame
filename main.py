from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return  render_template('login.html')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        data=request.get_json()
        print(data)
        return jsonify({'response':'Hola'})
        pass
    return render_template('login.html')
if __name__ =='__main__':
    app.run(debug=True)
