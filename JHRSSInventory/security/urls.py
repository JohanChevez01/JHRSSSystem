from django.conf.urls import url
from . import views

# /security/ 

app_name='security'

urlpatterns =[
	url(r'^loginform/', views.login_form, name='login_form'),
	url(r'^login/$', views.log_in, name='log_in'),
	url(r'^logout/$', views.log_out, name='log_out'),
]