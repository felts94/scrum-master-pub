from flask import Flask, session, request, jsonify, make_response
import os, time, datetime, json
from pathlib import Path
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#teams = {}
#people = {}



def bad_req(message=None):

    rv = ''
    if message:
        rv = jsonify(message)
    else:
        rv = jsonify({'success':False})

    res = make_response(rv, 400)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return res
    


def success(message=None):
    rv = ''
    if message:
        rv = jsonify(message)
    else:
        rv = jsonify({'success':True})

    res = make_response(rv, 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return res

@app.route('/')
def index():
    with open('data.json') as f:
        teams = json.load(f)
    return jsonify({'teams_obj': teams})

@app.route('/team/create', methods=['POST'])
def teamcreate():
    # global people
    with open('data.json') as f:
        teams = json.load(f)
    if request.method == 'POST':
        content = request.get_json()
        teamname = content.get('team-name', '')
        leader = content.get('leader', '')
        if teamname == '' or leader == '':
            return bad_req()

        # people[leader] = {
        #         "teams":[
        #             {
        #                 "name":teamname,
        #                 "role":"leader",
        #             },
        #         ],
        #     }
        
        teams[teamname] = {"leader":leader, "members": [{"name":leader, "updates":[]}]}
        json.dump(teams, open("data.json",'w'))
        return success()

@app.route('/team/<string:teamname>/', methods=['GET','POST'])
def teamview(teamname):
    with open('data.json') as f:
        teams = json.load(f)
    if request.method == 'POST':
        content = request.get_json()
        new_member = content.get('new-member', False)
        if new_member != False:
            members = teams[teamname]["members"]
            for m in members:
                if m['name'] == new_member:
                    return bad_req({'error':str(new_member + " exists")})
            members.append({"name":new_member, "updates":[]})
            teams[teamname]["members"] = members
            json.dump(teams, open("data.json",'w'))
            return success()
        return bad_req()


    if teams.get(teamname, False):
        return success(teams[teamname])
    
    return bad_req()


@app.route('/update/<string:teamname>/<string:membername>', methods=['GET','POST', 'OPTIONS'])
def teamviewmember(teamname, membername):
    with open('data.json') as f:
        teams = json.load(f)
    # global people
    if request.method == 'POST':
        content = request.get_json()
        print(request, content)
        if content == None:
            return bad_req()
        update = content.get('update')
        if update == None:
            return bad_req()
        members = teams[teamname]["members"]
        for m in members:
            if m['name'] == membername:
                m['updates'].insert(0,{
                'text':update,
                'time': str(datetime.datetime.now().strftime('%A %b %d, %I:%M%p'))
                })
                json.dump(teams, open("data.json",'w'))
                return success()
        return bad_req({'error':str('no member with name ' + membername)})
        

    if request.method == 'GET':
        try:
            for m in teams[teamname]["members"]:
                if m['name'] == membername:
                    return success({'team-name':teamname, 'member-name':membername, 'updates':m['updates']})
            return bad_req('no member with name ' + membername)
        except:
            return bad_req()

    if request.method == 'OPTIONS':
        return

if __name__ == "__main__":
    f = Path("./data.json")
    if not f.exists():
        json.dump({}, open("data.json",'w'))
    app.run(debug=True, host='0.0.0.0')
