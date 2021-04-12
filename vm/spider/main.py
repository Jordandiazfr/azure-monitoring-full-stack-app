from Mail_Class import Mail
from Blob_Class import Blob
from Clean_Class import Cleaner
from Logger_func import my_logger
import datetime
now = datetime.datetime.now()
logger = my_logger("MAIN * Function")

def main(): 
    logger.debug(f"SPIDER MICROSERVICE ACTIVATED - { now.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.debug("Calling instances")
    # Instances 
    email = Mail()
    logger.debug("Instace email called: " + str(email))
    blob = Blob()
    logger.debug("Instace Blob called: " + str(blob))
    clean = Cleaner()
    logger.debug("Instace Clean called: " + str(clean))
    
    # Methods 
    logger.debug("Email method to check new .xlsx reports:")
    email.subjectQuery("Azure")
    
    name = email.file_name
    clean.convert_to_csv(name)
    
    logger.debug("Blob method to upload files from the media folder to blob storage")
    blob.upload_blob()

if __name__ == "__main__":
    main()

