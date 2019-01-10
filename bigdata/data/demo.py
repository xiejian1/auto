from pyhdfs import HdfsClient

client = HdfsClient(hosts='127.0.0.1:50070')  #50070是端口号
flag = client.copy_from_local(localsrc='/home/bearning/test.txt',dest='/data/hdfs/hello/test.txt')
print(flag)
