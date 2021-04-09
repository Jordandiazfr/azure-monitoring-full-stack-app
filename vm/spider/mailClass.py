import imaplib
import email
import os
from dotenv import load_dotenv

class Mail:
    def __init__(self):
        load_dotenv()
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.outputdir = os.path.join(self.current_dir,'media')
        self.user = os.getenv('EMAIL_USER')
        self.password = os.getenv('EMAIL_PASS')
        self.server = 'imap.gmail.com'
        self.subject = 'Azure'
    
    # connects to email client through IMAP
    def connect(self, server, user, password):
        m = imaplib.IMAP4_SSL(self.server)
        m.login(self.user, self.password)
        m.select()
        return m
    
    def does_file_exist(self, file: str):
        f = []
        for (dirpath, dirnames, filenames) in os.walk(self.outputdir):
            f.extend(filenames)
            break
        if file in f:
            return True
        else:
            return False
    
    def download_report(self,m, emailid, outputdir):
        resp, data = m.fetch(emailid, "(BODY.PEEK[])")
        email_body = data[0][1]
        mail = email.message_from_bytes(email_body)
        if mail.get_content_maintype() != 'multipart':
            return
        for part in mail.walk():
            if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                # Get the name of the file and call the method to see if it exist
                f_name = part.get_filename()
                if not self.does_file_exist(f_name):
                    open(outputdir + '/' + f_name, 'wb').write(part.get_payload(decode=True))
                    print(f"New file {f_name} downloaded ")
                else:
                    print(f"File {f_name} already exist, nothing changed")       
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