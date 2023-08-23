import re 
import function as FO

def Register():
    Email_pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    Mobile_Pattern = r"^[01][0|1|2|5][0-9]{9}"
    while True:
        while True:
            Fname = input("Please Enter Your First Name: ")
            if Fname.isalpha():
                break
            else:
                print("Please Enter Valid First Name")
        while True:
            Lname = input("Please Enter Your Last Name: ")
            if Lname.isalpha():
                break
            else:
                print("Please Enter Valid Last Name")
        while True:
            Email = input("Please Enter Your Email: ")
            if re.fullmatch(Email_pattern,Email):
                break
            else:
                print("Please Enter Valid Email")
        Password = input("Please Enter Your Password: ")
        while True:
            Confirm_Password = input("Please Enter Your Password Again: ")
            if Confirm_Password == Password:
                break
            else:
                print("Password Do Not Match Enter Again")  

        while True:
            Mobile = input("Please Enter Your Mobile: ")
            if re.fullmatch(Mobile_Pattern,Mobile):
                break
            else:
                print("Please Enter Valid Mobile Number")
        break 
    ID = FO.Generate_ID()
    UserData = f"{ID}:{Fname}:{Lname}:{Email}:{Password}:{Mobile}\n"
    Saved = FO.SaveUsers(UserData)
    if Saved :
        print(f"Register Successfully Wellcome {Fname} {Lname}")
    else:
        print("================= Error Happened =================")    
    return "success"       
#####################################################################################

def Login():   
    for i in range(5)  :
        Em = input("Please Enter Your Email: ")    
        Passw = input("Please Enter Your Password: ")
        if FO.Get_Specific_User(Em,Passw):
            print("----------Login Success----------")
            return True
        else:
            print("Please Enter Correct Password")
    return "forget"
    
def Forgett():
    print("==================== For Recovery Your Password ====================")
    Em = input("Please Enter Your Email: ")
    Ph = input("Please Enter Your Phone Number: ")
    if FO.Get_Forget_User(Em,Ph):
        return 'login'
    else:
        print("Your Number And Your Email Are Not Exists")
        return 'ask register'

