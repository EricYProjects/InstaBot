

def get_initial_details():
    # 1 - Get Instagram login credentials (to access Instagram before searching)
    # 2 - Ask for Instagram account to run following & followers report on
    print("####Enter Instagram Login Credentials####")
    user_login_input = input("Username: ")
    user_pass_input = input("Password: ")

    print("\n####Enter email to receive report####")
    receive_email = input("Receiving Email: ")

    # Store input into dictionary to return
    instagram_search_dict = {
        "user_login": user_login_input,
        "user_pass": user_pass_input,
        "receive_email": receive_email,
    }

    return instagram_search_dict