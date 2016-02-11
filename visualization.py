from bokeh.charts import Bar, output_file, figure
from bokeh.plotting import figure,output_notebook

def bar(data):
	p = Bar(data, title="Topic extraction")
	show(p)

def plotting(self, data):
	pass