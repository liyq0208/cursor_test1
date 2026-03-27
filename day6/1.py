import re
asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

asa_conn_list = asa_conn.split('\n')
pattern=(
    r"[^\d]*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)"
    r"[^\d]*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)"
    r".*bytes\s+(\d+).*flags\s+(\w+)$"
    )
asa_info_dict={}
for i in asa_conn_list:
    asa_info=re.match(pattern,i).groups()
    asa_info_dict[asa_info[0:4]]=asa_info[4:]
print('打印字典：')
print(asa_info_dict)
print('格式化打印：')
for key,value in asa_info_dict.items():
    print("{:<10}: {:<15} | {:<10}: {:<8} | {:<10}: {} | {:<10}: {}\n{:<10}: {:<15} | {:<10}: {:<8}".format('src',key[0],'src_port',key[1],'dst',key[2],'dst_port',key[3],'bytes',value[0],'flags',value[1]))
    print("="*100)

