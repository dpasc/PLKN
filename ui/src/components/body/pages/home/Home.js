import React, { Fragment } from 'react'
import "./Home.css"
import {Row,Col} from 'reactstrap'
import ResultTable from './ResultTable'
import SearchPanel from './SearchPanel'



function Home()
{
    return(
        <Fragment>
            <Row>
                <Col>
                    <h3 className="page_title">Product Development Schedules</h3>
                </Col>                
            </Row>
            <SearchPanel/>
            <ResultTable/>
        </Fragment>
    )

}





export default Home;