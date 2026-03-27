import re
mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'
# print(mac_table.split())
mac_table_t=re.match(r'(\d+)\s+([\da-f\.]+)\s+([A-Z]+)\s+([\S]+)',mac_table).groups()
vlan= mac_table_t[0]
mac= mac_table_t[1]
type= mac_table_t[2]
port= mac_table_t[3]
print('{:<6}: {}'.format('VLAN',vlan))
print('{:<6}: {}'.format('MAC',mac))
print('{:<6}: {}'.format('Type',type))
print('{:<6}: {}'.format('Port',port))
