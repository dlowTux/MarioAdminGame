import Login
from flask import Flask,render_template,request,jsonify,session,g,url_for,redirect
import User
import Teams
import tournaments
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
            data=request.get_json()
            team=data['username'][0]
            user=data['username'][1]
            r=Teams.Team().AddPlayerClan(team,user)
            return  jsonify({'response':r})
    return 'No'
@app.route('/DeleteMemberClan/<id_player>')
def DeleteMemberClan(id_player):
    if g.user:
        Teams.Team().DeleteMemberClan(id_player)
        return redirect(url_for('teams'))
    return 'No'
@app.route('/ResetClans')
def resetclans():
    if g.user:
        Teams.Team().ResetClans()
        return redirect(url_for('teams'))
    return 'No'
@app.route('/tournament')
def tournament():
    c=tournaments.Tournament().GetTournament('1')
    s=tournaments.Tournament().GetTournament('2')
    p=tournaments.Tournament().GetTournament('3')
    return render_template(
            'tournaments.html',
            teams=Teams.Team().GetTeams(),
            players=User.User().GetAllPlayers(),
            single=s,
            clans=c,
            point=p,
            len_p=len(p),
            len_c=len(c),
            len_single=len(s)
            )

@app.route('/AddTournament', methods=['POST'])
def AddTournament():
    if g.user:
        data=request.get_json()
        name=data['tournament'][0]
        Type=data['tournament'][1]
        r=tournaments.Tournament().RegisterTournament(name,Type)
        return jsonify({'response':r})
    return 'None'
@app.route('/AddPlayerTournament',methods=['POST'])
def AddTournamentPlayer():
    if g.user:
        data=request.get_json()
        id_tournament=data['tournament'][0]
        id_player=data['tournament'][1]
        r=tournaments.Tournament().AddPlayerTournament(id_tournament,id_player)
        return jsonify({'response':r})
    return 'No'
@app.route('/AddTeamTournament',methods=['POST'])
def AddTeamTournament():
    if g.user:
        data=request.get_json()
        id_tournament=data['tournament'][0]
        id_clan=data['tournament'][1]
        r=tournaments.Tournament().AddClanTournament(id_clan,id_tournament)
        return jsonify({'response':r})
    return 'No'
@app.route('/AddPonitsSeries', methods=['POST'])
def AddPonitsSeries():
    if g.user:
        data=request.get_json()
        id_tournament=data['tournament'][0]
        id_player=data['tournament'][1]
        r=tournaments.Tournament().RegisterPointsSeries(id_tournament,id_player)
        return jsonify({'response':r})
    return 'No'
if __name__ =='__main__':
    app.run(debug=True)
