from django.contrib import admin
from .models import Product
from .models import Male_Eyeglasse
from .models import Male_Necklace
from .models import Male_Cap
from .models import Male_Earring
from .models import Female_Eyeglasse
from .models import Female_Necklace
from .models import Female_Cap
from .models import Female_Earring

# Register your models here.

#admin.site.register(Products)
admin.site.register(Product)
admin.site.register(Male_Eyeglasse)
admin.site.register(Male_Necklace)
admin.site.register(Male_Cap)
admin.site.register(Male_Earring)
admin.site.register(Female_Eyeglasse)
admin.site.register(Female_Necklace)
admin.site.register(Female_Cap)
admin.site.register(Female_Earring)