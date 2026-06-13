# Step 1 : Collecting student Information from the user
print("Enter student details")
name = input("Enter Student name :")
Reg_num = input("Enter Registration number :")
program = input("Enter program :")
semester = input("Enter Current Semester :")
cgpa = input("Enter CGPA :")

# Step 2 : Display the information in a well-formatted report
print("\n" + "="*30)
print("     STUDENT PROFILE     ")
print("="*30)
print(f"Name :           {name}")
print(f"Reg_num :        {Reg_num}")
print(f"program :        {program}")
print(f"semester :       {semester} ")
print(f"cgpa :           {cgpa}")
print("="*30)
