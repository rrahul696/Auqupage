import os
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
	def _readYamlFile(filepath):
		try:
			with open(filepath) as stream:
				return yaml.load(stream)
		except:
			print('Error opening', filepath)
			return {}

	@staticmethod
	def readAllYamlFiles():
		mappings = {}
		for rootDir, dirs, files in os.walk('../../inputs/processing/'):
			for filename in files:
				if '.yml' in filename:
					yaml_contents = FileProcessor._readYamlFile(rootDir + filename)
					mappings[yaml_contents['course_code']] = {}
					mappings[yaml_contents['course_code']]['title'] = yaml_contents['course_title']
					mappings[yaml_contents['course_code']]['mappings'] = yaml_contents['mappings']

		return mappings

	@staticmethod
	def writeJsonFile(filepath, obj):
		try:
			string = json.dumps(obj)
			with open(filepath, 'w') as stream:
				stream.write(string)
		except:
			print('Error writing JSON into', filepath)

	def getDirContents(root):
		files = []
		for rootDir, dirs, filenames in os.walk(root):
			files.extend(filenames)
		return files

	def writeQuestions(filepath, questions):
		string = ''
		for question in questions:
			string += '\n\nQuestion:\n\n' + question['question'] + '\n\n'
			string += '\nOptions:'
			for option in question['options']:
				string += '\n\t' + option
			if question['tags']:
				string += '\n\nTags:'
			for tag in question['tags']:
				string += '\n\t'+tag
				for subtag in question['tags'][tag]:
					string += '\n\t\t' + subtag
			# if question['input_tags']:
			# 	string += '\n\nTags based on injected mappings'
			# for input_tag in question['input_tags']:
			# 	string += '\n\t' + input_tag
			if question['errors']:
				string += '\n\nErrors:\n'+question['errors']
			else:
				string += '\n\nNo errors'
			string += '----------------------------------------------------------------'

		print(string)
		# with open(filepath, 'w'):



if __name__ == '__main__':
	
	# print(FileProcessor._readYamlFile('../../inputs/processing/python_keywords.yml'))
	# print(FileProcessor.readAllYamlFiles())
	print(FileProcessor.getDirContents('../../inputs/processing/'))
