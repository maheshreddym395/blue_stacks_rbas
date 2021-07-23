import Blue_stacks_role_class as role_class

# Class which maintains the users and related functions
class Users(role_class.Roles):
    def __init__(self, name, passw):
        self.username = name
        self.password = passw

    def add_admin_user(self):
        self.users[self.username] = self
        self.users_roles[self.username] = self.roles["Admin"].rolename

    def login(self):
        username = input("Please Enter the User Name")

        try:
            user_temp = self.users[username]
        except KeyError:
            print("The user name Entered Does not exist\n")
            return False
        except Exception as e:
            print(e)
            raise

        password = input("Please Enter the Password")
        try:
            if user_temp.password == password:
                print("Logged in Succesfully\n")
                return user_temp
            else:
                print("The Password Entered is Wrong\n")
                return False
        except Exception as e:
            print(e)
            raise

    def add_user(self):
        username = input("Please Enter the User Name")
        if self.users.get(username, -1) != -1:
            print("User already existed\n")
            return False
        password = input("Please Enter the Password")
        print("Please Confirm to add user with username={}, password={} , yes/no".format(username, password))
        yes_or_no = input()
        if yes_or_no == "yes":
            temp = Users(username, password)
            # Adding the User_details object to the users
            self.users[username] = temp

            #Adding a user under Basic_user later admin can change the role of the user
            self.users_roles[username] = self.roles["Basic_user"].rolename
            if  self.username!="Dummy" and self.users_roles[self.username]=="Admin":
                print("User {} Created Succefully ".format(username))
                return False
            else:
                print("User Created Succefully and logged into the user {}".format(username))
                return temp
        elif yes_or_no == "no":
            return False
        else:
            print("Please Enter yes or no\n")
            return False

    def del_user(self):
        if self.users_roles[self.username]=="Admin":
            username = input("Please Enter the User Name")
            action_username = self.users.get(username, -1)
            if action_username == -1:
                print("User doesnt exist\n")
                return False
            if action_username.username == "Admin":
                print("Admin Cannot be removed\n")
                return False
            print("Please Confirm to del user with username={}, yes/no".format(username))
            yes_or_no = input()
            if yes_or_no == "yes":
                #delete the user from users dict
                del self.users[username]
                # delete the user from users_role dict
                del self.users_roles[username]
                print("Deleted username {} Succefully".format(username))
                return False
            elif yes_or_no == "no":
                return False
            else:
                print("Please Enter yes or no\n")
                return False

    def update_user_role(self):
        if self.users_roles[self.username] == "Admin":
            username = input("Please Enter the User Name")
            action_username = self.users.get(username, -1)
            if action_username == -1:
                print("User doesnt exist\n")
                return False
            if action_username.username == "Admin":
                print("Admin's role Cannot be changed\n")
                return False
            print("The role of the {} is {}".format(username, self.users_roles[username]))
            print("\nThe Available roles are:")
            for roles_ele,roles_obj in self.roles.items():
                print("{}, Permission=[Read:{}, Write:{}, Append:{}]".format(roles_ele, roles_obj.access_permission_obj.Read, roles_obj.access_permission_obj.Write, roles_obj.access_permission_obj.Append))
            print("\nPlease Type the above available Roles")
            rolename=input()
            if self.roles.get(rolename,-1)!=-1:
                print("Please Confirm to Add role {} to user {}, yes/no".format(rolename,username))
                yes_or_no = input()
                if yes_or_no == "yes":
                    #update the users_role data
                    self.users_roles[username]=rolename
                    return False
                elif yes_or_no == "no":
                    return False
                else:
                    print("Please Enter yes or no\n")
                    return False
            else:
                print("The rolename {} entered doesnt exists".format(rolename))
                return False

    def display_users(self):
        if self.users_roles[self.username] == "Admin":
            print("\nUsers available are :")
            for users_ele,users_obj in self.users.items():
                print("{}, Password={}".format(users_ele,users_obj.password))
