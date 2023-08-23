import re
import function as FO

def Project_Choice():

    Choice = input("Please Enter 'C' For Create New Project: \nPlease Enter 'V' For View All Projcts: \nPlease Enter 'E' For Edit Your Own Project: \nPlease Enter 'D' For Delete Your Own Project: \nPlease Enter 'S' For Searching: ")
    if Choice.lower() == 'c':
        CreateP()
    elif Choice.lower() == 'v':
        Pro_Veiw()
    elif Choice.lower() == 'e':
        Edit_Proj()
    elif Choice.lower() == 'd':
        Del_Pro()
    elif Choice.lower() == 's':
        Search() 
    else:
        print("please Enter From Choices Only")       
def CreateP():
    TargetV = r"^[0-9]+"
    DateV = r"^[0-9]{1,2}[/.-][0-9]{1,2}[/.-][0-9]{4}$"
    Mobile_Pattern = r"^[01][0|1|2|5][0-9]{9}"

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
    ID = FO.Generate_ProID()
    ProjectsData = f"{ID}:{Title}:{Details}:{Target}:{StrDate}:{EndDate}:{Mobile}"
    Saved = FO.SaveProjects(ProjectsData)
    if Saved:
        print(f"The Project Title Is {Title}\nThe Project Details Is:{Details}\nThe Project Total Start Date Is {StrDate}\nThe Project End Date Is {EndDate}")
        print("========== Project Created ==========")
    else:
        print("================= Error Happened =================")
    return 

def Pro_Veiw():
    print(FO.Read_Projects())
    
def Edit_Proj():
    FO.Edit_Pro()   

def Del_Pro():
    FO.Dele_Pr()    
    
def Search():
    FO.Search_Pr()    