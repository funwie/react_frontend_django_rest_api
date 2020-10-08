import React from 'react';
import SearchForm from './components/SearchForm'
import OrderDetail from './components/OrderDetail'
import LineItems from './components/LineItems'
import VatDetail from './components/VatDetail'
import NavBar from './components/NavBar'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Alert } from 'react-bootstrap';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      order: {},
      feedBack: '',
      feedbackType: 'light',
      loaded: false
    }
  }

  onOrderSearchSubmitted = (orderId) => {
    if (orderId !== '') {
      this.fetchOrder(orderId);
      return;
    }
    this.setState({
      feedBack: 'Enter order number',
      feedbackType: 'danger',
      loaded: false
    });
  };

  fetchOrder = (orderId) => {
    const apiHost = 'http://localhost:8000';
    const requestUrl = `${apiHost}/api/orders/${orderId}`;
    fetch(requestUrl)
      .then(response => {
        if (!response.ok) {
          this.setState({
            feedBack: 'Could not find order, please check order number and try again',
            feedbackType: 'danger',
            loaded: false
          })
        } else {
          return response.json();
        }
      }).then(data => {
        console.log(data);
        if (data !== undefined) {
          this.setState({
            order: data,
            feedBack: '',
            feedbackType: 'light',
            loaded: true
          })
        }
      }).catch(() => {
        this.setState({
          feedBack: 'An error occurred, please try again',
          feedbackType: 'danger',
          loaded: false
        })
      });
  };

  // move staticElements and dynamicElements to separate components
  render() {
    let staticElements = (
      <div>
        <NavBar />
        <Alert variant={this.state.feedbackType}>{this.state.feedBack}</Alert>
        <SearchForm onSubmit={this.onOrderSearchSubmitted} />
      </div>
    );

    let dynamicElements = <div>Search for an order using the order number</div>
    if (this.state.loaded) {
      dynamicElements = (
        <div>
          <OrderDetail order={this.state.order} />
          <LineItems gross_total={this.state.order.summary.gross_total} order_lines={this.state.order.order_lines} />
          <VatDetail summary={this.state.order.summary} />
        </div>
      );
    }

    return (
      <div className="App container">
        {staticElements}
        {dynamicElements}
      </div>
    );
  }
}

export default App;
