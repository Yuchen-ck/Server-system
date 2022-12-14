from aggregate_utils import *
from fedAVG import *

def Aggregate(DBstring):
    print("開始聚合模型")
    '''
    1. 從clientDB下載模型
    2. FedAVG Algorithm : package FL_main/FL_main from github
    3. 聚合後上傳模型至serverDB
    4. 刪除資料夾檔案
    '''
    #1. 從clientDB下載模型
    downloadFolderPath = download_client_model_DB(DBstring)
    count = clientNumber(downloadFolderPath)
    
    #2. FedAVG Algorithm，聚合完成的模型，直接加密上傳至enc_server_model folder
    FedAVG(count,fixKey = b'hRtqZZr0I5QEF1JMLvbtY3ZsX6DxrMJd0tQvftc3XHQ=')

    #3. 聚合後上傳模型至serverDB
    # clearDB(DBstring) ---> 是否需要清空，待討論
    encFolder = './enc_server_model/'
    # encryptAllFiles(origFolder,encFolder,fixKey)
    upload_server_model(DBstring,encFolder)

    ##4. 刪除系統內部的資料檔
    #   (把原有資料夾刪除，再重新建立新的資料夾)
    clientModelPath  = './client_model/'
    encSerModelPath = './enc_server_model/'
    ##step1 : 刪除現有資料夾
    delete_UsedFolder(clientModelPath)
    delete_UsedFolder(encSerModelPath)

    ##step2 : 建立新的資料夾(相同名稱)
    os.makedirs(clientModelPath)
    os.makedirs(encSerModelPath)



