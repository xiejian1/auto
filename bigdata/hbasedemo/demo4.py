from hbasedemo.demo1 import conn
from hbase.ttypes import Mutation,BatchMutation

# mutation = Mutation(column='account:idcard',value='346565635265716326')
mutation1 = Mutation(column='address:city',value='渝北区')
mutation2 = Mutation(column='address:province',value='chongqing')
batchmutation = BatchMutation(row='lisi',mutations=[mutation1,mutation2])
client = conn()
client.mutateRows(tableName='user',rowBatches=[batchmutation])
# client.mutateRow(tableName='user',row='lisi',mutations=[mutation])
print("插入数据")
