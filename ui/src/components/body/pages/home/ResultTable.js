import React from 'react'
import {Row,Col} from 'reactstrap'
import {Table} from 'reactstrap'


function ResultTable(){

return (
    <Row>
        <Col md={{size:'auto',offset:4}}>
    <Table
    hover={true}
    responsive
    >
        <thead>
            <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
            </tr>
            <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
            </tr>
            <tr>
                <th scope="row">3</th>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
            </tr>
        </tbody>
     </Table>
     </Col>
    </Row>


    );
}


export default ResultTable;