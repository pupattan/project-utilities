import socket
import tempfile
from smb.SMBConnection import SMBConnection

class Smb(object):
    def __init__(self, username, password, server, share, port=139, domain=""):
        # split username if it contains a domain (domain\username)
        if '\\' in username:
            domain, username = username.split('\\') if username.count('\\') == 1 else ('', username)
        elif not domain.strip():
            raise Exception("domain must be provided")

        # setup data
        self.domain    = str(domain)
        self.username  = str(username)
        self.password  = str(password)
        self.client    = socket.gethostname()
        self.server    = str(server)
        self.server_ip = socket.gethostbyname(server)
        self.share     = str(share)
        self.port      = port
        self.conn      = None
        self.connected = False

    def connect(self):
        print(self.__dict__)
        self.conn = SMBConnection(self.username, self.password,
                                  self.client, self.server,
                                  use_ntlm_v2=True, domain=self.domain)
        self.connected = self.conn.connect(self.server_ip, self.port)
        print("coonected")
        return self.connected


if __name__ == '__main__':
    server = "server.com"   # server URL/DNS or hostname
    username = "pupattan"  # Username
    password = "Hghabaygad6#123"    # Password
    folder_name = r"Corpusfraace"   # Folder/directory name
    file_path = r'/YT/files/xml/7766212.xml'    # File path including sub-directory

    # --------------- Create object --------------
    smb = Smb('CORP\\'+username, password, server, folder_name)
    # or
    # smb = Smb(username, password, server, remote_name, domain="CORP")

    # --------- Connect -----------
    smb.connect()

    file_obj = tempfile.NamedTemporaryFile()
    file_attributes, filesize = smb.conn.retrieveFile(folder_name, file_path, file_obj)
    print(file_attributes)
    print(filesize)
    # Use file_obj to write your file that you read from remote location
    file_obj.close()

