import os,re

route_n_result=os.popen("route -n").read()
# print(route_n_result)
# re.match(r"[\s\S]*(0\.){3}0\s+((\d+\.){3}\d+)\s+).*UG[\s\S]+",route_n_result)
gateway=re.match(r"[\s\S]*(?:0\.){3}0\s+((?:\d+\.){3}\d+)[\s\S]+UG",route_n_result).group(1)
# print(result.group(1))

print("网关为：",gateway)