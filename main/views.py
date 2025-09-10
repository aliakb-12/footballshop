from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Man United Football Shop',
        'npm' : '2406495754',
        'name': 'Ali Akbar Murtadha',
        'class': 'PBP A'
    }

    return render(request, "main/main.html", context)