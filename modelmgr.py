# manage models
import modelloader

MODELS = {}

def register_model(name, desc):
	MODELS[name] = desc
	return(name)
	
def model_names():
	return(list(MODELS.keys()))

def load_models():
	modelloader.load_all()
	return(model_names())
	
def load_model(name):
	modelloader.load_model(name)
	return(name)
	
def model_files(name):
	return(MODELS[name][files])
	

	
