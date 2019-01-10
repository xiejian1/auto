from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase

def conn():
    # thrift默认端口是9090
    socket = TSocket.TSocket('127.0.0.1',9090)
    socket.setTimeout(5000)

    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Hbase.Client(protocol)
    socket.open()
    return client

# print(client.getTableNames())  # 获取当前所有的表名
