from pyspark.ml.clustering import Kmeans

# Learning at the stream

class Clustering:
	def __init__(self, centroids=20, seed=1234):
		self.sparks = KMeans(centroids=centroids, seed=1234)
		self.model = None

	def train(self, frame):
		self.sparks.parallize()
		self.model = self.spark.fit(frame)

	def predict(data):
		return self.model.predict(data)


class Classification:
	def __init__(self):
		pass