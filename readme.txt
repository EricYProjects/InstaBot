README

This project is intended for use on personal accounts with < 1000 followers or following

INITIAL SETUP REQUIREMENTS:
* Locally downloaded ChromeDriver

INITIAL FILE CONFIGURATION REQUIREMENTS:
[main.py]
Line 7 - Set chrome_driver_path variable to the ChromeDriver path on your computer

[email_results.py]
To enable sending of final results via email, edit the corresponding variables (you may need to generate/enable an app password in your email) 
Line 9 - Set sending_email variable to the email you want to send from
Line 10 - Set sending_password to your email’s app password 
Line 30 - Set the SMTP parameter to your email’s SMTP server

———

USAGE TIPS (As of 04/17/2023):

[Login Credentials]
Utilize your Instagram username (not phone number or email)

[Run Time]
Run time is dependent on the number of followers/following (print statements occur in the terminal to indicate the program’s actions)