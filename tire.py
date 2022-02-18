#My project: Result Viewing system

#A window will appear asking if you are a teacher or a student
#If the user types, he is a student. He will directly redirected to the result and he can only view the results but cannot change it.
#If the user types he is a teacher, the user must type the password to enter into the system and he or she can make changes into the system.
import os

#printing some instructions for the users
print(" \t\t\t\tARE YOU A STUDENT OR A TEACHER?")
print(" \t\t\tIf you are a student,Press S And If you are a teacher,Press T?")
#creating the list for the names,marks and result 
list_names = ["Ashim","Hari","Shyam","Sita","Rita","farin","Sarmila","Luffy","Naruto","Rem"]
marks = [78,45,67,34,12,67,45,78,23,90]
result = ["pass","just pass","pass","fail","fail","Pass","Just Pass","Pass","Fail","Pass"]
run = True


#creating the function for the students which can be accessed by both the teachers and the students
def student():
 #clearing the screen
 os.system('cls')
 print("\t\t\tResult of class 10")
 z = 0
 st_5 = len(list_names) 
 for z in range(st_5):
  print(list_names[z],":",marks[z],"  =",result[z])
  z = z + 1
  
 exi = input("Do you want to go Back to Main Menu(Y/N)\n")
 
 if exi=="Y" or exi=="y":
  head_1()
 elif exi=="N" or exi=="n":
  student()
 
def new_re():
 os.system('cls')
 print("\t\t\tResult of class 10")
 z = 0
 st_5 = len(list_names)
 # st_5 = st_5 - 1
 
 for z in range(st_5):
  print(list_names[z],":",marks[z],"  =",result[z])
  z = z + 1



#creating the function for the teacher (not for the students)
def Teacher():
 os.system('cls')
 print("\t\t\tResult of class 10")
 print("\t\t\tCan be modified")
 i = 0
 st_5 = len(list_names)
 #printing the names,marks and obtained result of the student
 for i in range(st_5):
   print(list_names[i],":",marks[i],"  =",result[i])
   i = i + 1
  
 que = input("Do you want to Modify?(Y/N)\n")
    
 if que=="Y" or que=="y":
     print("You have three option")
     print("You can delete the students name(press D)")
     print("you can add students name(press A)")
     print("you can replace students name(press R)")
     
     ans = input("Please make a choice\n")
     #for Deleting the names 
     if ans=="D" or ans=="d":
      os.system('cls')
      print("Delete the names and marks")
      
      dlt = str(input("Enter the name of student that you want to delete\n"))
     
      
      tr = 0
      for a in range(st_5):
       stu_1 = list_names[tr]
       stu_2 = marks[tr]
       stu_3 = result[tr]
       
       if dlt==stu_1:
        list_names.remove(stu_1)
        marks.remove(stu_2)
        result.remove(stu_3)
        new_re()
        lst_q = input("Do you want to Go to the main menu(Y/N)?\n")
        if lst_q=="Y" or lst_q=="y":
         head_1()
        else:
         Teacher()
       else:
        tr = tr + 1
     #For Adding the names
     elif ans=="A" or ans=="a":
      os.system('cls')
      
      print("Add the name and marks of the student")
      
      add_nam = input("Enter the name of student\n")
      add_mar = input("Enter the marks of the student\n")
      add_re = input("Enter the obtained result of the student\n")
      
      list_names.append(add_nam)
      marks.append(add_mar)
      result.append(add_re)
      
      print("successfully added the result")
      
      qut = input("Press enter to redirect to the homepage(Y/N)\n")
      
      if qut=="Y" or qut=="y":
       head_1()
     #For Replacing the names of the students
     elif ans=="R" or ans=="r":
      os.system('cls')
      
      print("Replace the names of the students")
      
      pp_nam = input("Enter the name of the student\n")
      pp_new_nam = input("Enter the new name of the student\n")
       
      tr = 0
      for a in range(st_5):
       stu_1 = list_names[tr]
       stu_2 = marks[tr]
       stu_3 = result[tr]
       
       if pp_nam==stu_1:
        list_names.remove(stu_1)
        marks.remove(stu_2)
        result.remove(stu_3)
        
        list_names.append(pp_new_nam)
        marks.append(stu_2)
        result.append(stu_3)       
      wrt = input("Do you want to go to Main Menu(Y/N)?\n")
      
      if wrt=="Y" or wrt=="y":
       head_1()
      elif wrt=="N" or wrt=="n":
       teacher()
     
     
     
  


def head_1():
 
 #main window/screen
 #Asking to the user if he/she wants to access the student's or teacher's system
 a = input("Enter your system\n")
 #validating the input 
 if a=="S" or a=="s":
  student()
 elif a=="T" or a=="t":
  print("Are you really a teacher?")
  ask = input("Please enter the required password to enter into the system\n")
  if ask=="Teacher@123456":
   Teacher()
  else:
   print("password Error.....Try Again")
   head_1()
 else:
  print("Error......Please Try again")
  os.system('cls')
  head_1()






head_1()

#Completed My Second Project
#Its not the best thing in the world but i am really proud of it.
#Thank You.....