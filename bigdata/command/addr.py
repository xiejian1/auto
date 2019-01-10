

# import psutil
#
# users = psutil.users()
#
# addr = users[0].host
# print(addr)

import socket

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip = s.getsockname()
    finally:
        s.close()

    print(ip[0])
if __name__ == '__main__':
    get_host_ip()