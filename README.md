<div align = "center">

<img height=200px src= "https://github.com/developer-student-club-thapar/officialWebsite/blob/master/Frontend/src/assets/dsc_logo.png">

<h1>DEVELOPER STUDENT CLUBS TIET</h1>

<a href="https://medium.com/developer-student-clubs-tiet"><img src="https://github.com/aritraroy/social-icons/blob/master/medium-icon.png?raw=true" width="60"></a>
<a href="https://twitter.com/dsctiet"><img src="https://github.com/aritraroy/social-icons/blob/master/twitter-icon.png?raw=true" width="60"></a>
<a href="https://www.linkedin.com/company/developer-student-club-thapar"><img src="https://github.com/aritraroy/social-icons/blob/master/linkedin-icon.png?raw=true" width="60"></a>
<a href="https://facebook.com/dscthapar"><img src="https://github.com/aritraroy/social-icons/blob/master/facebook-icon.png?raw=true" width="60"></a>
<a href="https://instagram.com/dsc.tiet"><img src="https://github.com/aritraroy/social-icons/blob/master/instagram-icon.png?raw=true" width="60"></a>

# Indian Number Plate Detection System

This repo contains the code for numberplate detection undertaken by DSC TIET

</div>

**Challenges with the Project** :
The number plate system in India isn't a fixed and a standard system as followed in other countries. So to make a system that could do the following with a good accuracy was a challenging task . 
Also to find a dataset that matched the task and would be good for training was a tough task .

**Approch for the problem :**
The approch used consisted of 2 major parts :
> Detecting a number plate detection system that could detect number plate from an image or a real time video and save the cropped detected part that is the image of number plate.
> OCR - to detect number from the cropped plate . 

**Techniques Used**

 **Technique 1** - With OpenCV for number plate detection and using 2 approches for OCR one with Tesseract and other with Google Cloud Vision API 
 This method gave pretty good resuts and had an advantage over a Machine Learning Based method as no training data was required for the task. 
 Google Colab was used for the task so as to install all the libraries easily. And the notebook for this approch was shared in the repo. 
 The steps involved were:
 > Instaling all libraries (pytesseract, google cloud vison etc)
 > Doing some image processing on the image to make it suitable for the detection 
 > Selecting top 30 Contours from the image ( Countours are an outline representing or bounding the shape or form of something)
 > Since a number plate would be a perfect 4 side contour , we selected that contour . 
 > So now our number plate is recognised . We need to recognise number from it .
 > 2 approches for OCR was tested and used . Their results have been shown in Colab Notebook . Google OCR is almost 95% accurate and gives perfect results.
 
 **Technique 2** - A machine Learning based approch using YOLO V3 model . 
 The major challenge was to find a relevant dataset which could be used with the above model. The input for the above model was the images of cars and output was the       coordinates of the number plate and once the number plate is detected , A similar OCR technique was to be used for number plate recognition. 
 Since the dataset was very limited , we tried to scrape images of Indian cars and labell it and create our own dataset .
 Tool being Used for Labelling the Images was LabelImg . (https://tzutalin.github.io/labelImg/)
 
 A total of 519 images were scrapped.The Link to the Scrapped Images :
 https://drive.google.com/drive/folders/1JZfurTi9r7M-ClMYXjLZ2S6MiWhWoe84
 
 Current we are in the phase of labelling the images and creating our very own dataset. 
 
 **Objectives**
To make a end to end perfect system (with a Good UI) where images and videos can be directly uploaded and number on the number plate for every car in image would be the output for both the approches . 
Also to make a system for the real time live feed would be the ultimate motive . 
