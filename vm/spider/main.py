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
    
    # Get the list of new files (Their names)
    new_files = email.file_name
    
    if new_files != []:
        for n in new_files:
            logger.info("New file detected " + n)
            clean.convert_to_csv(n)
            
    
    logger.debug("Blob method to upload files from the media folder to blob storage")
    blob.upload_blob()
    
if __name__ == "__main__":
    main()

