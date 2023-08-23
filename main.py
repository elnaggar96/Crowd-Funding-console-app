import register as RL
import creat_projects as PR
print("*****************Welcome*************")


Choice = input("Please Enter 'R' For Registration: \n  and if you  Have An Acount Please Enter 'L': ")
if Choice.lower() == "r":
    Ac=RL.Register()
    if Ac == 'success':
        PR.Project_Choice() 
elif Choice.lower() == 'l':
    Log = RL.Login()
    if Log == True:
        print("Create Your Project")
        PR.Project_Choice()
    elif Log == 'forget':
            forg = RL.Forgett()
            if forg == 'login':
                RL.Login()
            else:
                RL.Register() 
    elif Log == 'ask register':
        RL.Register()
else:
    print("Please Re Enter R or L :")
