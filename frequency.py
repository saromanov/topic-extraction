from nltk import bigrams, stopwords
from nltk.tokenize import word_tokenize
from collection import Counter

class Frequency:
	def __init__(self, data):
		self.stop = stopwords.words("english")
		self.data = [word_tokenize(word) for word in data]

	def fit(self, data):
		result = Counter()
		result.update([item for item in self.data])
		return result
