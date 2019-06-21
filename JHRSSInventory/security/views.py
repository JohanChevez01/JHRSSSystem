
#security app
from django.shortcuts import render
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from Inventory.models import *


def home(request):
	return render(request,'home.html')

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))

def log_in(request):
	if request.method == 'POST':
		form =AuthenticationForm(data=request.POST)

		if form.is_valid():
			u= request.POST['username']
			p= request.POST['password']
			user = authenticate(username= u, password= p) 

			if user is not None:
				if user.is_active:
					login(request,user)

					acceso=User.objects.get(id=request.user.id)

					if str(acceso.empleado.cargo.departamento) == "Administrador" and str(acceso.empleado.estado)=="True":
						return HttpResponseRedirect(reverse('Inventory:admin'));

					elif str(acceso.empleado.cargo.departamento) == "Recursos Humanos" and str(acceso.empleado.estado)=="True":
						return HttpResponseRedirect(reverse('Inventory:recursosH'))

					elif str(acceso.empleado.cargo.departamento) == "Compras" and str(acceso.empleado.estado)=="True":
						return HttpResponseRedirect(reverse('Inventory:compras'))

					elif str(acceso.empleado.cargo.departamento) == "Informatica & Tecnologia" and str(acceso.empleado.estado)=="True":
						return HttpResponseRedirect(reverse('Inventory:IT'))
					else:
						return HttpResponseRedirect(reverse('home'))
				else:
					return HttpResponseRedirect(reverse('Inventory:login_form'))
		else: 
			return render(request, 'login_form.html',{'form': form})
			return HttpResponse('Formulario invalido')
	else:
		return HttpResponse('Debes utilizar el metodo POST')


def login_form(request):
	form = AuthenticationForm()
	return render(request,'login_form.html', {'form':form})



