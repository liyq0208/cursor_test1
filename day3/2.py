import re
conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
conn_t=re.match(r'(\S+)[^\d]+([\d\.]+):(\d+)[^\d]+([\d\.]+):(\d+)',conn).groups()
# print(conn_t)
print('{:<12}: {}'.format('Protocol',conn_t[0]))
print('{:<12}: {}'.format('Server IP',conn_t[1]))
print('{:<12}: {}'.format('Server Port',conn_t[2]))
print('{:<12}: {}'.format('Client IP',conn_t[3]))
print('{:<12}: {}'.format('Client Port',conn_t[4]))