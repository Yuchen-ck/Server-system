from auth_function import *
DBstring = "mongodb+srv://root:kershaw1027@myfldb.tclbx48.mongodb.net/?retryWrites=true&w=majority"
if __name__ == '__main__':
    print("歡迎使用本系統。")

    # auth_First(DBstring)
    Aggregate(DBstring)
    
    
   
        