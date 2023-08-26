from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Url, User
from . import link_gen
from . import qr_gen

# Create your views here.
def index(request):
    return redirect('Dashboard')

# Create your views here.
def dashboard(request):
    print(request.method)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        url = request.POST['url']
        print(url)
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        
        short_code = link_gen.random_string()
        new_entry = Url(user=request.user ,url=url,url_short=short_code, pub_date=timezone.now())
        while not new_entry.test_unique_short():
            new_entry = Url(user=request.user ,url=url,url_short=short_code, pub_date=timezone.now())
            short_code = link_gen.random_string()
        
        url_domain_path = str(request.build_absolute_uri('/r/')) + str(short_code)
        qr_gen.generate_qr(url_domain_path, short_code)
        
        new_entry.save()

        return redirect('Dashboard')
    else:
        info = Url.objects.filter(user=request.user.id)
        paginator = Paginator(info, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        err_msg = request.session.get('err_msg', '')
        request.session['err_msg'] = ''
        
        return render(request, 'url_redirect/dashboard.html', {"urls":page_obj, "err_msg":err_msg})

def short_link_edit(request, id):
    if request.method == 'POST':
        urls_obj = Url.objects.get(url_short=id)
        new_short_code = request.POST['edit_short']
        list_urls = Url.objects.values_list('url_short', flat=True)
        if new_short_code in list_urls:
            #IMPLEMENT ERROR MESSAGE
            request.session['err_msg'] = "Short code already exists"
            return redirect('Dashboard')
        else:
            urls_obj.url_short = new_short_code
            urls_obj.save()
            url_domain_path = str(request.build_absolute_uri('/r/')) + str(new_short_code)
            qr_gen.generate_qr(url_domain_path, new_short_code)
            qr_gen.delete_qr(id)
            return redirect('Dashboard')
        
            
def page_redirect(request, id):
    #from database get url matching id, if not found 404 not found
    try:
        urls_obj = Url.objects.get(url_short=id)
        url = urls_obj.url
    except:
        return Http404('Page does not exist')
    # redirect to url
    urls_obj.visits += 1
    urls_obj.save()
    return redirect(url)

def short_link_delete(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    urls_obj = Url.objects.get(url_short=id)
    if urls_obj.user != request.user:
        return redirect('Dashboard')
    urls_obj.delete()
    qr_gen.delete_qr(id)
    return redirect('Dashboard')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Dashboard"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")
    
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST["email"]

        password_confirm = request.POST['password_confirm']
        
        if password != password_confirm:
            return render(request, 'register.html', {
                "message": "Passwords must match."
            })
        
        try:
            user = User.objects.create_user(username, email=email, password=password)
            user.save()
        except:

            return render(request, 'register.html', {
                "message": "Username already taken."
            })
        
        login(request, user)
        return redirect('Dashboard')
    else:
        return render(request, 'register.html')