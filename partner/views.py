from django.shortcuts import render

# Create your views here.

def partner_register(request):
    return render(request, 'partner/partner_register.html')