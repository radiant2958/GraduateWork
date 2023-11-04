from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about-us'),
    path('success/', views.success_page, name='success_page'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.new, name='new')
]
