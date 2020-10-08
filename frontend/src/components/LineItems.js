import React from 'react';
import { Table } from 'react-bootstrap';
import LineItem from './LineItem'

function LineItems(props) {
    const lineItems = props.order_lines || [];
    const orderGrossTotal = props.gross_total;
    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>Item</th>
                    <th>Price</th>
                    <th>Quatity</th>
                    <th>Total</th>
                </tr>
            </thead>
            <tbody>
                {lineItems.map(lineItem =>
                    <LineItem key={lineItem.id} line_item={lineItem} />
                )}
            </tbody>
            <tfoot>
                <tr>
                    <td>Total</td>
                    <td></td>
                    <td></td>
                    <td>£{orderGrossTotal}</td>
                </tr>
            </tfoot>
        </Table>
    );
}

export default LineItems;