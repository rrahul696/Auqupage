import json
import yaml

class FileProcessor:

	@staticmethod
	def readJsonFile(filepath):
		try:
			with open(filepath) as stream:
				return json.loads(stream.read())
		except:
			print('Error opening', filepath)
			return {}

	@staticmethod
	def readYamlFile(filepath):
		try:
			with open(filepath) as fp:
				return yaml.load(fp)
		except:
			print('Error opening', filepath)
			return {}

if __name__ == '__main__':
	
	print(FileProcessor.readYamlFile('../../inputs/processing/python_keywords.yml'))