import json

def getData(file) :
	with open(file) as jsonData :
		data = json.load(jsonData)

	return data