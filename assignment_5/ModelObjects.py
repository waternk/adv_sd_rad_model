class Element (object):
	def __init__ (self,name, unit):
		self.name=name
		self.unit=self.cleanUnit(unit)

	def cleanUnit(self, unit):
		bracket_index = unit.find('[')

		if bracket_index > -1:
			return str(unit[0:bracket_index]).strip()
		else:
			return unit.strip()

	def __str__(self):
		return "{0}({1})".format(self.name, self.unit)

class ValueElement (Element):
	def __init__ (self,name,unit):
		Element.__init__(self,name, unit)

class Variable (ValueElement):
	def __init__(self,name,unit):
		ValueElement.__init__(self,name,unit)

	def __str__(self):
		return "Variable [{0}({1})]".format(self.name, self.unit)

class Flow (ValueElement):
	def __init__(self,name,unit,src,dst):
		ValueElement.__init__(self,name,unit)   
		self.src = src
		self.dst = dst

	def __str__(self):
		return "Flow [{0}({1}) {2} => {3}]".format(self.name, self.unit, self.src, self.dst)

class StockElement (Element): pass
class Source (StockElement):
	def __init__ (self,name):
		StockElement.__init__(self,name,"dmnl")

	def __str__(self):
		return "Source [{0}]".format(self.name)

class Sink (StockElement):
	def __init__ (self,name):
		StockElement.__init__(self,name,"dmnl")

	def __str__(self):
		return "Sink [{0}]".format(self.name)

class Stock (ValueElement,StockElement):
	def __str__(self):
		return "Stock [{0}({1})]".format(self.name, self.unit)

class Link (object):
	def __init__(self,src,dst):
		self.src = src
		self.dst = dst