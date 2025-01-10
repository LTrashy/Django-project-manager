from django.contrib import admin

# Register your models here.
from .models import Project, Ticket, UserStory
# Register your models here.
admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(UserStory)