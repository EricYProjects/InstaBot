### Functions for main.py to call related to output files###

# Stores raw data from Instagram elements found in the scroll box into a file either named following.txt or followers.txt
# "bot" input is the object from main.py
# "option" is either "following" or "followers"
def output_unclean_data(bot, option):
    attribute_name = option
    attribute_value = getattr(bot, attribute_name, None)

    if attribute_value is not None:
        with open(file=f"{option}.txt", mode="w") as file:
            for item in attribute_value:
                file.write(item)


# 1 - Opens raw data file (created by function output_unclean_data) and goes through each line in for loop
# 2 - The Instagram raw data currently has structure:
#       Followers data - Ex: For each user there is a line that has structure Remove{username}
#       Following data - Ex: For each user there is a line that has structure Following{username}
# 3 - In the for loop, using an if statement, check to see if structure exists in the line
#       If it does:
#           - split the string using either verb (Ex: 'Remove', 'Following')
#           - get the value at -1 position in the string list (which is the username)
# 4 - Add the cleaned username to list
# 5 - Write to file & return the list
def output_clean_file(followers_or_following, verbs):
    username_list = []

    #1
    with open(file=f"{followers_or_following}.txt") as file:
        for line in file:
            #3
            for verb in verbs:
                if verb in line and line.split(verb)[-1] not in username_list:
                    #4
                    if verb == "Follow" and line.split(verb)[-1].startswith("ing"):
                        pass
                    else:
                        username_list.append(line.split(verb)[-1])
        with open(file=f"{followers_or_following}_clean.txt", mode="w") as file2:
            for item in username_list:
                file2.write(item)
    return username_list

# 1 - If username is in following (list1) and not in followers (list2), add to list
# 2 - Write to file
def output_final_list(list1, list2):
    follower_not_following_back = [x for x in list1 if x not in list2]
    with open(file="final_list.txt", mode="w") as file:
        for item in follower_not_following_back:
            file.write(item)
