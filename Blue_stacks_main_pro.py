import Blue_stacks_console_class as console_class

if __name__ == "__main__":
    print("--------------Hello Welcome to the RBAC System--------------\n")

    #creating a for for console control
    console_hand_obj=console_class.console_handling()
    #create all default users and roles
    console_hand_obj.create_all_default()
    user_obj = console_hand_obj.user_logging()
