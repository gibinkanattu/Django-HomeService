from django.contrib import admin
from .models import User,State,District,Area,Profile,Notification,Feedback,Order,JobCategory,RequestWork,Location
# Register your models here.
# admin.site.register(User)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Area)
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(JobCategory)
admin.site.register(Feedback)
admin.site.register(Order)
admin.site.register(RequestWork)
admin.site.register(Location)
