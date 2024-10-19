#  Есенбеков Кадыржан 
# 1 esep

# print ("Hello")

# 2 esep

# x = 10
# x = x + 5
# print(x)  

# 3 esep
# name = input("vvedite imya -> ")
# print("Privet", name)

# 4 esep
# chis_chas = float(input("vvedite skoka chasov: "))
# cahs_plat = float(input("skoka za chas: "))
# obshe_plat = chis_chas * cahs_plat
# print("obshaya summa:", obshe_plat)

# 5 esep
# eni = 17
# biiktigi = 12.0

# # print(eni // 2)  

# # # 2
# print(eni / 2.0)  

# # # 3
# # print(biiktigi / 3)  

# # # 4
# # print(1 + 2 * 5)  

#6 esep
# celsius = float(input("Цельсий бойынша температураны енгізіңіз: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Температура Фаренгейт бойынша:", fahrenheit)
 
# 7 esep
# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# if hours > 40:
#    overtime = (hours - 40) * (rate * 1.5)
#    pay = (40 * rate) + overtime
# else:
#    pay = hours * rate
# print("Pay:", pay)
 
# 8 eseptry:
# try:
#     hours = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))
    
#     if hours > 40:
#         overtime = (hours - 40) * (rate * 1.5)
#         pay = (40 * rate) + overtime
#     else:
#         pay = hours * rate
    
#     print("Pay:", pay)
# except ValueError:
#     print("Error, please enter numeric input")

 
# 9 esep 
# s = float(input("Enter score between 0.0 and 1.0: "))

# if 0.0 <= s <= 1.0:

#     if s >= 0.9:
#       g = "A"
#     elif s >= 0.8:
#        g = "B"
#     elif s >= 0.7:
#       g = "C"
#     elif s >= 0.6:
#        g = "D"
#     else:
#        g = "F"
#     print("Grade:", g)
# else:
#     print("Error, score out of range")

# s = float(input("Enter score between 0.0 and 1.0: "))

# if 0.0 <= s <= 1.0:
#     match s:
#      case s if s >= 0.9:
#       g = "A"
#      case s if s >= 0.8:
#        g = "B"
#      case s if s >= 0.7:
#        g = "C"
#      case s if s >= 0.6:
#        g = "D"
#      case _:
#        g = "F"
#     print("Grade:", g)
# else:
#     print("Error, score out of range")



# cicle

# while True:      
#         s = float(input("Enter score between 0.0 and 1.0 (or -1 to exit): "))
        
#         if s == -1:  
#             print("Exiting the program.")
#             break 

#         if 0.0 <= s <= 1.0:
#             match s:
#              case s if s >= 0.9:
#                 g = "A"
#              case s if s >= 0.8:
#                 g = "B"
#              case s if s >= 0.7:
#                 g = "C"
#              case s if s >= 0.6:
#                 g = "D"
#              case _:
#                 g = "F"
#             print("Grade:", g)
#         else:
#             print("Error, score out of range")

