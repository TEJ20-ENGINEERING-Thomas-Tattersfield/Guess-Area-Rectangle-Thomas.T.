# These ask the user to input the measurements
User_Input_Length = int(input ("Please input the length: "))
User_Input_Width = int(input ("please input the width: "))
User_Input_Area = int(input ("Please input the area: ")) 
# Line 6 calculates the true area
area = User_Input_Length * User_Input_Width 
# This line does the compareson 
if User_Input_Area == area: 
  print ("This is correct") 
if User_Input_Area < area :
  print ("your answer is smaller than the area") 
if User_Input_Area > area :
  print ("your answer is larger than the area")