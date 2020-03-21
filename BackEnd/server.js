const express =require("express");
const app =express();

const extractFrames = require('ffmpeg-extract-frames')
const fs = require('fs');
const path = require('path');
const axios= require("axios");
const ffmpegPath = require('@ffmpeg-installer/ffmpeg').path;
const ffmpeg = require('fluent-ffmpeg');
ffmpeg.setFfmpegPath(ffmpegPath)
var n=1;
const serverUrl='http://0.0.0.0:5000/';
const http = axios.create({
      baseURL:serverUrl,
});
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
	
	http.post('/POST',{ //my server path
        string:'num1', //irrelevant 
	})
	
})

app.listen(4000,function(){
    console.log("server on 4000");
});

