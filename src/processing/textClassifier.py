import json
import sys
sys.path.append('../')
from utils.textProcessor import TextProcessor

class TextClassifier:
	
	@staticmethod
	def classifyQuestiononCourseInfo(course_info, question):
		course_ngrams = TextClassifier._getCourseInfoNgrams(course_info)
		question_ngrams = TextClassifier._getQuestionNgrams(question)
		question['tags'] = {}

		for course_code in course_ngrams:
			course = course_ngrams[course_code]
			for topic_title in course['ngrams']:
				topic = course['ngrams'][topic_title]
				for subtopic_title in topic:
					subtopic = topic[subtopic_title]
					question_bigrams = question_ngrams[0]
					question_trigrams = question_ngrams[1]
					subtopic_bigrams = subtopic[0]
					subtopic_trigrams = subtopic[1]
					if subtopic_bigrams and question_bigrams:
						for question_bigram in question_bigrams:
							if question_bigram in subtopic_bigrams:
								if topic_title not in question['tags']:
									question['tags'][topic_title] = []
								question['tags'][topic_title].append(subtopic_title)
								break
					if topic_title in question['tags'] and subtopic_title in question['tags'][topic_title]:
						continue
					if subtopic_trigrams and question_trigrams:
						for question_trigram in question_trigrams:
							if question_trigram in subtopic_trigrams:
								if topic_title not in question['tags']:
									question['tags'][topic_title] = []
								question['tags'][topic_title].append(subtopic_title)

		return question
	
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
	def classifyQuestionOnInput():
		pass

	@staticmethod
	def _getCourseInfoNgrams(course_info):
		course_ngrams = {}
		for course in course_info:
			course_code = course['code']
			course_title = course['title']
			course_ngrams[course_code] = {}
			course_ngrams[course_code]['title'] = course_title
			course_ngrams[course_code]['ngrams'] = {}
			for topic in course['topics']:
				if 'title' not in topic or 'subtopics' not in topic:
					continue
				topic_title = topic['title']
				course_ngrams[course_code]['ngrams'][topic_title] = {}
				for subtopic in topic['subtopics']:
					stemmed_subtopic = TextProcessor.getStemmedText(subtopic)
					course_ngrams[course_code]['ngrams'][topic_title][subtopic] = TextProcessor.get2and3Ngrams(stemmed_subtopic)
		return course_ngrams

	def _getQuestionNgrams(question):
		stemmed_question = TextProcessor.getStemmedText(question['question'] + '\n' + question['expected_answer'])
		return TextProcessor.get2and3Ngrams(stemmed_question)


if __name__ == '__main__':
	with open('../outputs/extraction/course_info.json') as fp:
		course_info = json.loads(fp.read())
	print(json.dumps(TextClassifier.classifyQuestiononCourseInfo(course_info, {'question': 'On performing syntax directed translation  on a python program using bayesian learning and string algorithms and trees control flow graph\nOutput of min(list1) will be', 'expected_answer': '0.0'})))