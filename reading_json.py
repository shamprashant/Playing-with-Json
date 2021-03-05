import json

#reading json file
with open('example_data.json','r') as read_it:
	data = json.load(read_it)

#printing our json file data
print(data)