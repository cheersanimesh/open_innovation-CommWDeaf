# Project CommWDeaf
## Team TechBusters

### Impact

 **Over a  billion people in this people belong to the Deaf Community**..**Over 70 million people** in this community use Sign Language as a medium of communication.. Each Country may have one or sometimes two or more sign languages.. 

 *A sign language* is a language which uses manual communication and body language to convey meaning, as opposed to acoutically conveyed sound patterns.. This can involve simultaneously combining hand shapes,orientation and movement of the hands, arms or body, and facial expressions to fluidly expresses a speaker's thoughts..

 Development of any language including sign language, requires ongoing interaction between the speakers of that language.. Deaf people in rural areas have little or no oppurtunity, to meet other deaf people.. What is commonly observed that it appears to be literally the gestures used by hearing people to communicate with the deaf.. 

 The knowledge of sign language is limited and therefore it becomes a huge problem for these people.. 

 Deaf and Dumb people find it very difficult to communicate with people who have little or no knowledge about sign language. This widens the gap between these specially gifted people and others.. These specially gifted people are not able to express their ideas, feelings, emotions to the world and thus this becomes a huge problem for them.. These people find it very depressing to be not understood by the outside world.. As these people might have some brilliant ideas or talents which we are not able to see just because of this communication barrier.. Their ideas might never reach us which sounds very dissapointing..

 **Our project addresses this predicament of these people in our society..**

 **We propose to build a Web Application to enable a two way communication between  deaf or dumb community and a normal human being.. We use the power of Artificial Intelligence, Machine Learning and various other technical stacks to develop a full fledged application to address this challenge..**

 *We also address the problem of localised sign languages by providing flexibity to the dictionary of our sign languages..*

 We propose to capture the gestures through a camera and translate it to text and further to speech using cognitive solutions.. Further we record the voice of a normal person and translate it to text, which would enable the deaf person to **listen to a normal person** .. *Thus we establish a two way communication between the deaf and the normal person*..

 We deploy this application on a Web browser

 Our Application being a WEB application would be freely accesible to all people in this community, thus providing accesibility to the under-priviliged ..

 
### Implementation

**Frontend**:It is used  to provide realtime communication between the server and the client. It records the video from the webcam and posts it to the middleware server using formdata which in turn sends the video to the cnn model for prediction.It also enables text to speech and speech to text for the convienence of the deaf and dumb community.It accomplishes user friendly design and rich user interface.

**Technologies used**:**React.js**:
It helps to build rich user interfaces and allows writing custom components.It offers fast rendering and is SEO-friendly thus it is more likely to rank higher on  Google Search Engine Result Page.**Recordrtc**:Used to record WebRTC video media streams.It is very useful as it supports cross-browser video recording.**Speak-tts**:Used for speech to text implementation.

<br/>

 **Middleware Server** :
 The middleware server (i.e. server.js) is a relay between frontend and the machine learning model hosted on flask.When it encounters a post request it takes the video from the frontend and extract frames from it, so that it can be fed into the machine learning model.

 This is implemented using **Node.js** because it uses non-blocking, event-driven I/O to remain lightweight and efficient in the face of data-intensive real-time applications that run across distributed devices.

 Some libraries used are **Express.js** for server operation and **FFmpeg** for frame extraction.

<br/>

**Machine Learning Module**
Images have been accepted and preprocessed and then passed into a Neural Network for classification. Due to a large training data a very Deep Neural Network has been trained to reduce bias as well as variance of the classifier..

The training image data contained of self generated image data containing of 55500 images of 37 different labels..

The Neural Network Architecture implemented is similar to a **VGG 16** architecture.. Such a network has been chosen after a lot of test and trials.. A Deep network was preffered owing to the vast amount of variations in the Image Data..

The Neural Network has been implemented through **Keras** with **Tensorflow** serving as the backend.. It took about 2 hours to train the Neural Network on **Google Colab Servers** with *GPU as the hardware accelarator*.. 

In order to deploy into a web Application the predicting module has been hosted on a **Flask Server**, in order to make the module communicate with the FrontEnd.. Flask being a lightweight web framework was easily deployable..










