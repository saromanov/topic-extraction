from pyspark.ml.clustering import StreamingKMeans

# Learning at the stream

class Clustering:
	def __init__(self, centroids, weights):
		self.sparks = StreamingKMeans(centroids, weights)
		self.model = None

	def update(self, frame):
		self.sparks.parallelize(frame,2)
		return self.spark.update(frame, 1, u"batches")
