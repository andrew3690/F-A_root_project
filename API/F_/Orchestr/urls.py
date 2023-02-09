from django.urls import path, include
from . import views
#from .views import LoginView,LogoutView, RunListView,RunCreateView,RunEditView,RunDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'orches'

urlpatterns= [
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),

    path('home/',views.RunListView.as_view(),name='home'),
    path('home/createrun/',views.RunCreateView.as_view(),name='create'),
    path('home/editrun/<int:pk>/',views.RunEditView.as_view(),name='edit'),
    path('home/deleterun/<int:pk>/',views.RunDeleteView.as_view(),name='delete')
]

urlpatterns += staticfiles_urlpatterns()