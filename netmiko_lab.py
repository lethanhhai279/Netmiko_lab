import netmiko
SW = {
    "device_type":"cisco_ios",
    "ip":"10.215.27.85",
    "username":"vnpro",
    "password":"vnpro@123",
    "secret":"vnpro@321"
}
connect = netmiko.ConnectHandler(**SW)
connect.enable()
# list_command = ["vlan 10","name VnPro"]
# print(connect.send_command("clear ip ospf process"))
# print(connect.send_config_set(list_command))

name = ["p1","p2","p3","p4","p5"]
vlan_id = 20
for i in name:
    print(connect.send_config_set([f"vlan {vlan_id}",f"name {i}"]))
    vlan_id += 10
print(connect.send_config_set(["do sh vlan br"]))

