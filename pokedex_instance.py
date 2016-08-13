from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='internap2')


# Launching Instance
print "Delete Previous Instances"
instance_name = 'pokedex_server_dojo2'
#[cloud.delete_server(str(x.id)) for x in tst]
servers = conn.list_servers()
servers = [str(server.name) for server in servers]
if instance_name in servers:
	conn.delete_server(instance_name)

print "Selected image:"       
image_id = 'b9ba51bb-1852-4759-b80e-e588f40784db'
image = conn.get_image(image_id)
print(image)

print "\nSelected flavor:"
flavor_id = 'A1.1'
flavor = conn.get_flavor(flavor_id)
print(flavor)

#edit github address later
ex_userdata = '''#!/usr/bin/env bash
curl -L -s https://raw.githubusercontent.com/SerDigital/OpenStack/master/script.sh | bash -s --
'''

external_network = '2c65343d-5112-4141-b41d-9f35f0ddf6e3'

print('Checking for existing security groups...')
sec_group_name = 'web'
if conn.search_security_groups(sec_group_name):
    print('Security group already exists. Skipping creation.')
else:
    print('Creating security group.')
    conn.create_security_group(sec_group_name, 'network access for a web application.')
    conn.create_security_group_rule(sec_group_name, 80, 80, 'TCP')

print "\nServer creation:"
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    userdata=ex_userdata,
    network=external_network,
    security_groups=['default',sec_group_name])
