import React,{Component} from 'react';
import RecordRTC from 'recordrtc';
import axios from './axios-video'
import classes from './App.module.css';
import Webcam from "react-webcam";
import Speech from 'speak-tts';
import PostData from './prediction.json'
import 'bootstrap/dist/css/bootstrap.min.css';
import  {Button, Row,Container,Col}  from 'react-bootstrap';
import SpeechRecognition from "./speechtotext";
class CameraRecorder extends Component {
    state = { recordVideo: null, 
              text1:" "};

  stopRecord=()=> {
    this.state.recordVideo.stopRecording(() => {
      this.state.recordVideo.save("blobby.webm");
      var fd = new FormData();
      fd.append('upl',this.state.recordVideo.getBlob(), 'blobby.webm');
      console.log(this.state.recordVideo.getBlob());
      axios.post('/',fd).then(res=>{ })

    });
  }
  startRecord=()=> {
    this.getUserMedia(stream => {
      this.state.recordVideo = RecordRTC(stream, { type: 'video',});
      
      this.state.recordVideo.startRecording();
    });
  }
  textSpeech=()=>{
    const speech = new Speech();
    console.log(this.state.text1)
    speech.speak({
      text: this.state.text1,
  }).then(() => {
      console.log("Success !")
  }).catch(e => {
      console.error("An error occurred :", e)
  });
  }
  getUserMedia=(callback)=> {
    navigator.getUserMedia({ audio: false, video: true }, callback, error => alert(JSON.stringify(error)));
  }
componentDidMount=()=>
{
  PostData.map((postDetail,index)=>{
    this.setState({text1:postDetail.content})
  })}
  render() {
    
    return (
      <div >
        
        <meta name="viewport" content="width=device-width, initial-scale=1"></meta>
<script src="./xyz.js" ></script>
        <Container>
          <Row>
         <Webcam height="auto" width="auto" margin="auto"/>{"   "}
         <textarea value={this.state.text1} style={{fontSize:"30px"}} ></textarea>
         </Row><h1></h1>
         <Row>
         <Col><Button onClick={this.startRecord} variant="primary">Start Record</Button></Col>
         <Col><Button onClick={this.stopRecord} variant="success">Stop Record</Button></Col>
         <Col><Button onClick={this.textSpeech} variant="warning">text to speech</Button></Col>
         </Row><h1></h1>
         </Container>
           <div ><SpeechRecognition></SpeechRecognition></div>
        </div>
    )
  }
}

export default CameraRecorder;


