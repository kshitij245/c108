import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token

    def upload_files(self,folder_from,folder_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(folder_from,'rb')
        dbx.files_upload(f.read(),folder_to)

def main():
    access_token='sl.BA-VPf6atki5L00ZqK5pr_dbLxGqRGF5lRJflOKGLjmN6puND6uXOSKaQ-jVs0Xj-agcR-7TcAPIfclTe9BIeL4ysNI1XxvrH8wDdbkO5a3sMGcucu9_Km4Dq7Dyzb_YlM1_fLeJrCzg'
    transferData=TransferData(access_token)
    folder_from=input("enter the  path folder to transfer: ")
    folder_to=input("enter the full path to upload to dropbox: ")
    transferData.upload_files(folder_from,folder_to)
    print("folder has been moved")

main()
