from otp_function import OTP_second
from aggregate_function import Aggregate

def auth_First(DBstring):
    for i in range(3):
        account = input("請輸入帳號：")
        passwd = input('請輸入密碼: ')
        if account == 'test' and passwd == 'test':
            print("Welcome %s login."%(account))
            OTP_second() 
            Aggregate(DBstring)
            break
        elif i == 2:
            print("對不起，您輸入的帳號密碼錯誤已達%s次，系統強制退出"%(i+1))
        else:
            print("Error username or passwd.")
            print("對不起，您輸入的帳號或密碼有誤!")