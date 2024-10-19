# 2 esep
# def greet(a, b, c, d):
#     if a == b and c == d:
#         return "Сәлеметсіз бе"
#     elif a == 0:
#         return "Бағдарлама тоқтады"
#     else:
#         return "Бәріне сәлем"

# num = int(input("Бүтін сан енгізіңіз: "))
# result = greet(num, 10, 20, 20)
# print(result)

#3 esep
# def ComputePay(hours, rate):
#     if hours > 40:
#         overtime = (hours - 40) * (rate * 1.5) 
#         total_pay = (40 * rate) + overtime     
#     else:
#         total_pay = hours * rate 
#     return total_pay

# hours = float(input("Жұмыс сағаттарын енгізіңіз: "))
# rate = float(input("Тарифті енгізіңіз (сағатына төлем): "))

# pay = ComputePay(hours, rate)
# print(f"Жалпы төлем: {pay}")


#4 esep
# def CalculateGrade(score):
#     if score >= 0.9:
#         return "A"
#     elif score >= 0.8:
#         return "B"
#     elif score >= 0.7:
#         return "C"
#     elif score >= 0.6:
#         return "D"
#     else:
#         return "F"
# try:
#     score = float(input("Бағаны енгізіңіз (0-ден 1-ге дейін): "))
#     if 0 <= score <= 1:
#         grade = CalculateGrade(score)
#         print(f"Сіздің бағалауыңыз: {grade}")
#     else:
#         print("Қате: Баға 0 мен 1 аралығында болуы керек.")
# except ValueError:
#     print("Қате: Сандық мәнді енгізу қажет.")



# 5 esep
# def print_uppercase(filename):
#     try:
        
#         with open(filename, 'r') as file:
#             for line in file:
#                 print(line.upper())
#     except FileNotFoundError:
#         print(f"Файл '{filename}' не найден.")

# print_uppercase('primer.txt')

# 6 esep

# def process_file(filename):
#     with open(filename, 'r') as file:
#         words = set(file.read().split())  
#     return sorted(words)  

# filename = 'romeo.txt'
# sorted_words = process_file(filename)
# print(sorted_words)

#7 
# def count_emails(filename):
#     emails_count = {}
#     file = open(filename, 'r')
#     try:
#         for line in file:
#             if line.startswith('From '):
#                 email = line.split()[1]  
#                 emails_count[email] = emails_count.get(email, 0) + 1  
#     finally:
#         file.close()
    
#     return emails_count

# filename = 'mbox-short.txt'
# emails = count_emails(filename)
# for email, count in emails.items():
#     print(f'{email}: {count}')
