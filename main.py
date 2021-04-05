import Login
from flask import Flask,render_template,request,jsonify,session,g,url_for,redirect
import User
import Teams
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

@app.route('/players')
def players():
    if g.user:
        return render_template(
                'players.html',
                players=User.User().GetAllPlayers()
                )

    return redirect(url_for('login'))

@app.route('/RegisterUser', methods=['GET','POST'])
def  registeruser():
    if request.method=='POST':
        data=request.get_json()
        usuario=data['username']
        r=User.User().RegisterUser(usuario)
        return jsonify({'response':r})
    return 'No'
@app.route('/GetAllPlayers')
def GetAllPlayer():
    if g.user:
        return jsonify({ 'response':User.User().GetAllPlayers()})
    return jsonify({'response':False})
@app.route('/Player/<name>')
def GetsPlayer(name):
    if g.user:
        data=User.User().GetPlayer(name)
        return jsonify({'response':data})
    else:
        return 'No'
@app.route('/DeletePlayer/<id_player>')
def DeletePlayer(id_player):
    if g.user:
        #User.User().DeleteUser(id_player)
        return  render_template('deleteplayer.html',id_p=id_player)
    else:
        return 'No'
@app.route('/delete/<player>')
def deletesplayer(player):
    if g.user:
        User.User().DeleteUser(player)
        return redirect(url_for('players'))
    else:
        return 'No'
@app.route('/UpdatePlayer/<id_player>', methods=['GET','POST'])
def UpdatePlayer(id_player):
    if g.user:
        if request.method=='GET':
            return render_template(
                    'UpdatePlayers.html',
                    user=User.User().GetNamePlayer(id_player),
                    id_user=id_player
                    )
        if request.method=='POST':
            data=request.get_json()
            name_user=data['username'][0]
            return jsonify({'response':User.User().UpdatePlayer(id_player,name_user)})

    return 'No'
@app.route('/teams')
def teams():
    if g.user:
        return render_template(
                'teams.html',
                clans=Teams.Team().GetTeams(),
                players=User.User().GetAllPlayers(),
                )
    return 'No'
@app.route('/AddTeam',methods=['POST'])
def addteam():
    if g.user:
        if request.method=='POST':
            team=request.form['txtteams']
            user=request.form['txtuser']
            Teams.Team().AddPlayerClan(team,user)
            return redirect(url_for('teams'))
        pass
    return 'No'
if __name__ =='__main__':
    app.run(debug=True)
