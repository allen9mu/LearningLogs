#for users

from django.conf.urls import url
from django.contrib.auth.views import login

from users import views

urlpatterns =[
    #for login
    url (r'^login/$',login,{'template_name':'users/login.html'},name = 'login'),
    #for logout
    url (r'^logout/$',views.logout_view,name = 'logout'),
    #for registe
    url (r'^registe/$',views.register,name = 'register'),    
    
]
