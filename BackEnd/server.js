const express =require("express");
const app =express();
const extractFrames = require('ffmpeg-extract-frames')
const fs = require('fs');
const path = require('path');
const axios= require("axios");

var n=1;
function frame_out() {
    extractFrames({
		input: 'blobby ('+n+').webm',
		output: './frames/frames-%i.jpg',
		offsets: [
		  1000,
		  2000,
		  3000,
		  4000,
		  5000,
		  6000,
		  7000,
		  8000,
		  9000,
		  10000,
		]
	  })
	n++;
	axios.post('http://0.0.0.0:5000/post',{
        string:"num1",
    })
}
app.post("/", function(req,res){
	const directory = './frames';

fs.readdir(directory, (err, files) => {
  if (err) throw err;

  for (const file of files) {
    fs.unlink(path.join(directory, file), err => {
      if (err) throw err;
    });
  }
});
setTimeout(frame_out,3000);

	
	
})
app.listen(4000,function(){
    console.log("server on 4000");
});

