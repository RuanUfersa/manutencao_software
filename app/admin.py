from django.contrib import admin
from app.models import Verduras
from app.models import Frutas
from app.models import Entrega
from app.models import Pagamento
from app.models import Item

admin.site.register(Verduras)
admin.site.register(Frutas)
admin.site.register(Entrega)
admin.site.register(Pagamento)
admin.site.register( Item)
