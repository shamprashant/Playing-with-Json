var = {
	"subjects": {
		"Maths":85,
		"Physics": 90
	}
}

import json

with open('example_data.json', 'w') as file:
	json.dump(var, file)