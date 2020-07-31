def tab():
    print('---------------------------------')

tab()
# Create function
def Hello():
    print('Hello Robert')

# call function
Hello()
tab()

# Create function have parameter
def Sawatdee(friend):
    print('สวัสดี', friend)
    print('สบายดีไหม')

# call function and put variable
Sawatdee('จอห์น')
tab()

# Create function have parameter and add default value
def Sawatdee_V2(friend='Alex'):
    print('Hello', friend)
    
# call function and put variable
Sawatdee_V2('Jin')
tab()

# call function don't put variable
Sawatdee_V2()
tab()
