import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, rb) as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'xlCQ0Lsv2rwAAAAAAAAAARAqqtJrRPcMMuW-Mw3kLij3ZLDBrhBEf7gG4e2PssIc'
    transferData = TransferData(access_token)

    file_from = input("Enter the file name to transfer: ")
    file_to = input("Enter the destination where the file should be transferred: ")

    transferData.upload_file(file_from, file_to)
    print("File uploaded!")

if __name__ == '__main__':
    main()