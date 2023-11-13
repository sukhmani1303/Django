from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import testForm
from service.models import Service


def aboutUs(request):
    data  = {
        "title" : "about page",
        "arr" : [1,2,3,4,5]
             
             }
    


    return render(request, "about.html", data)

# def home(request):
#     return HttpResponse("<b>Home Page<b>")

def course_dynamic_link(request, blogid):
    return HttpResponse(f"SHowing blog with id : {blogid}")

def course_dynamic_link_strict(request, blogid):
    return HttpResponse(f"SHowing blog with id (int) : {blogid}")

def course_dynamic_link_slug(request, blogid):
    return HttpResponse(f"SHowing blog with id (slug) : {blogid}")

# render html template

def redirect(request):
    if request.method == "GET":
        output = request.GET.get("op1")
        print("output : ", output)
        return render(request, "redirected.html", {"data" : output})

def submitform(request):
    print("inside submitform")
    try:
        if request.method == "GET":
            email = request.GET.get("email")
            print("email : ", email)
            redurl = f'/redirect/?op1={email}'
            
            return HttpResponseRedirect(redurl)
    except:
        return render(request, "index.html")


def render_page__home(request):
    data  = {
        "title" : "home page",
        "arr" : [1,2,3,4,5]
             
             }

    return render(request, "index.html", data)

def data_dealing(request):
    data = Service.objects.all()

    return render(request, "data_dealing.html", {"output" : data} )

def form_data(request):
    try:
        if request.method == 'GET':
            # email = request.GET['email']
            # passw = request.GET['pass']

            email = request.GET.get('email')
            passw = request.GET.get('passw')

            print("email : ", email)

            data = {
                "val" : email
            }
            data["type"] = "GET"

            redurl = f'/redirect/?op={email}'
            return HttpResponseRedirect(redurl)
            
        elif request.method == 'POST':
            email = request.POST.get('email')
            passw = request.POST.get('passw')

            print("email : ", email)

            print("\npost hai")

            data = {
                "val" : email
            }
            data["type"] = "POST"

            redurl = f'/redirect/?op={email}'

            return HttpResponseRedirect(redurl)

    except:
        print("\n\nerror hai !!!")
        pass

    f1 = testForm()

    data['form'] = f1

    return render(request, "form.html", data)
