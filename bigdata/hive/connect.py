from impala.dbapi import connect

def connection():
    conn = connect(host='127.0.0.1', port=10000, database='default', auth_mechanism='PLAIN')
    cur = conn.cursor()

    return cur
