montht = int(input('Input a month [1-12]:'))
dayt = int(input('Input a day [1-31]:'))
list_of_months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if montht == 1 or montht == 2 or montht == 12:
    a = 'winter'
elif montht ==4 or montht ==5 or montht == 3:
    a = 'spring'
elif montht == 7 or montht == 8 or montht ==6:
    a = 'summer'
else:
    a = 'autumn'
# print(just_list)
# for y in just_list:
#     print(y, end = " ")
print(list_of_months[montht-1],',', dayt,'.','Season is',a)
