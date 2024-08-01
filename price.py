str_length= input  ("please type length :")
str_width= input("please type width :")
length=float(str_length)
width= float(str_width)
area= length* width
str_area=str(area)
str_much= input("how much for 1 metar ? ") 
much=float(str_much)
total= much * area
str_total=str(total) 
print ("the total area is : " + str_area )
print("give the guy :$" + str_total)
