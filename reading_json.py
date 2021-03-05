import json

with open('example_data.json','r') as read_it:
	data = json.load(read_it)
	
print(data)