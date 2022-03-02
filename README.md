# Present
## Automating Google Meet using Python
Present was developed Selenium, Tensorflow
Present is an automatic system that join meetings on google meet and say 'present' on your place when it hear your name
you only need to provide your email, and the meeting link
Selenium is a powerful tool for controlling web browsers through programs and performing browser automation. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C#, etc, we will be working with Python.
Tensorflow is a free and open-source software library for machine learning and artificial intelligence. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks.
Web Driver will connect to your Google account automatically,open the meeting link, turn your cam and mic off and join
During meeting a speech recognition system will recognise your name, then open the mic say 'Present' and turn it off
if the teacher says your name two or more time in short period the system will open the mic play some bad noise for 3 seconds then turn it off and send in the chat room 'My internt connection is unstable' <br/>
## Perequisites <br/>
Python 3.X <br/>
install all the Seleium packages with the official [Guide from Selenium](https://selenium-python.readthedocs.io/installation.html#) <br/>
selenium 4.X <br/>
Tensorflow 2.X <br/>
ffmpeg <br/>
sounddevice <br/>
wavio <br/>
scipy <br/>
### Other <br/>
you need a pro e-mail <br/>
High quality internet <br/>
## Steps <br/>
### First Step
#### Prepare your envirement <br/>
1. Configure you envirement and install the necessary packages to automate browsing using Selenium with the official [Guide from Selenium](https://selenium-python.readthedocs.io/installation.html#) <br/>
2. Import the necessary modules such as Web Driver, Time  
3. Create an instance of Chrome browser with some required prerequisite Chrome Options().
4. Define some usefull function to use later (Google Login,...)
5. Go to Google Classroom Login page and Login using the defined function and we found buttons by their xpaths using a function in selenium named find_element_by_xpath().
6. Now switch to ggogle meet and write the meet code
7. turn off mic and cam and join the meeting
### Second Step <br/>
#### Train a custom Speech Recognition Model <br/>
we will use yamnet pre-trained model to recognise a specific name <br/>
after record the training data from mic using ffmpeg <br/>
all work done on google colab <br/>
### Third Step <br/>
#### Preprocess real time sound <br/>
with the sounddevice and wavio modules from python it's pretty easy to preprocess , record sound from device <br/>
### Fourth Step <br/>
save the Speech recognition model and import it on pycharm <br/>
