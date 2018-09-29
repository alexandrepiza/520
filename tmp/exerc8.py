stdin, stdout, stderr = client.exec_command('Is -la')
if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
print(stderr.read().decode('utf-8'))