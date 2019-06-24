import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import DetailCheckList from "./components/DetailCheckList";

class App extends React.Component {
  state = {
      score: {
          punctuationScore: 0,
          trigramScore: 0,
          capitalScore: 0,
          repetitionScore: 0,
          spaceRatioScore: 0,
          lengthScore: 0,
          spaceScore: 0,
          total: 0
      },
      message: "",
      showBreakdown: false
  };

  onMessageChange(text) {
    this.setState({message: text});
  }

  render() {
      return (
          <div className="App">
            <div className="w-50 w-sm-100 mx-auto">
              <h1 className="App-header"> ACNL Letter Scorer</h1>
              <textarea className="form-control mt-5"
                        placeholder="Enter your message here.."
                        value={this.state.message} onChange={(event) => this.onMessageChange(event.target.value)}/>
              <button className="btn btn-primary m-2" onClick={this.getScore.bind(this)}>Submit</button>
                {this.state.showBreakdown ? <DetailCheckList {...this.state.score} /> : ""}
            </div>

          </div>
      );
  }

  getScore() {
    axios.post("/score", {message:this.state.message})
        .then(response => {
            console.log(response);
            this.setState({score: response.data, showBreakdown:true})
        })
  }
}

export default App;
