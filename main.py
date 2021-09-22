import os
import sys
import json

IMAGES = {}

def add(folderPath):
	images = os.listdir(folderPath)
	for img in images:
		IMAGES[img] = {
			"tags": [],
			"name": img
		}
	print(f'Successfully added folder "{folderPath}"')
	_save_imgs(IMAGES)
	return IMAGES

def tag(imgPath,tagList):
	IMAGES = _read_imgs()
	if (imgPath in IMAGES):
		IMAGES[imgPath]["tags"].append(tagList)
	else:
		IMAGES[imgPath] = {}
		IMAGES[imgPath]["tags"] = [tagList]
	_save_imgs(IMAGES)
	print("Successfully tagged", imgPath, "with", tagList)

def search(query,opt):
	results = []
	IMAGES = _read_imgs()
	
	if (opt == "-f"):
		for x in IMAGES:
			if (query in IMAGES[x]["name"]):
				results.append(IMAGES[x])
	if (opt == "-t"):
		for x in IMAGES:
			if (query in IMAGES[x]["tags"]):
				results.append(IMAGES[x])
	return results
	
	
def _save_imgs(data, location="IMAGES.json"):
	'''Save JSON data to the location'''
	with open(location, "w") as outfile:
		json.dump(data, outfile)


def _read_imgs(location="IMAGES.json"):
	'''Read data from the location to a JSON object'''
	with open(location, "r") as infile:
		return json.load(infile)
	
	
def main():
	try:
		funct = sys.argv[1]
		if funct=="tag":
			tag(sys.argv[2], sys.argv[3])
		elif funct=="add":
			print(add(sys.argv[2]))
		elif funct=="search":
			print(search(sys.argv[2], sys.argv[3]))
		else:
			raise(f"ERROR: Incorrect action {funct}.")
	except:
		print(f"Incorrect input {sys.argv[1:]}")



if __name__ == '__main__':
	main()
