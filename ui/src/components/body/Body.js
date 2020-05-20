import './Body.css';
import React,{useState} from 'react'
import {Nav,NavItem,NavLink} from 'reactstrap';
import {TabContent, TabPane,Col,Row,} from 'reactstrap'
import classnames from 'classnames';
import Home from './pages/home/Home'


function Body(){
    const [activeTab, setActiveTab] = useState('1')

    const toggle = tab => {
        if(activeTab !== tab) setActiveTab(tab)
    }

    return(
        <div className="body">
            <Nav tabs justified={true}> 
                <NavItem>
                    <NavLink
                            className={classnames({ active: activeTab === '1' })}
                            onClick={() => { toggle('1'); }}
                    >
                        Home
                    </NavLink>
                </NavItem>
                <NavItem>
                    <NavLink
                                className={classnames({ active: activeTab === '2' })}

                                onClick={() => { toggle('2'); }}
                    >
                        API
                    </NavLink>
                </NavItem>
                <NavItem>
                    <NavLink
                                className={classnames({ active: activeTab === '3' })}
                                onClick={() => { toggle('3'); }}
                    >
                        Coming Soon
                    </NavLink>
                </NavItem>
                <NavItem>
                    <NavLink
                                className={classnames({ active: activeTab === '4' })}
                                onClick={() => { toggle('4'); }}
                    >
                       About
                    </NavLink>
                </NavItem>
                <NavItem>
                    <NavLink
                                className={classnames({ active: activeTab === '5' })}
                                onClick={() => { toggle('5'); }}
                    >
                         Contact
                    </NavLink>
                </NavItem>
            </Nav>
            <TabContent activeTab={activeTab}>
        <TabPane tabId="1">
          <Row>
            <Col sm="12">
              <Home/>
            </Col>
          </Row>
        </TabPane>
        <TabPane tabId="2">
          <Row>
            <Col sm="12">
              <h4>API</h4>
            </Col>
          </Row>
        </TabPane>
        <TabPane tabId="3">
          <Row>
            <Col sm="12">
              <h4>Coming Soon</h4>
            </Col>
          </Row>
        </TabPane>
        <TabPane tabId="4">
          <Row>
            <Col sm="12">
              <h4>About</h4>
            </Col>
          </Row>
        </TabPane>
        <TabPane tabId="5">
          <Row>
            <Col sm="12">
              <h4>Contact</h4>
            </Col>
          </Row>
        </TabPane>
      </TabContent>
        </div>
    )
}

export default Body;