import React from 'react'
import './SearchPanel.css'
import {Row,Col} from 'reactstrap'
import {Form,FormGroup} from 'reactstrap'
import {InputGroup,InputGroupAddon,InputGroupText,Input,Label} from 'reactstrap'





function SearchPanel()
{
    return (
        <div id='main'>
            <Label>
                Vendors
            </Label>
            <Form>
                <FormGroup row>
                    <Col sm={{size:12,offset:5}}>
                        <InputGroup>
                            <InputGroupAddon addonType="prepend">
                                    <InputGroupText>
                                        <Input addon type="checkbox" aria-label="Checkbox for following text input" />
                                    </InputGroupText>
                                </InputGroupAddon>
                            <InputGroupText>Woolworths</InputGroupText>
                        </InputGroup>
                    </Col>
                    <Col sm={{size:'auto',offset:5}}>
                        <InputGroup>
                            <InputGroupAddon addonType="prepend">
                                    <InputGroupText>
                                        <Input addon type="checkbox" aria-label="Checkbox for following text input" />
                                    </InputGroupText>
                                </InputGroupAddon>
                            <InputGroupText>Woolworths</InputGroupText>
                        </InputGroup>
                    </Col>
                </FormGroup>
            </Form>
        </div>
    );


}


export default SearchPanel;