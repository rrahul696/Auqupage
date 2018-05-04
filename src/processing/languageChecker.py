from language_check import LanguageTool
from nltk import word_tokenize as tokenize

class LanguageChecker:
	
	language_tool = LanguageTool('en-GB')

	@staticmethod
	def checkLanguage(question):
		text = question['question']
		matches = LanguageChecker.language_tool.check(text)
		errors = ''

		lines = text.split('\n')
		for match in matches:
			message = str(match)
			message_lines = message.split('\n')
			# if not message_lines:
			# 	continue
			# print(message_lines)
			try:
				line_no = message_lines[0].split(',')[0]
				errors += line_no + ': ' + message_lines[3] + '\n' + (' ' * (len(line_no) + 2)) + message_lines[4] + '\n' + message_lines[2] + '\n\n'
			except:
				continue
		question['errors'] = errors

if __name__ == '__main__':
	text = '''my name is rahil. I is awesome
	i is also goods boyz
	psych yay!
	'''

	# text = 'I am a good boy'
	print(LanguageChecker.checkLanguage(text))