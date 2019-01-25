import os, time
# @app.route('/')
# def index():
#     return jsonify({'teams_obj': teams, 'people_obj': people})

APP_URL = 'http://127.0.0.1:5000'

#create team

# @app.route('/team/create', methods=['POST'])
# def teamcreate():
#     global people
#     global teams
#     if request.method == 'POST':
#         content = request.get_json()
#         teamname = content.get('teamname', '')
#         leader = content.get('leader', '')
#         if teamname == '' or leader == '':
#             return bad_req()

#         people[leader] = {
#                 "teams":[
#                     {
#                         "name":teamname,
#                         "role":"leader",
#                     },
#                 ],
#             }
        
#         teams[teamname] = {"leader":leader, "members": {}}
#         return success()

# @app.route('/team/<string:teamname>/', methods=['GET','POST'])
# def teamview(teamname):
#     global teams
#     global people
#     if request.method == 'POST':
#         content = request.get_json()
#         new_member = content.get('new-member')
#         if new_member != None:
#             members = teams[teamname]["members"]
#             members[new_member] = {
#                 'updates':[]
#             }
#             teams[teamname]["members"] = members
#             return success()
#         return bad_req()


#     if teams.get(teamname, False):
#         leader = teams[teamname]['leader']
#         return jsonify({'team':teams[teamname], 'leader': leader})


# @app.route('/team/<string:teamname>/<string:membername>', methods=['GET','POST'])
# def teamviewmember(teamname, membername):
#     global teams
#     global people
#     if request.method == 'POST':
#         content = request.get_json()
#         update = content.get('update')
#         if update == None:
#             return bad_req()
#         members = teams[teamname]["members"]
#         m = members.get('membername')
#         if m != None:
#             m['updates'].insert(0,{
#                 'text':update,
#                 'time': str(time.now())
#             })
#             members['membername'] = m

#         teams[teamname]["members"] = members
#     return success()

# # @app.route('/team/create', methods=['GET', 'POST'])
# # def teamcreate():
# #     if request.method == 'POST':
# #         session['team'] = request.form['teamname']
# #         return redirect(url_for('teamview', teamname=request.form['teamname']))
# #     return '''
# #         <form method="post">
# #             <p><input type=text name=teamname>
# #             <p><input type=submit value="Create Team">
# #         </form>
# #     '''
# app.run(debug=True, host='0.0.0.0')
