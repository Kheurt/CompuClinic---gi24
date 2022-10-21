from django.db.models import Model

class AdminImporter:

	@classmethod
	def register_models(cls, register, models):
		# Lister les membres de models
		classes = [c for c in dir(models) if not c.startswith("_")]

		# Evaluer chaque membre et register si membre est subclass de Model
		for c in classes:
			try:
				if issubclass(eval(c), Model):
					register(eval(c))
			except:
				pass
