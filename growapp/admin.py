from django.contrib import admin

from .models import Complaints_model, Feature_model, Feedback_model, Login_model, Product_model, User_model

# Register your models here.

admin.site.register(Login_model)
admin.site.register(User_model)
admin.site.register(Feedback_model)
admin.site.register(Feature_model)
admin.site.register(Product_model)
admin.site.register(Complaints_model)
