import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      msg: null,
    };
  }

  componentDidMount() {
    fetch("http://localhost:5000/hello-world")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            msg: result.message,
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error,
          });
        }
      )
  }

  render() {
    const {error, isLoaded, msg} = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>{msg}</div>
      );
    }
  }
}


ReactDOM.render(
  <App/>,
  document.getElementById('root')
);