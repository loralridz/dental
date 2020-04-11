from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
	return render(request,'home.html',{})

def contact(request):
	if request.method == "POST":
		messege_name = request.POST['messege-name']
		messege_email = request.POST['messege-email']
		messege = request.POST['messege']
		
		return render(request,'contact.html',{})
	else:
		return render(request,'contact.html',{})