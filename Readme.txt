RBAC system assumptions and cmd promt guide

How to run:
Run the script: Blue_stacks_main_pro.py 
Latest version of python 3.8 and above

Modules to be imported:
import sys
Cmd: pip install sys

Dependencies:
Scripts which have to be in same path to run the program:
Blue_stacks_main_pro.py
Blue_stacks_console_class.py
Blue_stacks_user_class.py
Blue_stacks_role_class.py
Blue_stacks_database_class.py
Blue_stacks_resources_class.py
Blue_stacks_access_modes_class.py

All the mentioned scripts have to be in one folder as the  Blue_stacks_main_pro.py script


Each user can have one role and can be changed only by admin role user..
Each Role can have 3 permission Read, Write, Append which can be set by Admin role User..
When a new user is created by default user will have the Basic_user role which can be changed by Admin Role user..
Resources, Roles , Users can be added deleted..
At the startup i have created 2 roles Admin, Basic_user as default roles, and 2 resources code1,code2 as default..
At the startup i hav created a Admin user with Admin role as default..

Admin user:(Default user)
Username: Admin
Password: Admin


I have Created a interactive input based console for interaction with the program:
Startup console:

--------------Hello Welcome to the RBAC System--------------

1. Login to an Existing User
2. Add a User
3. Exit the Console

Admin user console:

 ---------Logged into user Admin--------- 
1. Role Based Services 
3. Resource Based Services
4. Go back to Logging Console
5. Exit the Console

User Based Services(only for admin):

 ---------Logged into user Admin in user_based_services--------- 
1. Add a User --------------To Add user
2. Delete a User --------------To Del user
3. Display Users Available --------------To Display available users
4. Go Back to Admin Console --------------To go back
5. Exit the Console

Role based Services(only for Admin):

 ---------Logged into user Admin in role_based_services--------- 
1. Add a Role --------------To Add role
2. Delete a Role --------------To del role
3. Update Role of a User --------------To update a role of a user
4. Display Roles Available --------------To display available roles
5. Go Back to Admin Console --------------Go back
6. Exit the Console

Resources based services (For all users but add and del resources are activated only for Admin)

Here u can choose the action on the reource then it will ask for resource name based on the permission the access will be granted or denied

 ---------Logged into user Admin in resources_based_services--------- 
1. Add a Resource	  --------------To Add resources
2. Delete a Resource  --------------To del resources
3. Read a Resource    --------------{
4. Write a Resource	  --------------Here u can choose the action on the reource then it will ask for resource name based on the permission the access will be granted or denied
5. Append a Resource  --------------}
6. Display Resources Available --------------List of available resources
7. Go Back to Admin Console --------------Go back
8. Exit the Console