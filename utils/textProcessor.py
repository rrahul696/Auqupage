from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams
from re import fullmatch

class TextProcessor:
	
	@staticmethod
	def get2and3Ngrams(text):
		n_grams = []
		for n in range(2, 4):
			n_grams.append(tuple(map(lambda x: ' '.join(x), ngrams(filter(TextProcessor.isTokenAWord, word_tokenize(text)), n))))
		return n_grams

	@staticmethod
	def getStemmedText(text):
		porterStemmer = PorterStemmer()
		stop_words = set(stopwords.words('english'))
		return ' '.join(\
			map(lambda token: porterStemmer.stem(token),\
				filter(lambda token: len(token) > 1 and token not in stop_words,\
					map(lambda token: token.lower(), word_tokenize(text)))))

	@staticmethod
	def getWords(text):
		return tuple(map(lambda token: token.lower(), word_tokenize(text)))

	@staticmethod
	def isTokenAWord (token):
		return True if fullmatch(r'[A-Za-z]+[-]?[A-Za-z]*', token) else False

if __name__ == '__main__':
	text = 'the big bang theory, is one  awesome thepry! belive it, comon.'
	print(TextProcessor.get2and3Ngrams(text))
	print(TextProcessor.getStemmedText(text))