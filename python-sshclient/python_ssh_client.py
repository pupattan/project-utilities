import paramiko

hostname = 'example.com'
port = 22
username = 'pupattan'
password = 'nnn23n12388123'

if __name__ == "__main__":
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print(stdout.read())
    s.close()