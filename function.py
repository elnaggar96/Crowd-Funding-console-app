import re

def Generate_ID():
    Users = Read_Users_Content()
    # print(Users)
    if isinstance(Users,list):
        No_Of_Users = len(Users)
        if No_Of_Users == 0 :
            return 1
        else:
            LastUser = Users[-1]
            LastUser = LastUser.split(":")
            NewID = int(LastUser[0])+1
            return NewID
    else:
        return False  
    
def Read_Users_Content():
    try:
        FileObject = open('Users.txt','r')
    except Exception as e :
        return False
    else:
        Users = FileObject.readlines()
        return Users            

def SaveUsers(data):
    try:
        FileObject = open('Users.txt','a')
    except Exception as e:
        return False
    else:
        FileObject.write(data)
        FileObject.close()
        return True


def Get_Specific_User(Email,Pass):
    Users = Read_Users_Content()
    for User in Users:
        UserDate = User.strip("\n")
        UserDate = UserDate.split (":")
        if UserDate[3]==Email and UserDate[4]==Pass:
            return True
    else:
        return False 
    
def Get_Forget_User(Email,Phone):
    Users = Read_Users_Content()
    for User in Users:
        UserDate = User.strip("\n")
        UserDate = UserDate.split (":")
        if UserDate[3]==Email and UserDate[5]==Phone:
            print (f"Your Password Is {UserDate[4]} Please Don't Forget It Again")
            return True
    else:
        return False 
            
        
###################################################################    

def Read_Projects():
    try:
        FileObject = open('Projects.txt','r')
    except Exception as e :
        return False
    else:
        Proj = FileObject.readlines()
        return Proj  

def Generate_ProID():
    Proj = Read_Projects()
    if isinstance(Proj,list):
        No_Of_Proj = len(Proj)
        if No_Of_Proj == 0 :
            return 1
        else:
            LastUser = Proj[-1]
            LastUser = LastUser.split(":")
            NewID = int(LastUser[0])+1
            return NewID
    else:
        return False 

def SaveProjects(data):
    try:
        FileObject = open('Projects.txt','a')
    except Exception as e:
        return False
    else:
        FileObject.write(data)
        FileObject.close()
        return True    
    

    
def Write_Pro(Proj:list):
    try:
        Fileoperation = open('Projects','w')
    except Exception as e:
        return False             
    else :
        Fileoperation.writelines(Proj)
        Fileoperation.close()
        return True
def Dele_Pr():
    Mob = input("Please Enter Your Phone: ")
    ID = input("Please Enter Project ID: ")
    Projs = Read_Projects()
    for index,Pro in enumerate(Projs):
        pro = pro.strip("\n")
        pro = pro.split(":")
        if Pro[0]== str(ID) and Pro[6] == str(Mob):
            del Projs[index]
            Write_Pro(Projs)
        else:
            print("This Project Not Your Own Project")    
            
def Edit_Pro():
    TargetV = r"^[0-9]+"
    DateV = r"^[0-9]{1,2}[/.-][0-9]{1,2}[/.-][0-9]{4}$"
    Mobile_Pattern = r"^[01][0|1|2|5][0-9]{9}"
    Mob = input("Please Enter Your Phone: ")
    ID = input("Please Enter Project ID: ")
    Projs = Read_Projects()
    for index,Pro in enumerate(Projs):
        pro = pro.strip("\n")
        pro = pro.split(":")
        if Pro[0]== str(ID) and Pro[6] == str(Mob):
            del Projs[index]
            Write_Pro(Projs)
            while True:
                Title = input("Please Enter Project Title: ")
                if Title.isalpha():
                    break
                else:
                    print("Please Enter Valid Title")
            Details = input("Please Enter Project Details: ")
            while True:
                Target = input("Please Enter Total Targer: ")
                if re.fullmatch(TargetV,Target):
                    break
                else:
                    print("Please Enter Valid Target")
            while True:
                StrDate = input("Please Enter Start Date Of The Project: ")
                if re.fullmatch(DateV,StrDate):
                    break
                else:
                    print("Please Enter Valid Date")
            while True:
                EndDate = input("Please Enter End Date Of The Project: ")
                if re.fullmatch(DateV,EndDate):
                    break
                else:
                    print("Please Enter Valid Date") 
            while True:
                Mobile = input("Please Enter Your Mobile: ")
                if re.fullmatch(Mobile_Pattern,Mobile):
                    break
                else:
                    print("Please Enter Valid Mobile Number")         
            ID = Generate_ProID()
            ProjectsData = f"{ID}:{Title}:{Details}:{Target}:{StrDate}:{EndDate}:{Mobile}"
            Saved = SaveProjects(ProjectsData)
            if Saved:
                print(f"The Project Title Is {Title}\nThe Project Details Is:{Details}\nThe Project Total Start Date Is {StrDate}\nThe Project End Date Is {EndDate}")
                print("========== Project Edited ==========")
            else:
                print("================= Error Happened =================")
            return             
        else:
            print("This Project Not Your Own Project")
            

def Search_Pr():
    ID = input("Please Enter Project ID: ")
    Projs = Read_Projects()
    for index,Pro in enumerate(Projs):
        pro = pro.strip("\n")
        pro = pro.split(":")
        if Pro[0]== str(ID):
            print(Projs[index])
        else:
            print("This Project Not Your Own Project")               