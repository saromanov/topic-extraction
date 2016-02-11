import rake

class Extract:
	def __init__(self):
		self.extraction = rake.Rake("SmartStoplist.txt",3,3,1)

	def get_keywords(self, text):
		return self.extraction.run(text)