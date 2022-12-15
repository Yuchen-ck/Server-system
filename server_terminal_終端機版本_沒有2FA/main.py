from auth_function import *
DBstring = "mongodb+srv://root:kershaw1027@myfldb.tclbx48.mongodb.net/?retryWrites=true&w=majority"
if __name__ == '__main__':
    print("歡迎使用本系統，請通過帳號密碼認證與OTP碼認證，才能正式啟用本系統。")

    #auth_First(DBstring)
    Aggregate(DBstring)
    
    
   
        
