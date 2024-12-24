from django.db import models

# Create your models here.

class Login_model(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    type=models.CharField(max_length=100,null=True,blank=True)
    
class User_model(models.Model):
    LOGIN_ID=models.ForeignKey(Login_model,on_delete=models.CASCADE, null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Phone_no=models.IntegerField(null=True,blank=True)

class Feature_model(models.Model):
    Humidity=models.CharField(max_length=100,null=True,blank=True)
    Temperature=models.CharField(max_length=100,null=True,blank=True)
    Moisture=models.CharField(max_length=100,null=True,blank=True)

class Feedback_model(models.Model):
     USER_ID=models.ForeignKey(User_model,on_delete=models.CASCADE,null=True,blank=True)
     created_at = models.DateField(auto_now_add=True)
     Review=models.CharField(max_length=100,null=True,blank=True)
     Feedback=models.CharField(max_length=100,null=True,blank=True)
    
    
class Product_model(models.Model):
      Product_name=models.CharField(max_length=100,null=True,blank=True)
      Quantity=models.IntegerField(null=True,blank=True)
      Price=models.IntegerField(null=True,blank=True)
      Image=models.FileField(upload_to='product/',null=True,blank=True)
      details=models.CharField(max_length=100,null=True,blank=True)


    
class Complaints_model(models.Model):
     LOGIN_ID=models.ForeignKey(Login_model,on_delete=models.CASCADE,null=True,blank=True)
     Complaints=models.CharField(max_length=100,null=True,blank=True)
     created_at = models.DateField(auto_now_add=True)
     updated_at = models.DateField(auto_now=True)
     Reply=models.CharField(max_length=100,null=True,blank=True)


     
