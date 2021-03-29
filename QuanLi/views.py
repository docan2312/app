from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import Post_DonVi, Post_CongDoan, Post_Tour, Post_Login, Post_DK, CongDoan_Post, Tour_Post, DV_Post, CreateUser
from django.contrib import auth, messages
from django.contrib.auth import logout, login, authenticate
from .filters import Detail_CongDoanVienFilter, CongDoanVienFilter, TourFilter
def home(request):
    donvi = DonVi.objects.all()
    tour = Tour.objects.all()
    cdv = CongDoanVien.objects.all()
    total_donvi = donvi.count()
    total_tour = tour.count()
    total_cdv = cdv.count()
    context = {
        'donvi': donvi,
        'tour': tour,
        'total_donvi': total_donvi,
        'total_tour': total_tour,
        'total_cdv': total_cdv,
    }
    return render(request, 'QuanLi/dashboard.html', context)
###########################################################
def detail_DV(request, pk_donvi):
    donvi = DonVi.objects.get(id=pk_donvi)
    congdoan = donvi.congdoanvien_set.all()
    total_congdoan = congdoan.count()

    myFilter = Detail_CongDoanVienFilter(request.GET, queryset=congdoan)
    congdoan = myFilter.qs

    context = {
        'donvi': donvi,
        'total_congdoan': total_congdoan,
        'congdoan': congdoan,
        'myFilter': myFilter
    }
    return render(request, 'QuanLi/deital_DV.html', context)

def create_DV(request):
    form_dv = Post_DonVi()
    return render(request, 'QuanLi/Create_DV.html', {'form_dv': form_dv})

def save_DV(request):
    if request.method == 'POST':
        q = Post_DonVi(request.POST)
        if q.is_valid():
            q.save()
            return render(request, 'QuanLi/save_DV.html', {'form': q})
        else:
            return render(request, 'QuanLi/error_createDV.html')
    else:
        return HttpResponse("khong phai post")

def update_DV(request, id=None):
    instance = get_object_or_404(DonVi, id=id)
    form = DV_Post(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        instance.save()
        return render(request, 'QuanLi/save_DV.html')
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, 'QuanLi/update_DV.html', context)

def del_DV(request, id):
    xoa = DonVi.objects.get(id=id)
    return render(request, 'QuanLi/xoa_DV.html', {'xoa': xoa})

def save_del_DV(request, id):
    if request.method == "POST":
        xoa = DonVi.objects.get(id=id)
        xoa.delete()
        return render(request, 'QuanLi/save_DV.html')
##########################################################################
def CDV(request):
    donvi = DonVi.objects.all()
    total_dv = donvi.count()
    cdv = CongDoanVien.objects.all()
    total_cdv = cdv.count()
    myFilter = CongDoanVienFilter(request.GET, queryset=cdv)
    cdv = myFilter.qs
    context = {
        'donvi': donvi,
        'total_dv': total_dv,
        'cdv': cdv,
        'total_cdv': total_cdv,
        'myFilter': myFilter
    }
    return render(request, 'QuanLi/CongDoanVien.html', context)

def create_CDV(request):
    form = Post_CongDoan()
    return render(request, 'QuanLi/Create_CDV.html', {'form': form})

def save_CDV(request):
    if request.method == 'POST':
        q = Post_CongDoan(request.POST, request.FILES)
        if q.is_valid():
            q.save()
            return render(request, 'QuanLi/save_CDV.html')
        else:
            return render(request, 'QuanLi/error_CDV.html')

def del_CDV(request, id):
    xoa = CongDoanVien.objects.get(id=id)
    return render(request, 'QuanLi/xoa_CDV.html', {'xoa': xoa})

def save_del_CDV(request, id):
    if request.method == "POST":
        xoa = CongDoanVien.objects.get(id=id)
        xoa.delete()
        return render(request, 'QuanLi/save_CDV.html')

def update_CDV(request, id):
    instance = get_object_or_404(CongDoanVien, id=id)
    form = CongDoan_Post(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        instance.save()
        return render(request, 'QuanLi/save_CDV.html')
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, 'QuanLi/update_CDV.html', context)
###########################################################
def tour(request):
    tour = Tour.objects.all()
    total_tour = tour.count()
    dki = DKTour.objects.all()
    total_dki = dki.count()

    myFilter = TourFilter(request.GET, queryset=tour)
    tour = myFilter.qs
    context = {
        'tour': tour,
        'total_tour': total_tour,
        'total_dki': total_dki,
        'myFilter': myFilter
    }
    return render(request, 'QuanLi/Tour.html', context)

def create_tour(request):
    form = Post_Tour()
    return render(request, 'QuanLi/create_Tour.html', {'form': form})

def save_tour(request):
    if request.method == 'POST':
        q = Post_Tour(request.POST, request.FILES)
        if q.is_valid():
            q.save()
            return render(request, 'QuanLi/save_Tour.html')
        else:
            return render(request, 'QuanLi/error_Tour.html')

def detail_tour(request,id):
    detail = Tour.objects.get(id=id)
    dk = detail.dktour_set.all()
    total_dk = dk.count()
    context = {
        'tour': detail,
        'total_dk': total_dk
    }
    return render(request, 'QuanLi/detail_tour.html', context)

def del_tour(request, id):
    xoa = Tour.objects.get(id=id)
    return render(request, 'QuanLi/xoa_Tour.html', {'xoa': xoa})

def save_del_tour(request, id):
    if request.method == "POST":
        xoa = Tour.objects.get(id=id)
        xoa.delete()
        return render(request, 'QuanLi/save_Tour.html')

def update_Tour(request, id=None):
    instance = get_object_or_404(Tour, id=id)
    form = Tour_Post(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        instance.save()
        return render(request, 'QuanLi/save_Tour.html')
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, 'QuanLi/update_Tour.html', context)
#############################################################

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'QuanLi/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def register_Account(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was create for ' + user)
            return redirect('login')
    return render(request, 'QuanLi/registerAccount.html', {'form': form})
#######################################
def register_tour(request):
    form = Post_DK()
    return render(request, "QuanLi/register_Tour.html", {'form': form})

def save_register(request):
    if request.method == 'POST':
        q = Post_DK(request.POST, request.FILES)
        if q.is_valid():
            q.save()
            return render(request, 'QuanLi/save_Tour.html')
        else:
            return render(request, 'QuanLi/Error.html')

def del_dktour(request, id):
    xoa = DKTour.objects.get(id=id)
    return render(request, 'QuanLi/xoa_DKTour.html', {'xoa': xoa})

def save_del_DKtour(request, id):
    if request.method == "POST":
        xoa = DKTour.objects.get(id=id)
        xoa.delete()
        return render(request, 'QuanLi/save_Tour.html')