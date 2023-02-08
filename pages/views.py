from django.shortcuts import render
from .models import ServicesModel,Category,Tag,ProjectModel, ContactModel

# Create your views here.

def Indexview(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        subject = request.POST['subject']
        message = request.POST['message']

        mesaj = ContactModel(name=name, email=email, tel=tel, subject=subject, mesaj=message)
        mesaj.save()

        return render(request, 'pages/contact.html', {'kayit' : 'Mesajınız başarılı bir şekilde oluşturuldu. En yakın zamanda sizinle irtibata geçeceğiz.'})
    

    services = ServicesModel.objects.all()
    projects = ProjectModel.objects.filter(is_home=True)
   
    context = {
        'services' : services,
        'projects' : projects,
     }
    return render(request, 'pages/index.html', context)


def ServicesView(request):
    services = ServicesModel.objects.all()
    projects = ProjectModel.objects.all()

    context = {
        'services' : services,
        'projects' : projects
    }
    return render(request, 'pages/services.html', context)


def Service_Detail(request,slug):
    service = ServicesModel.objects.get(slug=slug)
    services = ServicesModel.objects.all()

    context = {
        'services' : services,
        'service' : service
    }
    return render(request, 'pages/service_detail.html',context)


def AboutView(request):
    services = ServicesModel.objects.all()
    context = {
        'services' : services
    }
    return render(request, 'pages/about.html', context)


def ContactView(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        subject = request.POST['subject']
        message = request.POST['message']

        mesaj = ContactModel(name=name, email=email, tel=tel, subject=subject, mesaj=message)
        mesaj.save()

        return render(request, 'pages/contact.html', {'kayit' : 'Mesajınız başarılı bir şekilde oluşturuldu. En yakın zamanda sizinle irtibata geçeceğiz.'})

    services = ServicesModel.objects.all()
    context = {
        'services' : services
    }
    return render(request, 'pages/contact.html', context)


def ProjectView(request):
    projects = ProjectModel.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    services = ServicesModel.objects.all()

    context = {
        'projects' : projects,
        'tag' : tag,
        'category' : category,
        'services' : services
    }
    return render(request, 'pages/projects.html', context)


def Project_Detail(request, slug):
    projects = ProjectModel.objects.all()
    proje = ProjectModel.objects.get(slug=slug)

    context = {
        'projects' : projects,
        'proje' : proje
    }
    return render(request, 'pages/project_detail.html', context)

def CategoryView(request, slug):
    category = Category.objects.filter(category__slug=slug)
    projects = ProjectModel.objects.all()
    tag = Tag.objects.all()
    
    context = {
        'category' : category,
        'tag' : tag,
        'projects' : projects
    } 
    return render(request, 'pages/projects.html', context)

def TagView(request, slug):
    tag = Tag.objects.filter(tag__slug=slug)
    category = Category.objects.all()
    projects = ProjectModel.objects.all()
    
    context = {
        'tag' : tag,
        'category' : category,
        'projects' : projects
    } 
    return render(request, 'pages/projects.html', context)