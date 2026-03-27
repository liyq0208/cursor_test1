import os,re
result = os.popen("ifconfig ens33").read()
match = re.match(r"[\s\S]+inet\s+([\d\.]+)[\sa-z]+([\d\.]+)[\sa-z]+([\d\.]+)[\s\S]+ether\s+([a-f\d:]+)",result)
# print(match.groups())
ip, netmask, broadcast, mac = match.groups()
print('{:<10}: {}'.format('IP',ip))
print('{:<10}: {}'.format('Netmask',netmask))
print('{:<10}: {}'.format('Boradcast',broadcast))
print('{:<10}: {}'.format('MAC',mac))
print('--------------------------------')
print("ping网关测试：")
gateway=re.match(r"(\d+\.){3}",ip).group(0)+"1"
result_ping=os.popen(f"ping {gateway} -c 2").read()
print(result_ping)  