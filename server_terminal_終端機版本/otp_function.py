def OTP_second():
    for i in range(3):
        OTP_code = input("請輸入OTP碼：")
        
        if OTP_code == 'test':
            print("歡迎使用本系統")
            break
        elif i == 2:
            print("對不起，您輸入的OTP錯誤已達%s次，系統強制退出"%(i+1))
        else:
            print("Error username or passwd.")
            print("對不起，您輸入的OTP或密碼有誤!")