from django.contrib import admin
from .models import OX_law, OX_safety, OX_service, OX_transit
from .models import Law_easy, Law_normal, Law_hard, Transit_easy, Transit_normal, Transit_hard
from .models import Safety_easy, Safety_normal, Safety_hard, Service_easy, Service_normal, Service_hard
from .models import Practice, Challenge

# Register your models here.
admin.site.register(OX_law)
admin.site.register(OX_safety)
admin.site.register(OX_service)
admin.site.register(OX_transit)
admin.site.register(Law_easy)
admin.site.register(Law_normal)
admin.site.register(Law_hard)
admin.site.register(Transit_easy)
admin.site.register(Transit_normal)
admin.site.register(Transit_hard)
admin.site.register(Safety_easy)
admin.site.register(Safety_normal)
admin.site.register(Safety_hard)
admin.site.register(Service_easy)
admin.site.register(Service_normal)
admin.site.register(Service_hard)
admin.site.register(Practice)
admin.site.register(Challenge)