from Mail_Class import Mail
from Blob_Class import Blob
from Logger_func import my_logger
import datetime
now = datetime.datetime.now()
logger = my_logger("main function")

def main(): 
    logger.debug(f"SPIDER MICROSERVICE ACTIVATED - { now.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.debug("Calling instances")
    # Instances 
    email = Mail()
    logger.debug("Instace email called: " + str(email))
    blob = Blob()
    logger.debug("Instace Blob called: " + str(blob))
 
    # Methods 
    logger.debug("Email method to check new .xlsx reports:")
    email.subjectQuery("Azure")
    
    logger.debug("Blob method to upload files from the media folder to blob storage")
    blob.upload_blob()

if __name__ == "__main__":
    main()

