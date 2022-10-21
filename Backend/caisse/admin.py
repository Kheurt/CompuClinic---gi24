from django.contrib import admin
# from . import models as module_models
from .models import *
# from django.db.models import Model

# # Lister les membres de models
# classes = [c for c in dir(module_models) if not c.startswith("_")]

# print(classes)

# # Evaluer chaque membre et register si membre est subclass de Model
# for c in classes:
# 	try:
# 		res = issubclass(eval(c), Model)
# 		print(res)
# 		if res:
# 			admin.site.register(eval(c))
# 	except:
# 		print(c)

admin.site.register(Bon)
admin.site.register(AGV)
admin.site.register(BGS)
admin.site.register(BSC)
admin.site.register(TIAPS)
admin.site.register(Quittance)
