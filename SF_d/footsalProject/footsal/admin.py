from django.contrib import admin

# Register your models here.
from .models import NewslPost,PhotoPost,ResultPost,Event,PhotoPost,PhotoOnlyPost,SPP,SPOP

admin.site.register(NewslPost)
admin.site.register(PhotoPost)
admin.site.register(ResultPost)
admin.site.register(Event)
admin.site.register(SPP)
admin.site.register(SPOP)