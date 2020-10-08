import React from 'react';
import { Table, Row, Col } from 'react-bootstrap';

function VatDetail(props) {
    const summary = props.summary ;
    return (
        <Row>
            <Col xs lg="4">
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Net</th>
                            <th>VAT @ 20%</th>
                            <th>Gross</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>£{summary.net_total}</td>
                            <td>£{summary.vat_total}</td>
                            <td>£{summary.gross_total}</td>
                        </tr>
                    </tbody>
                </Table>
            </Col>
        </Row>

    );
}

export default VatDetail;