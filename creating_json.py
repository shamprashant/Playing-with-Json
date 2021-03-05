# Python program showing  
# use of json package 
  
import json 
  
# {key:value mapping} 
data = {
	'name': 'prashant',
	'course': 'B.Tech',
	'college': 'ABESIT college of engineering'
}

# conversion to JSON done by dumps() function 
json_data = json.dumps(data)

# printing the output 
print(json_data) 