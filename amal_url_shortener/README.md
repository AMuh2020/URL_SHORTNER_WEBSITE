# URL Shortner project by AMUH2020

## Description

For my CS50W capstone project, I have decided to create a URL shortener, using the Django web framework. I used the qrcode and Pillow libaries to generate qrcodes for the short links. 

### Qr Code
The qr code feature took me quite some time to setup as I had to figure out the directory structure, and how the pages would be served to the user, eventually I resulted to using the static files as django (for development at least), serves the static files using the static url.

### Models

I extended Django's User model, to add a boolean field, which is for the users premium status. I decided to implement a Premium tier, as it would give a sense of depth to the project. Premium users were able to edit the pre generated short codes (the string of alphanumeric texts that designates the route to the link that is shortened) and change it to their own custom short code if they so wish to do so. I had to implement a custom user manager, with which I had a heavy reliance on the django documentation to complete

I also created a model for the short codes , the urls , using a charfields and the user who generated them using a foreign key relation. The table also has a date published field and a visits counter, to track the number of times the short url was used.

### URLS.py


## Distinctiveness and Complexity