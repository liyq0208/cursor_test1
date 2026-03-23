import re
interface = "GigabitEthernet0/0/1"

int_type = re.match("([^0-9]*)([0-9/]+)", interface).groups()[0]
int_num = re.match("([^0-9]*)([0-9/]+)", interface).groups()[1]

print('接口类型: '+int_type)
print('接口编号: '+int_num)



