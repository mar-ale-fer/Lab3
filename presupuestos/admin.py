from django.contrib import admin
from .models import Cliente
from .models import Presupuesto

admin.site.register(Cliente)
admin.site.register(Presupuesto)

