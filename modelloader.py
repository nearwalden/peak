# imports models 
# assumes package is 'models'

import importlib

MODEL_MODULE = "models"
	
def load_all():
	import models
	return True
	
def load_one(name):
	module = MODEL_MODULE + '.' + name
	importlib.import_module(module)
	return(name)
	

	
	
