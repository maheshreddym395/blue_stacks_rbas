import Blue_stacks_user_class as user_class
import Blue_stacks_role_class as role_class
import Blue_stacks_access_modes_class as access_modes_class
import Blue_stacks_resources_class as resource_class
import sys

#class handling the console functions
class console_handling():
    def __init__(self):
        pass

    def create_all_default(self):

        # Created a Default Admin Role
        admin_role_access = access_modes_class.Access_Modes(True, True, True)
        roles_obj = role_class.Roles("Admin", admin_role_access)
        roles_obj.add_default_roles()

        # Created a Default Basic_user Role
        bu_role_access = access_modes_class.Access_Modes(True, False, False)
        roles_obj = role_class.Roles("Basic_user", bu_role_access)
        roles_obj.add_default_roles()

        # Created a Default Admin User
        users_obj = user_class.Users("Admin", "Admin")
        users_obj.add_admin_user()

        #create default resources
        basic_resources = resource_class.Resources("code1")
        users_obj.resources[basic_resources.resource_name]=basic_resources
        basic_resources = resource_class.Resources("code2")
        users_obj.resources[basic_resources.resource_name]=basic_resources

    #Function which gives options to the user
    def options_to_user_logging(self):
        print("1. Login to an Existing User")
        print("2. Add a User")
        print("3. Exit the Console")

        try:
            inp_option=int(input())
        except ValueError:
            print("Please provide correct Input\n")
            self.options_to_user(users_obj)
            return False
        except Exception as e:
            print(e)
            raise

        #temp user obj to call fucntions of the Users to create or login
        temp_user_obj=user_class.Users("Dummy","Dummy")
        options={
            1:temp_user_obj.login,
            2:temp_user_obj.add_user,
            3:sys.exit,
        }
        try:
            return options[inp_option]()
        except KeyError:
            print("Please provide correct Input\n")
            self.options_to_user(users_obj)
            return False
        except Exception as e:
            print(e)
            raise

    #All services related to users
    def user_based_services(self,loged_user_obj):
        if loged_user_obj.users_roles[loged_user_obj.username] == "Admin":
            print("\n ---------Logged into user {} in user_based_services--------- ".format(loged_user_obj.username))
            print("1. Add a User")
            print("2. Delete a User")
            print("3. Display Users Available")
            print("4. Go Back to Admin Console")
            print("5. Exit the Console")

            try:
                inp_option = int(input())
            except ValueError:
                print("Please provide correct Input\n")
                self.user_based_services(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise

            options = {
                1:loged_user_obj.add_user,
                2:loged_user_obj.del_user,
                3:loged_user_obj.display_users,
                4: self.admin_console,
                5: sys.exit,
            }
            try:
                if inp_option==4:
                    return options[inp_option](loged_user_obj)
                else:
                    return options[inp_option]()
            except KeyError:
                print("Please provide correct Input\n")
                self.user_based_services(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise
        else:
            self.options_to_user_logging

    #All Services related to the Roles
    def role_based_services(self,loged_user_obj):
        if loged_user_obj.users_roles[loged_user_obj.username] == "Admin":
            print("\n ---------Logged into user {} in role_based_services--------- ".format(loged_user_obj.username))
            print("1. Add a Role")
            print("2. Delete a Role")
            print("3. Update Role of a User")
            print("4. Display Roles Available")
            print("5. Go Back to Admin Console")
            print("6. Exit the Console")

            try:
                inp_option=int(input())
            except ValueError:
                print("Please provide correct Input\n")
                self.role_based_services(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise

            options={
                1:loged_user_obj.add_role,
                2:loged_user_obj.del_role,
                3:loged_user_obj.update_user_role,
                4:loged_user_obj.display_roles,
                5:self.admin_console,
                6:sys.exit,
            }
            try:
                if inp_option in [5]:
                    return options[inp_option](loged_user_obj)
                else:
                    return options[inp_option]()
            except KeyError:
                print("Please provide correct Input\n")
                self.role_based_services(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise
        else:
            self.options_to_user_logging

    # All Services related to the Resources
    def resources_based_services(self, loged_user_obj):
            print("\n ---------Logged into user {} in resources_based_services--------- ".format(loged_user_obj.username))
            print("1. Add a Resource")
            print("2. Delete a Resource")
            print("3. Read a Resource")
            print("4. Write a Resource")
            print("5. Append a Resource")
            print("6. Display Resources Available")
            if loged_user_obj.users_roles[loged_user_obj.username] == "Admin":
                print("7. Go Back to Admin Console")
            else:
                print("7. Go Back to User Console")
            print("8. Exit the Console")

            try:
                inp_option = int(input())
            except ValueError:
                print("Please provide correct Input\n")
                self.resources_based_services(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise

            options = {
                1: loged_user_obj.add_resources,
                2: loged_user_obj.del_resources,
                3: loged_user_obj.read_resources,
                4: loged_user_obj.write_resources,
                5: loged_user_obj.append_resources,
                6: loged_user_obj.display_resources,
                7: self.other_console,
                8: sys.exit,
            }
            if loged_user_obj.users_roles[loged_user_obj.username] == "Admin":
                options[7]=self.admin_console
            try:
                if inp_option in [7]:
                    return options[inp_option](loged_user_obj)
                else:
                    return options[inp_option]()
            except KeyError:
                print("Please provide correct Input\n")
                self.resources_based_services(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise

    #Function which gives options to the Admin User
    def options_to_Adminuser(self, loged_user_obj):
        if loged_user_obj.users_roles[loged_user_obj.username] == "Admin":
            print("\n ---------Logged into user {}--------- ".format(loged_user_obj.username))
            print("1. Role Based Services")
            print("2. User Based Services")
            print("3. Resource Based Services")
            print("4. Go back to Logging Console")
            print("5. Exit the Console")

            try:
                inp_option=int(input())
            except ValueError:
                print("Please provide correct Input\n")
                self.options_to_Adminuser(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise

            options={
                1:self.role_based_services_console,
                2:self.user_based_services_console,
                3:self.resources_based_services_console,
                4:self.user_logging,
                5:sys.exit,
            }
            try:
                if inp_option in [1, 2, 3]:
                    return options[inp_option](loged_user_obj)
                else:
                    return options[inp_option]()
            except KeyError:
                print("Please provide correct Input\n")
                self.options_to_Adminuser(loged_user_obj)
                return False
            except Exception as e:
                print(e)
                raise
        else:
            self.options_to_user_logging

    # Function which gives options to the Other User
    def options_to_otherusers(self, loged_user_obj):
        print("\n ---------Logged into user {}--------- ".format(loged_user_obj.username))
        print("1. Resource Based Services")
        print("2. Go back to Logging Console")
        print("3. Exit the Console")

        try:
            inp_option = int(input())
        except ValueError:
            print("Please provide correct Input\n")
            self.options_to_otherusers(loged_user_obj)
            return False
        except Exception as e:
            print(e)
            raise

        options = {
            1: self.resources_based_services_console,
            2: self.user_logging,
            3: sys.exit,
        }
        try:
            if inp_option in [1]:
                return options[inp_option](loged_user_obj)
            else:
                return options[inp_option]()
        except KeyError:
            print("Please provide correct Input\n")
            self.options_to_otherusers(loged_user_obj)
            return False
        except Exception as e:
            print(e)
            raise

    # Function to Run in the Role Based services console
    def role_based_services_console(self,user_detail_obj):
        while (1):
            self.role_based_services(user_detail_obj)

    # Function to Run in the User Based services console
    def user_based_services_console(self,user_detail_obj):
        while (1):
            self.user_based_services(user_detail_obj)

    # Function to Run in the Resources Based services console
    def resources_based_services_console(self,user_detail_obj):
        while (1):
            self.resources_based_services(user_detail_obj)

    # Function to Run in the Admin console
    def admin_console(self,user_detail_obj):
        while (1):
            self.options_to_Adminuser(user_detail_obj)

    # Function to Run in the Admin console
    def other_console(self,user_detail_obj):
        while (1):
            self.options_to_otherusers(user_detail_obj)

    #Function to Run the userloggin console
    def user_logging(self):
        # infinate loop until users logs in or creates a user
        while (1):
            # Logged in or created a new user will be stored here in the obj
            user_detail_obj = self.options_to_user_logging()
            if user_detail_obj:
                if user_detail_obj.users_roles[user_detail_obj.username] == "Admin":
                    self.admin_console(user_detail_obj)
                else:
                    self.other_console(user_detail_obj)