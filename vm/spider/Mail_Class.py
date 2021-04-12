import imaplib
import email
import os
from dotenv import load_dotenv
from Logger_func import my_logger
logger = my_logger("MAIL instance")

class Mail:
    def __init__(self):
        load_dotenv()
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.outputdir = os.path.join(self.current_dir,'media')
        self.user = os.getenv('EMAIL_USER')
        self.password = os.getenv('EMAIL_PASS')
        self.server = 'imap.gmail.com'
        self.subject = 'Azure'
        self.file_name = None
        self.new_file = 0
    
    # connects to email client through IMAP
    def connect(self, server, user, password) -> object :
        m = imaplib.IMAP4_SSL(self.server)
        m.login(self.user, self.password)
        m.select()
        logger.info("Connected to the mail server")
        return m
    
    def does_file_exist(self, my_file: str) -> bool:
        f = []
        for (dirpath, dirnames, filenames) in os.walk(self.outputdir):
            f.extend(filenames)
            break
        if my_file in f:
            logger.info( str(my_file) + " Already exist in the media folder")
            return True
        else:
            return False
    
    def file_is_excel(self, filename: str) -> bool:
        ext = filename.split(".")
        extension = ext[1]
        if extension ==  "xlsx" or extension == "csv":
            logger.info( str(filename) + " found this file with a correct extension")
            return True
        else:
            logger.info( str(filename) + " found in your mail has not a proper .xlsx or .csv extension")
            return False
        
    def create_media_folder(self):
        # Create Media folder if it not exists, and create a file in folder Sample to test the upload and download.       
        if not os.path.exists(self.outputdir):
                logger.info("Media folder doesn't exist: Creating a new one")
                os.makedirs(self.outputdir)
                logger.info("Media folder created")

    def download_report(self,m, emailid, outputdir):
        resp, data = m.fetch(emailid, "(BODY.PEEK[])")
        email_body = data[0][1]
        mail = email.message_from_bytes(email_body)
        if mail.get_content_maintype() != 'multipart':
            return
        for part in mail.walk():
            if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                # Get the name of the file and call the method to see if it exist
                self.create_media_folder()
                f_name = part.get_filename()
                
                if not self.does_file_exist(f_name) and self.file_is_excel(f_name):
                    open(outputdir + '/' + f_name, 'wb').write(part.get_payload(decode=True))
                    logger.info( str(f_name) + " was downloaded")
                    self.file_name = f_name
                    self.new_file += 1 
                else:
                    logger.info( str(f_name) + " was not downloaded, nothing changed") 
    # download attachments from all emails with a specified subject line
    # as touched upon above, a search query is executed with a subject filter,
    # a list of msg objects are returned in msgs, and then looped through to 
    # obtain the emailid variable, which is then passed through to the above 
    # download_report function
            
    def subjectQuery(self, subject:str):
        m = self.connect(self.server, self.user, self.password)
        m.select("Inbox")
        typ, msgs = m.search(None, '(SUBJECT "' + subject + '")')
        msgs = msgs[0].split()
        for emailid in msgs:
            self.download_report(m, emailid, self.outputdir)
