from django.contrib import admin
from .models import Conferencias
from .models import Conferencista
from .models import Participantes
# Register your models here.


#------------------------------------------------------------
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'fecha', 'hora', 'conferencista')
    list_editable = ('nombre', 'conferencista')

admin.site.register(Conferencias, ConferenciaAdmin)
#------------------------------------------------------------
admin.site.register(Conferencista)
#------------------------------------------------------------
admin.site.register(Participantes)