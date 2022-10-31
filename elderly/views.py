from django.shortcuts import render

def elderaccount(request):
    return render(request, 'elderly/elderAccountLogin.html')