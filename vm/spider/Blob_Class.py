import os
import sys
from azure.storage.blob import BlockBlobService, PublicAccess
from dotenv import load_dotenv

class Blob():
    def __init__(self):
        load_dotenv()
        self.local_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'media')
        self.container_name = None
        self.username = os.getenv('STORAGE_ACC_NAME')
        self.secret_key = os.getenv('AZURE_STORAGE_CONNECTIONSTRING')

    def create_container(self, conn, name: str):
        self.container_name = name
        # Create a container called 'report'.
        try:    
            conn.create_container(name)
            return True
        except Exception as e:
            print(e) 

    def list_media_files(self):
        '''Returns  a list of all downloaded media files'''
        files = []
        for (dirpath, dirnames, filenames) in os.walk(self.local_path):
            files.extend(filenames)
            break
        return files

    def upload_blob(self):
        try:
            # Create the BlockBlobService that is used to call the Blob service for the storage account
            blob_service_client = BlockBlobService( account_name=self.username, account_key=self.secret_key)
            
            # Create the container
            self.create_container(blob_service_client,'reports')
            
            # Set the permission so the blobs are public.
            blob_service_client.set_container_acl(self.container_name, public_access=PublicAccess.Container)
            
            # Get the name for all files 
            my_files = self.list_media_files()
            
            for files in my_files:
                local_file_name = files
                print(local_file_name)
                full_path_to_file = os.path.join(self.local_path, local_file_name)

                print("Current file = " + full_path_to_file)
                print("\nUploading to Blob storage as blob: " + local_file_name)

                # Upload the created file, use local_file_name for the blob name
                blob_service_client.create_blob_from_path(self.container_name, local_file_name, full_path_to_file)

            # List the blobs in the container
            print("\nList blobs in the container")
            generator = blob_service_client.list_blobs(self.container_name)
            for blob in generator:
                print("\t Blob name: " + blob.name)
                
        except Exception as e:
            print(e)