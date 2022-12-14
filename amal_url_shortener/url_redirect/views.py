from django.shortcuts import render, redirect
from django.http import Http404

from .models import Urls
from .forms import urlForm
import datetime
from . import link_gen
from . import qr_gen

def go(request):
    return redirect('Dashboard')

# Create your views here.
def dashboard(request):
    if request.method == 'POST':
        url = request.POST['url']
        print(url)
        form = urlForm(request.POST)
        if form.is_valid():
            short_code = link_gen.random_string()
            list_urls = Urls.objects.values_list('url_short', flat=True)
            while short_code in list_urls:
                short_code = link_gen.random_string()
            new_entry = Urls(url=url,url_short=short_code, pub_date=datetime.datetime.now())
            new_entry.save()
            #qr code part
            print("yes")
            url_domain_path = str(request.build_absolute_uri('/r/')) + str(short_code)
            print(url_domain_path)
            qr_gen.generate_qr(url_domain_path, short_code)
        
        return redirect('Dashboard')
    else:
        form = urlForm()
        info = Urls.objects.all()
        return render(request, 'url_redirect/dashboard.html', {'form': form,"urls":info})

def short_link_edit(request, id):
    if request.method == 'POST':
        urls_obj = Urls.objects.get(url_short=id)
        print("MADE IT")
        new_short_code = request.POST['edit_short']
        print(new_short_code)
        list_urls = Urls.objects.values_list('url_short', flat=True)
        if new_short_code in list_urls:
            #IMPLEMENT ERROR MESSAGE
            return redirect('Dashboard')
        else:
            urls_obj.url_short = new_short_code
            urls_obj.save()
            url_domain_path = str(request.build_absolute_uri('/r/')) + str(new_short_code)
            qr_gen.generate_qr(url_domain_path, new_short_code)
            print("HERE")
            print(url_domain_path)
            print(id)
            qr_gen.delete_qr(id)
            return redirect('Dashboard')
        
            
def page_redirect(request, id):
    #from database get url matching id, if not found 404 not found
    try:
        urls_obj = Urls.objects.get(url_short=id)
        url = urls_obj.url
    except:
        return Http404('Page does not exist')
    # redirect to url
    urls_obj.visits += 1
    urls_obj.save()
    return redirect(url)

