import chilkat
import re
ssh = chilkat.CkSsh()
ipfile = open("iplist.txt", "r").readlines()
intVal = 3000
ssh.put_ConnectTimeoutMs(intVal)
result = open("result.txt", "a")

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
lst = []
for line in ipfile:
    if pattern.search(line) != None:
        lst.append(pattern.search(line)[0])


for ip in lst:
    print("Testing " + ip)
    success = ssh.Connect(ip, 22)
    connected = ssh.get_IsConnected()
    if (connected == True):
        connected = ssh.SendIgnore()

        print("connected => " + ip)
        result.write(ip + "\n")
    ssh.Disconnect()

if lst == []:
    print("No server found")
