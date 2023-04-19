from file_cleaning import output_unclean_data, output_clean_file, output_final_list
from user_input import get_initial_details
from email_results import send_email

import selenium_bot as sbot

chrome_driver_path = "ENTER CHROME DRIVER PATH HERE"

instagram_parameters = get_initial_details()

#Initialize the bot object
bot_start = sbot.InstaBot(instagram_parameters["user_login"], instagram_parameters["user_pass"])
output_unclean_data(bot_start, "following")
output_unclean_data(bot_start, "followers")
followers_list = output_clean_file(followers_or_following="followers", verbs=["Remove"])
following_list = output_clean_file(followers_or_following="following", verbs=["Following", "Follow"])
output_final_list(following_list, followers_list)
send_email(instagram_parameters["receive_email"], instagram_parameters["user_login"])







