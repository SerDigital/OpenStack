from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='internap2')

# Ensuring container exists
available_containers  = conn.list_containers()
container_name = 'legendary-pokemons'
if container_name in available_containers:
	conn.delete_container(container_name)
container = conn.create_container(container_name)

# Populating container
pkmns = {'Articuno the Ice Bringer': 'Pokemon/articuno.png', 
	 'Moltres the Fire Bringer ': 'Pokemon/moltres.png',
	 'Ditto the CopyCat' : 'Pokemon/ditto.png'}
for object_name, file_path in pkmns.items():
	conn.create_object(container=container_name, name=object_name, filename=file_path)


