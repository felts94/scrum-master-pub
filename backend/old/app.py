from flask import Flask, session, redirect, url_for, escape, request, render_template
import os, time
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
teams = {}
people = {}

@app.route('/')
def index():
    return redirect(url_for('teamcreate'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

@app.route('/team/create', methods=['GET', 'POST'])
def teamcreate():
    global people
    global teams
    if request.method == 'POST':
        teamname = request.form['teamname']
        leader = request.form['leader']
        people = {
            leader:{
                "teams":[
                    {
                        "name":teamname,
                        "role":"leader",
                    },
                ],
            }
        }
        teams[teamname] = {"leader":leader, "members": {}}
        return redirect(url_for('teamview', teamname=request.form['teamname']))
    return '''
        <form method="post">
            <p>Team Name: <input type=text name=teamname>
            <p>Team Leader: <input type=text name=leader>
            <p><input type=submit value="Create Team">
        </form>
    '''

@app.route('/team/<string:teamname>/', methods=['GET','POST'])
def teamview(teamname):
    global teams
    global people
    if request.method == 'POST':
        if request.form.get('newmember') != None:
            members = teams[teamname]["members"]
            members[request.form['newmember']] = {
                'updates':[]
            }
            teams[teamname]["members"] = members
        return redirect(url_for('teamview', teamname=teamname))


    if teams.get(teamname, False):
        leader = teams[teamname]['leader']
        return render_template(
            'team.html', leader=leader, teamname=teamname, members=teams[teamname]["members"])


@app.route('/team/<string:teamname>/<string:membername>', methods=['GET','POST'])
def teamviewmember(teamname, membername):
    global teams
    global people
    if request.method == 'POST':
        members = teams[teamname]["members"]
        m = members.get('membername')
        if m != None:
            m['updates'].insert(0,{
                'text':request['memberupdate'],
                'time': str(time.now())
            })
            members['membername'] = m

        teams[teamname]["members"] = members
    return redirect(url_for('teamview', teamname=teamname))

# @app.route('/team/create', methods=['GET', 'POST'])
# def teamcreate():
#     if request.method == 'POST':
#         session['team'] = request.form['teamname']
#         return redirect(url_for('teamview', teamname=request.form['teamname']))
#     return '''
#         <form method="post">
#             <p><input type=text name=teamname>
#             <p><input type=submit value="Create Team">
#         </form>
#     '''
app.run(debug=True)
