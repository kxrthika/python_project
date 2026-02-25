
country_code = {'bangladesh' : '0091' , 'Australia' : '0025' , 'nepal' : '0097'}
print("country code for : ")
print(country_code.get("bangladesh" , "user not found"))
print("country code for : ")
print(country_code.get("australia" , "user not found"))
print("country code for : ")
print(country_code.get("nepal" , "user not found"))
country_code["japan"] = "0081"
print("country code for : ")
print(country_code.get("japan" , "user not found"))
