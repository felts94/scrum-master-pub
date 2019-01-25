import React, { Component } from 'react';

// * snip *

function newUpdate(team, name, data) {
  var data = {
    "update": "New update"
  }
  return fetch('http://localhost:5000/update/' + encodeURI(team) + '/' + encodeURI(name), {
    method: 'POST',
    body: '{"update": "New update"}',
    mode: 'no-cors',
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(res => {
    console.log(res)
    return res;
  }).catch(err => err);
}

// async () => {
//   const rawResponse = await fetch(fetch('http://localhost:5000/update/' + encodeURI(teamname) + '/' + encodeURI(member.name), {
//     method: 'POST',
//     headers: {
//       'Accept': 'application/json',
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({a: 1, b: 'Textual content'})
//   });
//   const content = await rawResponse.json();

//   console.log(content);
// }

function logit(data) {
  console.log(data);
}

class Team extends Component {
  render() {
    {
      var teamname = this.props.teamname;
      var leader = this.props.team.leader;
      console.log(this, this.props)
      var members = this.props.team.members;
      var divStyle = {
        background: "#eee",
        padding: "20px",
        margin: "20px"
      };
      var updateInputStyle = {
        background: "#eee",
        marginLeft: "20px",
        marginTop: "10px"
      }
    }
    return (<div>Leader: {leader}
      {members.map(member => <div style={divStyle} key={member.name}>
        {member.name}
        {member.updates.length > 0 && <li style={{ marginTop: "10px" }}>{member.updates[0].time}: {member.updates[0].text}</li>}
        <div style={updateInputStyle}>
          <input type="text" name="update" id="updateText" placeholder="Submit new update"></input>
          <input type="button" value="submit" onClick={async () => {
            const raw = await fetch('http://localhost:5000/update/' + encodeURI(teamname) + '/' + encodeURI(member.name), {
            method: 'POST',
            mode: 'no-cors',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({update: 'New Update'})
            });
            console.log(raw)
            const resp = await raw;
            console.log(resp);
  }}></input>
        </div>
      </div>)}
    </div>)
  }
}


export default Team;