import React from 'react';
import { Card } from 'react-bootstrap';

function OrderDetail(props) {
  const order = props.order;
  return (
    <Card className="mb-4 mt-3" style={{ width: '21rem' }}>
      <Card.Body>
        <Card.Text>Order: {order.id}</Card.Text>
        <Card.Text>Customer: {order.customer_name}</Card.Text>
        <Card.Text>Date: {order.created_at}</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default OrderDetail;