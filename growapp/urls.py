
from django.urls import  path

from .views import *
urlpatterns = [
    path('',Login.as_view(), name='login'),
    path('home/',Home.as_view(),name='home'),
    path('feedback/',Feedback.as_view(),name='feedback'),
    path('complaints/',Complaints.as_view(),name='complaints'),
    path('manageusers/',Manageuser.as_view(),name='manageuser'),
    path('deleteuser/<int:pk>', Deleteuser.as_view(),name='deleteuser'),
    path('addnewuser/',Addnewuser.as_view(),name='addnewuser'),
    path('Replycomplaint',Replycomplaint.as_view(),name='Replycomplaint'),
    path('Prod_view',Prod_view.as_view(),name='Prod_view'),
    path('Addproducts',Addproducts.as_view(),name='addproducts'),
    path('deteleproduct/<int:pk>/',Deleteproduct.as_view(),name='Deleteproduct'),
    path('manageseeds/',Manageseeds.as_view(),name='manadeseeds'),
    path('addseed/',Addseed.as_view(),name='addseed'),
    path('deleteseed/<int:pk>/',Deleteseed.as_view(),name='Deleteseed'),

]

