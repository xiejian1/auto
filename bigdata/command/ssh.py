import sh
from subprocess import Popen,PIPE

cmd = "ssh root@139.159.140.183 ls /home/ubuntu"
p = Popen(cmd,stdin=PIPE,stderr=PIPE,shell=True)
data = p.communicate()
print(data)