name_1 = "Flu"
name_2 = "TheFire"
full_name = name_1 + name_2
print(full_name)

# _1
print('My name is {}'.format(full_name))

# _2
print(f'My name is {full_name}') #f'' คือ format string

money = 1000
# _3
print(f'I have money: {money:,d}') # :,d คือ functionพิเศษที่จะใส่ , ไว้ที่ตัวเลข

account = 1234.1234
# _3.1
print(f'I have moeny: {account:,.2f}') # .xf คือ ใช้ปัดทศนิยมให้เหลือ x หลัก
