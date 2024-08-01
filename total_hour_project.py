number_of_minites= input("inter number of total minites : ")
float_number_of_minites= float(number_of_minites)
number_of_hour=float_number_of_minites // 60 
number_of_minites= float_number_of_minites % 60
str_number_of_hour=str (number_of_hour)
str_number_of_minites= str(number_of_minites)
print("the total of hour = " + str_number_of_hour + " and " + str_number_of_minites + " minites ")