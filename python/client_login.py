import base64
import paramiko

client = paramiko.SSHClient()
#hostname='10.76.68.199'
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.76.68.199', username='rtestuser', password='ironport')
#print(" Connecting to %s \n with username=%s... \n" % (username))
stdin, stdout, stderr = client.exec_command('ls -l')
stdin, stdout, stderr = client.exec_command('pwd' )
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()