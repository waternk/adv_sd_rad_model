class Element (object):
	def __init__ (self,name):
		self.name=name

	def __str__(self):
		return self.name

class ValueElement (Element):
	def __init__ (self,name,unit):
		Element.__init__(self,name)
		self.unit = unit

class Variable (ValueElement):
	def __init__(self,name,unit):
		ValueElement.__init__(self,name,unit)

	def __str__(self):
		return "Variable [" + self.name + "]"

class Flow (ValueElement):
	def __init__(self,name,unit,src,dst):
		ValueElement.__init__(self,name,unit)   
		self.src = src
		self.dst = dst

	def __str__(self):
		return "Flow [" + self.name + ", " + str(self.src) + " => " + str(self.dst) + "]"

class StockElement (Element): pass
class Source (StockElement): 
	def __str__(self):
		return "Source [" + self.name + "]"

class Sink (StockElement): 
	def __str__(self):
		return "Sink [" + self.name + "]"

class Stock (ValueElement,StockElement):
	def __str__(self):
		return "Stock [" + self.name + "]"

class Link (object):
	def __init__(self,src,dst):
		self.src = src
		self.dst = dst