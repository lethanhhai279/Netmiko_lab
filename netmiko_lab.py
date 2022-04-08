import netmiko
SW = {
    'device_type':'cisco_ios',
    'ip':'10.215.27.190',
    'username':'vnpro',
    'password':'vnpro@123',
    'secret':'vnpro@321'
}
connect = netmiko.ConnectHandler(**SW)
print(connect.enable())
# show_ip = connect.send_command('show ip int br')
# show_run = connect.send_command('show run')
# print(show_ip)
# print(show_run)
# new_hostname = connect.send_config_set(['hostname Switch'])
# print(new_hostname)
# new_vlan = connect.send_config_set([' no vlan 10','do sh vlan'])
# print(new_vlan)
for i in range(10,41,10):
    tao_vlans = connect.send_config_set([f'vlan {i}'])
    print(tao_vlans)
print(connect.send_command('sh vlan br'))
port = 1
for i in range(10,31,10):
    set_ip = connect.send_config_set([f'int e0/{port}','no switchport',f'ip address 192.168.{i}.1 255.255.255.0'])
    port+=1
print(set_ip)
print(connect.send_command('sh ip int br'))
# name_vlan = ['GD','KT','KeToan','ThuKy','BV']
# num_vlan = 10
# for j in name_vlan:
#     tao_vlans = connect.send_config_set([f'vlan {num_vlan}',f'name {j}'])
#     num_vlan+=10
#     print(tao_vlans)
# print(connect.send_command('sh vlan'))

