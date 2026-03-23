version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

version_raw1=version_raw.strip()
print('去掉空格: '+version_raw1)
print('转大写:   '+version_raw1.upper())
print('替换版本: '+version_raw1.replace("17.03.04", "17.06.01"))
