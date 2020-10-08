import React from 'react';

function LineItem(props) {
    const lineItem = props.line_item;
    return (
        <tr>
            <td>{lineItem.item.name}</td>
            <td>£{lineItem.price}</td>
            <td>{lineItem.quantity}</td>
            <td>£{lineItem.line_total}</td>
        </tr>
    );
}

export default LineItem;