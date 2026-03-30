import os,re,shutil
files = {
    'R1_config.txt': 'hostname R1\ninterface GigabitEthernet0/0\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R2_config.txt': 'hostname R2\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R3_config.txt': 'hostname R3\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'SW1_config.txt': 'hostname SW1\ninterface Vlan1\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
}
current_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(current_dir+"/backup")
backup_dir = current_dir+"/backup"
for file,conf_value in files.items():
    with open(backup_dir+"/"+file, "w") as f:
        f.write(conf_value)
device_list = []
for file in os.listdir(backup_dir):
    with open(backup_dir+"/"+file, "r") as f:
        conf_value = f.read()
        config_value_list= conf_value.split("\n")
        for config_value in config_value_list:
            if re.match(r"^\s*shutdown\s*$", config_value):
                device_list.append(file)
                break
if device_list:
    print('发现包含 shutdown 接口的设备配置文件：')
    for device in device_list:
        print(device)
else:
    print('未发现包含 shutdown 接口的设备配置文件')
if os.path.exists(backup_dir):
    shutil.rmtree(backup_dir)
if not os.path.exists(backup_dir):
    print('backup/ 目录已清理')
