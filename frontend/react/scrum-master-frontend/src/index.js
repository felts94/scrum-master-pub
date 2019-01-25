import React from 'react';
import ReactDOM from 'react-dom';
import axios from "axios"
import './index.css';
import App from './App';
import TeamCollection from './TeamCollection';
import * as serviceWorker from './serviceWorker';

const alld = {
    "teams_obj": {
        "App Team 1": {
            "leader": "Kyle",
            "members": [
                {
                    "name": "Kyle",
                    "updates": [
                        {
                            "text": "Finished app dev _____",
                            "time": "Monday Jan 07, 11:08 PM"
                        },
                        {
                            "text": "Finished app dev _____",
                            "time": "Monday Jan 07, 11:08 PM"
                        }
                    ]
                },
                {
                    "name": "Kyle Felter",
                    "updates": [
                        {
                            "text": "Finished app dev _____",
                            "time": "Monday Jan 07, 11:08 PM"
                        },
                        {
                            "text": "Finished app dev _____",
                            "time": "Monday Jan 07, 11:08 PM"
                        },
                        {
                            "text": "Finished app dev _____",
                            "time": "Monday Jan 07, 11:08 PM"
                        },
                        {
                            "text": "Finished app dev _____",
                            "time": "Monday Jan 07, 11:08 PM"
                        }
                    ]
                }
            ]
        }
    }
}

// console.log(alld)
// alld = async () => {
//     try {
//       // const url =
//       //   window.graphUrl === "__GRAPH_URL__" ? "/data.json" : window.graphUrl;
//       const res = await axios.get(
//         "http://localhost:5000/"
//       );;
//       return res
//     } catch (err) {
//       console.error(err);
//     }
//   };
//   console.log(alld)
ReactDOM.render(<TeamCollection alld={alld}/>, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
