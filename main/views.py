from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245876',
        'name': 'Nabilah Devina Mumin',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
