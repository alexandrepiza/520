import paramiko

try:
    con = paramiko.client.SSHClient()
    con.load_system_host_keys()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.connect('192.168.202.8',
                    username='sabado',
                    password='sabado')
except Exception as e:
    print('Erro conexão: {}'.format(e))
    exit()

stdin, stdout, stderr = con.exec_command('cat /etc/apt/sources.list')
if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))