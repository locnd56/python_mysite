import React, { Component } from "react";
import PropTypes from "prop-types";
class Form extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired
  };
  state = {
    question_text: "",
    pub_date: ""
  };
  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };
  handleSubmit = e => {
    e.preventDefault();
    const { question_text, pub_date } = this.state;
    const lead = { question_text, pub_date };
    const conf = {
      method: "post",
      body: JSON.stringify(lead),
      headers: new Headers({ "Content-Type": "application/json" })
    };
    fetch(this.props.endpoint, conf).then(response => console.log(response));
  };
  render() {
    const { question_text, pub_date } = this.state;
    return (
      <div className="column">
        <form onSubmit={this.handleSubmit}>
          <div className="field">
            <label className="label">Question</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="question_text"
                onChange={this.handleChange}
                value={question_text}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">pub_date</label>
            <div className="control">
              <textarea
                className="textarea"
                type="text"
                name="pub_date"
                onChange={this.handleChange}
                value={pub_date}
                required
              />
            </div>
          </div>
          <div className="control">
            <button type="submit" className="button is-info">
              Submit question
            </button>
          </div>
        </form>
      </div>
    );
  }
}
export default Form;