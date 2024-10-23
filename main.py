from Database import *
from Train import *
from Data_collector import *
from Face_recog import *


def Edit_db():
    print("<<<<<<<Welcome to Data Base Editor>>>>>>>")
    print("Press 1 to Add Data")
    print("Press 2 to Delete Data")
    inp_edit=int(input("Press your input:"))
    if inp_edit==1:
        print()
        id=int(input("Enter the id of new student:"))
        name=str(input("Enter the name of new student:"))
        add_data(id,name)

        print("<<<Image Sample collection>>>")
        print(f"{name} Please come in front of camera")
        p=input("Press enter to start data collection:")
        if p=="":
            capture(id)

    elif inp_edit==2:
        print()
        id=int(input("Enter the id of student you want to delete:"))
        del_data(id)
    else:
        print("\nYou have pessed the wrong input.....")
        print("Please repeat...\n")
        Edit_db()
    



print("---------Welcome to AAS--------\n")
print("1.Student Details")
print("2.Edit Database")
print("3.Train AAS")
print("4.Start Attendance:")
inp=int(input("\nSelect the options:"))

if inp==1:
    data()
elif inp==2:
    Edit_db()
elif inp==3:
    train()
    # print("Please wait for some time...")
elif inp==4:
    face_recog()


