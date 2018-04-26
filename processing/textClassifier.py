import json
# from processText import ProcessText
# from read_files import readFilesInDir
import sys
sys.path.append('../')
from utils.textProcessor import TextProcessor

class TextClassifier:
	
	@staticmethod
	def searchInCourseNgrams(ngrams_question):
		tags = {}
		for question_ngram_type in ngrams_question:
			for question_ngram in question_ngram_type:
				for course_key in course_ngrams:
					course = course_ngrams[course_key]
					for topic_key in course:
						topic = course[topic_key]
						for sub_topic in topic:
							for ngram_type in sub_topic:
								for ngram in ngram_type:
									if ngram == question_ngram:
										if course_key not in tags:
											tags[course_key] = {}
										if topic_key not in tags[course_key]:
											tags[course_key][topic_key] = {}
										ngram_key = ' '.join(ngram)
										if ngram_key not in tags[course_key][topic_key]:
											tags[course_key][topic_key][ngram_key] = 0
										tags[course_key][topic_key][ngram_key] += 1
		return tags

	@staticmethod
	def classifyQuestion(course_info, question = None):
		course_ngrams = TextClassifier._getCourseInfoNgrams(course_info)
		return course_ngrams

	@staticmethod
	def _getCourseInfoNgrams(course_info):
		course_ngrams = {}
		for course in course_info:
			course_code = course['code']
			course_title = course['title']
			course_ngrams[course_code] = {}
			course_ngrams[course_code]['title'] = course_title
			for topic in course['topics']:
				if 'title' not in topic or 'subtopics' not in topic:
					continue
				topic_title = topic['title']
				course_ngrams[course_code][topic_title] = {}
				for subtopic in topic['subtopics']:
					stemmed_subtopic = TextProcessor.getStemmedText(subtopic)
					course_ngrams[course_code][topic_title][subtopic] = TextProcessor.get2and3Ngrams(stemmed_subtopic)
		return course_ngrams

if __name__ == '__main__':
	with open('../outputs/extraction/course_info.json') as fp:
		course_info = json.loads(fp.read())
	print(json.dumps(TextClassifier.classifyQuestion(course_info)))
