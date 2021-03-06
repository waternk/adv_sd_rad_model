class Element (object):
	def __init__ (self,name):
		self.name=name

	def __str__(self):
		return self.name

from enum import Enum

class ValueTypeConstant(Enum):
	auxiliary = 0
	constant = 1
	data = 2
	initial = 3
	level = 4
	lookup = 5
	realityCheck = 6
	string = 7
	subscript = 8
	timeBase = 9
    
class ValueType(object):
	def __init__(self,valueTypeConstant,value):
		self.valueTypeConstant = valueTypeConstant
		self.value = value

class ValueElement (Element):
	def __init__ (self,name,valueType):
		Element.__init__(self,name)
		self.valueType = valueType

class Variable (ValueElement):
	def __init__(self,name,valueType):
		ValueElement.__init__(self,name,valueType)

	def __str__(self):
		return "Variable [" + self.name + "]"

class Flow (ValueElement):
	def __init__(self,name,valueType,src,dst):
		ValueElement.__init__(self,name,valueType)   
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