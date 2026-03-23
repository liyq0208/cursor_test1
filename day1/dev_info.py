'''
========== 设备信息 ==========
设备名称: C8Kv1
管理地址: 192.168.1.1
厂商:     Cisco
型号:     C8000v
系统版本: IOS-XE 17.3.4
==============================
'''
hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"
print("========== 设备信息 ==========")
print(f"{'设备名称:':<6}{hostname}")
print(f"{'管理地址:':<6}{ip}")
print(f"{'厂商:':<8}{vendor}")
print(f"{'型号:':<8}{model}")
print(f"{'系统版本:':<6}{os_version}")
print("==============================") 


