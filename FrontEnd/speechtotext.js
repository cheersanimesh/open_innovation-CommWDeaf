import React, {Component } from 'react'
import SpeechRecognition from 'react-speech-recognition';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container,Button,Row,Col} from 'react-bootstrap';
const options={
  autoStart:false,
}
class Dictaphone extends Component {
  render() {
    const { transcript, startListening,stopListening, browserSupportsSpeechRecognition } = this.props
    if (!browserSupportsSpeechRecognition) {
      return null
    }
    return (
      <div style={{margin:"0px 500px"}} >
        <Container>
        <Row>
        <Col sm={4.5}><textarea value={transcript} style={{fontSize:"30px",width:"400px" ,height:"400px"}} ></textarea> </Col>
        <Col><Button onClick={startListening} variant="primary" style={{marginTop:"150px" ,padding:"20px"}}>Start</Button>{'  '}
        <Button onClick={stopListening} variant="warning" style={{marginTop:"150px" ,padding:"20px"}}>Stop</Button></Col>       
        </Row>
        
        </Container>
      </div>
    )
  }
}

export default SpeechRecognition(options)(Dictaphone)