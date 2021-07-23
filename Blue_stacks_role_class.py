import Blue_stacks_access_modes_class as access_modes_class
import Blue_stacks_database_class as database_class
import Blue_stacks_resources_class as resource_class

# Class which maintains the Roles and related functions
class Roles(database_class.Database, access_modes_class.Access_Modes, resource_class.Resources):

    def __init__(self, name, access_modes_obj):
        self.rolename = name
        self.access_permission_obj=access_modes_obj

    #function to add a admin role
    def add_default_roles(self):
        self.roles[self.rolename] = self

    def add_role(self):
        #Only users having Admin role can add a role
        if self.users_roles[self.username]=="Admin":
            rolename = input("Please Enter the Role Name")
            if self.roles.get(rolename, -1) != -1:
                print("Role already existed\n")
                return False
            print("Please enter the permissions in order of Read,Write,Append")
            print("Ex: Only Read Input --> 1,0,0")
            modes_access=input()
            b = modes_access.split(",")

            #check the inputs:
            if len(b)==3:
                for ele in b:
                    if ele not in ['1', '0']:
                        print("Numbers entered are not 0's and 1's")
                        return False
                acess_temp=access_modes_class.Access_Modes(int(b[0]), int(b[1]), int(b[2]))
            else:
                print("Please Enter the Input in the format of 1,1,1")
                return False

            print("Please Confirm to add role with rolename={}, acessmodes={} , yes/no".format(rolename, b))
            yes_or_no = input()
            if yes_or_no == "yes":
                temp = Roles(rolename, acess_temp)
                # Adding the roles object to the roles table
                self.roles[rolename]=temp
                print("Role {} Created Succefully".format(rolename))
                return False
            elif yes_or_no == "no":
                return False
            else:
                print("Please Enter yes or no\n")
                return False

    def del_role(self):
        #Only users having Admin role can del a role
        if self.users_roles[self.username]=="Admin":
            print("Available Roles are:")
            for roles_ele,roles_obj in self.roles.items():
                print("{}, Permission=[Read:{}, Write:{}, Append:{}]".format(roles_ele, roles_obj.access_permission_obj.Read, roles_obj.access_permission_obj.Write, roles_obj.access_permission_obj.Append))
            rolename = input("\nPlease Enter the Role Name")
            action_rolename = self.roles.get(rolename, -1)
            if action_rolename == -1:
                print("Role doesnt exist\n")
                return False
            if action_rolename.rolename in ["Admin", "Basic_user"]:
                print("\n{} Cannot be removed".format(rolename))
                return False

            #Display th user effected by the deletion of the role
            users_changed=[]
            for key_user,val_role in self.users_roles.items():
                if val_role==rolename:
                    users_changed.append(key_user)
            print("\nDeleting Role {}  changes users {} role to Basic_user".format(rolename,users_changed))

            print("\nPlease Confirm to del Role = {}, yes/no".format(rolename))
            yes_or_no = input()
            if yes_or_no == "yes":
                #del from roles data
                del self.roles[rolename]
                #del the users havng this role in users_role data and update them to basic user
                users_changed=[]
                for key_user,val_role in self.users_roles.items():
                    if val_role==rolename:
                        users_changed.append(key_user)
                        self.users_roles[key_user]="Basic_user"
                print("\nDeleted Role {} Succefully and changed users {} role to Basic_user".format(rolename,users_changed))
                return False
            elif yes_or_no == "no":
                return False
            else:
                print("Please Enter yes or no\n")
                return False

    def display_roles(self):
        if self.users_roles[self.username] == "Admin":
            print("\nUsers available are :")
            for roles_ele, roles_obj in self.roles.items():
                print("{}, Permission=[Read:{}, Write:{}, Append:{}]".format(roles_ele, roles_obj.access_permission_obj.Read, roles_obj.access_permission_obj.Write, roles_obj.access_permission_obj.Append))