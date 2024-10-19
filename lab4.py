# 1 esep
sum_odd = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        sum_odd += i
    i += 1
print("Тақ сандардың қосындысы:", sum_odd)

# 2 esep
# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
# print("kosindylar:", sum)

# 3 esep
# n = int(input("Vvedite kolichestvo chisel Fibonachchi: "))
# fib1 = 1
# fib2 = 1
# print(fib1, fib2, end=" ")
# for i in range(2, n):
#     fib_next = fib1 + fib2
#     print(fib_next, end=" ")
#     fib1, fib2  =  fib2, fib_next

# 4 esep
# str = 'X-DSPAM-Confidence:0.8475'
# colon_pos = str.find(':')
# number = float(str[colon_pos+1:])
# print("resultat:", number)

# 5 esep
# input_str = input("vvedite slova: ")
# first_char = input_str[0]
# s_char = input_str[len(input_str) // 2]
# l_char = input_str[-1]
# new_str = first_char + s_char + l_char
# print("novaya stroka:", new_str)

# 6 esep
# main_str = input("osnovnoe: ").lower()
# sub_str = input("vnutrnnee: ").lower()
# vxozhdenie = main_str.count(sub_str)
# print("obshee:", vxozhdenie)

# 7 esep
input_str = input("vvedite: ")
bukvy = 0
chisla = 0
simvoly = 0

for char in input_str:
    if char.isalpha():
        bukvy += 1
    elif char.isdigit():
        chisla += 1
    else:
        simvoly += 1

print("Әріптер саны:", bukvy)
print("Сандар саны:", chisla)
print("Арнайы таңбалар саны:", simvoly)




