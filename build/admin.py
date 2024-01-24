from django.contrib import admin

# Register your models here.

from .models import (
    Service, 
    Activitie,
    Ourblog,
    Partner,
    Contact

)

admin.site.register(Service),
admin.site.register(Activitie),
admin.site.register(Ourblog),
admin.site.register(Partner),
admin.site.register(Contact)

# user: Korxona
# parol: 123