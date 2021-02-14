import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'U3VubpXQTdMAAAAAAAAAAd_RRFzrNEVcKNibpRDIuik5zPazkTmhPZdu4ctkwwTJ'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :-")
    file_to = '/Python/upload.txt'

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

if __name__ == '__main__':
    main()