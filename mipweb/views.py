from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'mipweb/home.html')

def csi_jump(request):
    return render(request, 'mipweb/csi-jump.html')

def iac_stds(request):
    return render(request, 'mipweb/iac-stds-smart-grids.html')

def team(request):
    return render(request, 'mipweb/mip-team.html')

def partnership(request):
    return render(request, 'mipweb/partnership.html')

def donor(request):
    return render(request, 'donor/donor-register.html')

def lifelinenets(request):
    return render(request, 'mipweb/lifelinenets.html')

def research(request):
    return render(request, 'mipweb/research.html')
