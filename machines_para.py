import paramiko
import re
import string

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.217.128",22,username="mine",password="123456")
stdin,stdout,stderr = client.exec_command("cat /etc/network/interfaces.bk")
for line in stdout.readlines():

    if "dns-nameserver" in line:
        print line
        line_yu=line
        lines=re.sub("dns-nameserver.*","dns-nameserver 10.3.70.253 172.16.2.2",line)
        string_du=" sudo sed -i 's/"+line_yu.replace('\n','')+"/"+lines.replace('\n','')+"/g' /etc/network/interfaces.bk"
        print string_du
        print lines
stdin,stdout,stderr = client.exec_command(string_du,get_pty=True)
stdin.write('123456\n')
stdin.flush()
print stderr.readlines()
client.close()
