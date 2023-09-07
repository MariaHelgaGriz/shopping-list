from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Maria Helga Grizelda',
        'class': 'PBD KI'
    }

    return render(request, 'main.html', context)