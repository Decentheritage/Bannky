
import pymysql
import random


mypro = pymysql.connect(host='127.0.0.1', user='root', passwd='' , database='Bank_trial')
mycursor = mypro.cursor()
# mycursor.execute("CREATE DATABASE Bank_trial")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE Zenith_Bank (ctm_id INT(4), Firstname VARCHAR(20), Lastname VARCHAR(20), Email VARCHAR(20)UNIQUE, Password VARCHAR(20), Confirm_password VARCHAR(20), Phone_number VARCHAR(11)UNIQUE,Pin INT(4), Confirm_Pin INT(4), Username VARCHAR(10)UNIQUE, Account_number INT(10), Account_balance VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor: 
#     print(table)


mtn = ['0703','0706','0803','0806','0903','0906','+234703','+234706','+234803','+234806','+234903','+234906']
glo = ['0705','0805','0707','0709','0805','0807','+234705','+234805','+234707','+234709','+234805','+234807']
airtel = ['0702','0708','0802','0808','+234702','+234708','+234802','+234808']
class First:
    def __init__(self):
        self.nu = 'nu'
    
        
    #    MAIN 
    def main(self):
        opin = 1
        print('Welcome to Zenith Bank\n Press 1. to Register or 2. to Login')
        while opin <= 3:
            opinion = input('Enter your Option please: ')
            if opinion == '1':
                f.reg()
                break
            elif opinion == '2':
                f.log()
                break
            else:
                print('Wrong input')
                opin += 1
        else:
            print('Wrong input')
            quit()
               
        # REGISTRATION
    def reg(self):
        pincount = 1
        phonecount = 1
        First_name = input('Enter your Firstname: ')
        Last_name = input('Enter your Lastname: ')
        Email = input('Enter your Email: ')
        Password = input('Enter your Password: ')
        Confirm_password = input('Confirm Password: ')
        while phonecount <= 3: 
            Phone_number = input('Enter your Phone Number: ')
            if Phone_number[:4] in mtn and len(Phone_number) == 11 or Phone_number[:7] in mtn and len(Phone_number) == 14:
                print('Mtn')
                break
            elif Phone_number[:4] in glo and len(Phone_number) == 11 or Phone_number[:7] in mtn and len(Phone_number) == 14:
                print('Glo')
                break
            elif Phone_number[:4] in airtel and len(Phone_number) == 11 or Phone_number[:7] in airtel and len(Phone_number) == 14:
                print('Airtel')
                break
            else:
                print('Invalid Phone Number')
                phonecount += 1
        else:
            print('Multiple wrong input')
            quit() 
        while pincount <= 3:
            Pin = int(input('Enter your Pin: '))
            Confirm_pin = int(input('Cornfirm your Pin: '))
            if Pin == Confirm_pin :
                print('Your Pin is Correct')
                break
            else:
                print('Wrong Pin Match')
                pincount += 1
        else:
            print("You've Tried Multiple Times")
            quit()         
        Username = input('Enter Username: ')
        Account_number = random.randrange(1111111111,2222222222)
        Account_balance = 0
        magic = "INSERT INTO Zenith_Bank (First_Name,Last_Name,Email,Password,Confirm_Password,Phone_Number,Pin,Confirm_Pin,Username,Account_Number,Account_Balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (First_name,Last_name,Email,Password,Confirm_password,Phone_number,Pin,Confirm_pin,Username,Account_number,Account_balance)
        mycursor.execute(magic,val)
        mypro.commit()
        print(f"Welcome {First_name}\nYour Account Number is {Account_number}\nAnd your balance is {Account_balance}\nYou can now proceed to Login")
        
        # LOGIN
    def log(self):
        userpin = 1
        print('Welcome to Zenith Bank')
        Username = input('Enter your Username: ')
        Pin = int(input('Enter your Pin: '))
        data = "SELECT * FROM Zenith_Bank WHERE Username = %s AND Pin = %s"
        val = (Username,Pin)
        mycursor.execute(data,val)
        balm = mycursor.fetchone()
        while userpin <= 3:   
            if Username == balm[-3] and Pin == balm[-5]:
                print(f'Welcome {balm[1]} {balm[2]}')
                break
            else:
                print('Your Username or Pin did not match\nTry again')
                userpin += 1
        else:
            print('Your grace is overdue')
            quit()
        
        
f = First()
f.main()       
# f.reg()
# f.log()       

        
        




    
    
    
    
    
    