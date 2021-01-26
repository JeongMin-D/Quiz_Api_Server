from django.contrib import admin
from .models import Multiple_easy, OX_easy, Test_easy
from .models import Multiple_normal, OX_normal, Test_normal
from .models import Multiple_hard, OX_hard, Test_hard

# Register your models here.
admin.site.register(Multiple_easy)
admin.site.register(Multiple_normal)
admin.site.register(Multiple_hard)
admin.site.register(OX_easy)
admin.site.register(OX_normal)
admin.site.register(OX_hard)
admin.site.register(Test_easy)
admin.site.register(Test_normal)
admin.site.register(Test_hard)