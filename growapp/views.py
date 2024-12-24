from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from growapp.models import Complaints_model, Login_model, User_model
from .forms import *

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request, 'login2.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
       
        try:
            obj=Login_model.objects.get(username=username,password=password)
            request.session['user_id']=obj.id
            if obj.type=='admin':
                return redirect('home')
            else:
                return HttpResponse("user type not recognized")
        except Login_model.DoesNotExist:
            return HttpResponse("does not exist")
            
            
class Home(View):
    def get(self,request):
        c = Product_model.objects.all()[:5]
        return render(request,'Home.html',{'hina':c})
    
class Feedback(View):
    def get(self,request):
        obj=Feedback_model.objects.all()
        return render(request,'Feedback.html',{'val':obj})
    
class Complaints(View):
    def get(self,request):
        obj=Complaints_model.objects.all()
        return render(request,'Complaints.html',{'val':obj})

    
class Manageuser(View):
    def get(self,request):
        obj=User_model.objects.all()
        return render(request,'manageusers.html', { 'hina':obj })
    
class Prod_view(View):
    def get(self,request):
        obj=Product_model.objects.all()
        return render(request,'Prod_view.html', { 'hina':obj })    
    
class Deleteuser(View):
    def get(self,request,pk):
        obj=User_model.objects.get(pk=pk)
        obj.delete()
        return redirect('manageuser')
    

class Addnewuser(View):
    def get(self,request):
        return render(request,'addnewuser.html')
    def post(self,request):
        c=Adduser_form(request.POST)
        if c.is_valid():
            f = c.save(commit=False)
            f.LOGIN_ID=Login_model.objects.create(username=request.POST['username'], password=request.POST['password'])
            f.save()
            return redirect('/manageusers')
        
class Replycomplaint(View):
    def post(self,request):
        compid=request.POST['complaintId']
        obj=Complaints_model.objects.get(pk=compid)
        obj.Reply=request.POST['Reply']
        obj.save()
        return redirect('complaints')

class Addproducts(View):
    def get(self,request):
        return render(request,'addproducts.html')
    def post(self,request):
        c=Addproduct_form(request.POST, request.FILES)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script> alert('product add sucessfully');window.location='/Prod_view' </script>''')
       
    
    
class Deleteproduct(View):
    def get(self,request,pk):
        obj=Product_model.objects.get(pk=pk)
        obj.delete()
        return HttpResponse('''<script> alert('product deleted sucessfully');window.location='/Prod_view' </script>''')
       
 