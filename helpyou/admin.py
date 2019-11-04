from django.contrib import admin
from .models import TD_categorias
from .models import TB_salas
from .models import TB_psicologos
from .models import TB_participantes

admin.site.register(TD_categorias)
admin.site.register(TB_salas)
admin.site.register(TB_psicologos)
admin.site.register(TB_participantes)
