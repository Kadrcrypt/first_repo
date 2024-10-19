# 1 esep

# def process_file(filename):
#     with open(filename, 'r') as file:
#         slova = set(file.read().split())  
#     return sorted(slova)  

# filename = 'romeo.txt'
# sorted_slova = process_file(filename)
# print(sorted_slova)

# 2
 
# def emails(filename):
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
# emails = emails(filename)
# for email, count in emails.items():
#     print(f'{email}: {count}')

# 3 esep

def emails(filename):
    emails_count = {}
    file = open(filename, 'r')
    try:
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]  
                emails_count[email] = emails_count.get(email, 0) + 1  
    finally:
        file.close()
    
    return emails_count

filename = 'mbox-short.txt'
emails = emails(filename)

max_email = None
max_count = 0

for email, count in emails.items():
    if count > max_count:
        max_count = count
        max_email = email

print(f'Ең көп хабар келген электрондық пошта: {max_email}, хабар саны: {max_count}')
