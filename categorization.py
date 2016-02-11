from sklearn.ensemble import RandomForestClassifier
from sklearn import grid_search
from sklearn.feature_extraction.text import CountVectorizer
from spark_sklearn import GridSearchCV


class Classifier:
	def __init__(self):
		self.model = None

	def preprocess(self, data):
		return CountVectorizer().fit_transform(data)

	def train(self,X, y):
		param_grid = {
		  "max_depth": [6, None],
		  "max_features": [5,10,20],
		  "bootstrap": [True, False],
		}
		self.model = GridSearchCV(RandomForestClassifier(), param_grid=param_grid)
		self.model.fit(X, y)

	def preidict(self, X):
		return self.model.predict(X)