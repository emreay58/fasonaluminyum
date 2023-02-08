from django.urls import path
from . import views

urlpatterns = [
    path('', views.Indexview, name='index'),
    path('hizmetler/', views.ServicesView, name='services'),
    path('hizmetler/<slug:slug>/', views.Service_Detail, name='service_detail'),
    path('hakkimizda/', views.AboutView, name='about'),
    path('iletisim/', views.ContactView, name='contact'),
    path('projeler/', views.ProjectView, name ='project'),
    path('projeler/<slug:slug>', views.Project_Detail, name='project_detail'),
    path('kategori/<slug:slug>/', views.CategoryView, name='category'),
    path('etiket/<slug:slug>/', views.TagView, name='tag'),
]
