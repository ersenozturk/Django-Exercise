from django.contrib import admin
from .models import Creator, Language, Frameworks, Developers

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Frameworks)
admin.site.register(Developers)

# Register your models here.
