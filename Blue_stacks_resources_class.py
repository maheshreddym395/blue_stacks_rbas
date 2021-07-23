class Resources():
    def __init__(self,r_name):
        self.resource_name=r_name

    def add_resources(self):
        if self.users_roles[self.username] == "Admin":
            print("\nPlease enter the name of the resource to be Added")
            name = input()
            if self.resources.get(name,-1)==-1:
                temp=Resources(name)
                self.resources[name]=temp
                print("Resource {} Added Successfully".format(name))
            else:
                print("Rssource {} is already existed".format(name))
        else:
            print("Sorry you dont have Access to add resources please choose other actions")
        return False

    def del_resources(self):
        if self.users_roles[self.username] == "Admin":
            print("\nPlease enter the name of the resource to be Deleted")
            name = input()
            if self.resources.get(name,-1)!=-1:
                del self.resources[name]
                print("Resource {} Deleted Successfully".format(name))
            else:
                print("Rssource {} is doesnot exist".format(name))
        else:
            print("Sorry you dont have Access to Delete resources please choose other actions")
        return False

    def display_resources(self):
        print("\nResources available are :")
        for res_ele in self.resources.keys():
            print("{},".format(res_ele))
        return False

    def read_resources(self):
        print("Resources available for Reading")
        self.display_resources()
        print("\nPlease enter the name of the resource to be Read")
        name = input()
        if self.resources.get(name, -1) == -1:
            print("Resource {} is not present please select available resources".format(name))
        else:
            if self.roles[self.users_roles[self.username]].access_permission_obj.Read==1:
                print("Resource {} Read Successfully".format(name))
            else:
                print("Sorry Resource {} is not allowed to Read for you".format(name))
        return False

    def append_resources(self):
        print("Resources available for Appendin")
        self.display_resources()
        print("\nPlease enter the name of the resource to Append")
        name = input()
        if self.resources.get(name, -1) == -1:
            print("Resource {} is not present please select available resources".format(name))
        else:
            if self.roles[self.users_roles[self.username]].access_permission_obj.Append==1:
                print("Resource {} Appended Successfully".format(name))
            else:
                print("Sorry Resource {} is not allowed to Append for You".format(name))
        return False

    def write_resources(self):
        print("Resources available for writing")
        self.display_resources()
        print("\nPlease enter the name of the resource to writing")
        name = input()
        if self.resources.get(name, -1) == -1:
            print("Resource {} is not present please select available resources".format(name))
        else:
            if self.roles[self.users_roles[self.username]].access_permission_obj.Write==1:
                print("Resource {} was modified Successfully".format(name))
            else:
                print("Sorry Resource {} is not allowed to write for You".format(name))
        return False
