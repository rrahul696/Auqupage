from utils.fileProcessor import FileProcessor
from processing.textClassifier import TextClassifier
from processing.languageChecker import LanguageChecker
from extraction.extractor import Extractor

def init():
	course_infos_inputs = FileProcessor.getDirContents('../inputs/extraction/course_infos')
	course_infos_outputs = FileProcessor.getDirContents('../outputs/extraction/course_infos')
	ip_filenames = map(lambda x: x.split('.')[0], course_infos_inputs)
	op_filenames = list(map(lambda x: x.split('.')[0], course_infos_outputs))
	for input in ip_filenames:
		if input not in op_filenames:
			Extractor.readCourseInfo('../inputs/extraction/course_infos/'+input+'.pdf', '../outputs/extraction/course_infos/'+input+'.txt')

def main():
	# init()
	questions = FileProcessor.readJsonFile('toc.json')['questions']
	course_info = FileProcessor.readJsonFile('course_info.json')
	# print(questions)
	# mappings = FileProcessor._readYamlFile('python.yml')
	for question in questions:
		# print(question)
		TextClassifier.classifyQuestionOnCourseInfo(course_info, question)
		# TextClassifier.classifyQuestionOnInput(mappings, question)
		LanguageChecker.checkLanguage(question)
	FileProcessor.writeQuestions('output.txt', questions)

if __name__ == '__main__':
	main()
