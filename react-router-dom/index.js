import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter, Route, Routes, NavLink, useParams} from 'react-router-dom'; 

function Home(){
  return(
<div>
    <h2>Home</h2>
    Home..
  </div>
  );
}

var contents =[
  {id:"1" , title:'HTML', desc : "html is.."},
  {id:"2" , title:'React', desc : "react is.."},
  {id:"3" , title:'Js', desc : "js is.."}  
]

function Topic(){
  var params = useParams();
  var topic_id = params.id;
  var selected_topic={
    title:"Sorry",
    desc:"Not Found"
  }

  for(var i=0; i<contents.length; i++){
    if(Number(contents[i].id) === Number(topic_id)){
     selected_topic.title = contents[i].title;
     selected_topic.desc = contents[i].desc;
     break;
    }
  }
  // console.log("params", params, ":" ,topic_id);
    return (
      <div>
        <h3>{selected_topic.title}</h3>
        {selected_topic.desc}
      </div>
    )
}
function Topics(){
  var lis =[];
  for(var i=0; i<contents.length;i++){
    lis.push (<li key={contents[i].id}><NavLink to={contents[i].id}>{contents[i].title}</NavLink></li>)
  }
  return(
<div>
    <h2>Topics</h2>
    <ul>
      {lis}
    </ul>

    <Routes>
    <Route path=":id" element={<Topic/>}/>
    </Routes> 
  </div>
  );
}

function Contact(){
  return(
<div>
    <h2>contact</h2>
    contact..
  </div>
  );
}


function App(){
  return (
    <div>
      <h1>React router dom ex</h1>
      <ul>
        <li><NavLink to="/">Home</NavLink></li>
        <li><NavLink  to="/topics">Topic</NavLink></li>
        <li><NavLink to="/contact">Contact</NavLink></li>

      </ul>
      <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/topics/*" element={<Topics/>}/>
      <Route path="/contact" element={<Contact/>}/>
      <Route path="*" element={"Not Found"}/>
      </Routes>
    </div>
  );
}
ReactDOM.render(
  <React.StrictMode><BrowserRouter><App /></BrowserRouter></React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
