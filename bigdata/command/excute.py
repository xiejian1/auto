import sh
import os
dirs = os.path.abspath(__file__)
print(dirs)
print("执行复制")
# sh.scp(dirs,"root@139.159.140.183:/home/ubuntu/")
result = sh.ps("/usr/bin/ps")
print(result)
print("复制结束")