import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./Form"
const App = () => (
  <React.Fragment>
    <DataProvider endpoint="polls/api/question" 
                render={data => <Table data={data} />} />
    <Form endpoint="/admin/polls/question/add/"/>
  </React.Fragment>
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;