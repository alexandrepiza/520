import paramiko

try:
    client = paramiko.client.SSHClient()
    client.load system host keys()
    client.set missing host key policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1',
                    username='bran',
                    password='4linux',
                    port=12222')
except Exception as e:
    print('Erro conexão: {}’.format(e))
    exit()

stdin, stdout, stderr = client.exec_command('Is -la')
if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
print(stderr.read().decode('utf-8'))