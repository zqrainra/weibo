from django.conf.urls import url
import views

urlpatterns = [
    url(r'^change_profile/', views.change_profile,name='change_profile'),
    url(r'^show_acount/', views.show_acount,name='show_acount'),
]