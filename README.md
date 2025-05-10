# URL Shortner project by AMUH2020

Youtube Video demonstration: [https://youtu.be/JUjO2fZyYtA?si=vjKWU6ZmEpspyJCc](https://youtu.be/JUjO2fZyYtA?si=vjKWU6ZmEpspyJCc)

## Installation

To install the project, you will need to have python 3.8+ installed on your system, then pip install the requirements.txt file using the command below

```bash
pip install -r requirements.txt
```
To run the project, you will need to run the following commands in the project directory

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Navigate to the url and enjoy the project!


## Description

For my CS50W capstone project, I have decided to create a URL shortener, using the Django web framework. I used the qrcode and Pillow libaries to generate qrcodes for the short links. 

### Qr Code

The qr code feature took me quite some time to setup as I had to figure out the directory structure, and how the pages would be served to the user, eventually I resulted to using the static files as django (for development at least), serves the static files using the static url.

### Models

I extended Django's User model, to add a boolean field, which is for the users premium status. I decided to implement a Premium tier, as it would give a sense of depth to the project. Premium users were able to edit the pre generated short codes (the string of alphanumeric texts that designates the route to the link that is shortened) and change it to their own custom short code if they so wish to do so. I had to implement a custom user manager, with which I had a heavy reliance on the django documentation to complete

I also created a model for the short codes , the urls , using a charfields and the user who generated them using a foreign key relation. The table also has a date published field and a visits counter, to track the number of times the short url was used.

### URLS.py

Most routes are located in the url_redirect.urls.py file such as the login, logout, and register routes. The Dashboard route is also located here and it has 2 sub directories, edit, and delete that have the id (which is actually the short_link) of a url record as their url parameters.

The /r/ route, which stands for redirect, is where the magic happens, it takes the short link as a parameter, and its view does a 3xx redirect to the page linked to the short_code.

## Bootstrap v5.3

Bootstrap v5.3 was used for the styling of the project, over the course of CS50w I have grown to admire bootstrap as it makes it quite easy to quickly style a website, and it also makes it easy to make a website mobile responsive. 

## Distinctiveness and Complexity

The very concept of this project, with it being a URL shortener, is already distinctive to all the other CS50W projects. The paragraph's below will further explain why this is so, whilist also discussing the project's complexity as well.

### QR code

The QR code feature is a very distinctive feature, as it is not a feature that is found in most URL shorteners. In terms of complexity I had to use the qrcode and Pillow libraries to generate the QR code, and I had to figure out how to serve the QR code to the user. To do this I made use of the django debug=True, staticfiles app, to serve the QR code directly from the /static/ route, this was the simpler solution. In production I would have to setup, a reverse proxy to do this. I also had to figure out how to generate the QR code, and I had to figure out how to generate the QR code using the short link, as the short link is the only thing that is unique to each url record. The QR codes were generated using the short link, and were then saved in the static directory in a qrcode sub directory, with the short link as its name, ending with the .png extension. The QR codes were then served using the static url, and its file name. A feature I didn't include in the video, due to time constraints, was the ability to enlarge the qr code, by clicking on it. This was done using javascript.

### Premium Users

Another distinctive aspect of my project was the premium users feature, which allowed users to edit the short link, and change it to their own custom short link. This was done by adding a boolean field to the user model, and then creating a custom user manager, as I already mentioned before. Javascript was used, to hide the buttons, and create an input field around the short link so that it could be edited. The user could then click on the save button, to save the new short link, or click on the cancel button to cancel the edit. The edit button was only visible to premium users, and the save and cancel buttons were only visible when the edit button was clicked.

## Closing Remarks

CS50W has been an amazing experience, and I have learnt a lot throughout the course. I would like to thank Brian Yu for teaching this course, and Harvard's CS50 for providing this course for free.



