import gensim


class Similarity:
	def __init__(self, alpha=0.05, workers=10):
		self.item = gensim.Doc2Vec(alpha=alpha, workers=workers)

	def training(self, dataset, epoch=50):
		self.item.build_vocab(dataset)
		for i in range(epoch):
			self.item.train(epoch)
			self.item.alpha -= 0.01
			self.item.min_alpha = self.item.alpha

	def sim(self, sent):
		return self.item.most_similar(sent)


# Word2Vec for similarity between the words
