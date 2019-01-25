import React, { Component } from 'react';
import Team from './Team'

class TeamCollection extends Component{
    dict = this.props.alld;
    keys = []
    render(){
        {
            var dict = this.props.alld.teams_obj
        }
        return( <div>
        {
          Object.keys(dict).map((key, index) => ( 
            <div key={index}> 
            {key}
            <Team teamname={key} team={dict[key]}/></div>
          ))
        }
      </div>)}
}


export default TeamCollection;