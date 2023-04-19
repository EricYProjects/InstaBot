
# InstaBot

Python web scraper which returns an emailed list of Instagram usernames that exist in a user's 'Following' list but do not exist in the user's 'Followers' list


## Required Downloads:

* Locally downloaded ChromeDriver


```bash
  https://chromedriver.chromium.org/downloads
```
    
## Initial File Setup Requirements:

#### main.py ####
```
Line 7 - Set chrome_driver_path variable to the ChromeDriver path on your computer

```

#### email_results.py ####
```
To enable sending of final results via email, edit the corresponding variables 
(you may need to generate/enable an app password in your email)

Line 9 - Set sending_email variable to the email you want to send from
Line 10 - Set sending_password to your email’s app password 
Line 30 - Set the SMTP parameter to your email’s SMTP server

```


## Usage Tips

#### Login Credentials

* Utilize your Instagram username (not phone number or email)

#### Run Time

* Run time is dependent on the number of followers/following (print statements occur in the terminal to indicate the program’s actions)


## Demo

1 - User input is gathered in terminal

![App Screenshot](https://raw.githubusercontent.com/EricYProjects/InstaBot/main/InstaBot-demo-images/Screen%20Shot%202023-04-18%20at%2011.56.31%20PM.png)


2 - Bot opens browser & passes credentials into Instagram web form & logs in

![App Screenshot](https://raw.githubusercontent.com/EricYProjects/InstaBot/main/InstaBot-demo-images/Screen%20Shot%202023-04-18%20at%2011.56.58%20PM.png)

3 - Bot redirects to profile page, scrolls through pop up box to gather data/usernames

![App Screenshot](https://raw.githubusercontent.com/EricYProjects/InstaBot/main/InstaBot-demo-images/Screen%20Shot%202023-04-19%20at%2012.12.18%20AM.png)

4 - Data is output to files, cleaned & compared

![App Screenshot](https://raw.githubusercontent.com/EricYProjects/InstaBot/main/InstaBot-demo-images/Screen%20Shot%202023-04-18%20at%2011.58.17%20PM.png)

5 - Final list is sent to specified email

![App Screenshot](https://raw.githubusercontent.com/EricYProjects/InstaBot/main/InstaBot-demo-images/Screen%20Shot%202023-04-18%20at%2011.58.55%20PM.png)
