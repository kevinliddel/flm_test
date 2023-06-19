from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        'title': "Fiangonana Loterana Malagasy",
    }
    return render(request, 'statistic/index.html', context)