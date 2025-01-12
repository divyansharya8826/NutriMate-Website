from curses import BUTTON1_CLICKED
from django.shortcuts import render

# dic = {
#     'keto' : '/services/diet/#keto',
#     'mediterranean' : '/services/diet/#mediterranean',
#     'protein' : '/services/diet/#protein',
#     'fiber' : '/services/diet/#fiber',
# }

# Create your views here.
def diet(request):
    return render(request, "diets.html")
    # return HttpResponse("Hello, world. You're at the diet page.")


def exercise(request):
    return render(request, "exercises.html")
    # return HttpResponse("Hello, world. You're at the exercise page.")


def planning(request):
    return render(request, "planning.html")
    # return HttpResponse("Hello, world. You're at the planning page.")

# def onClick(request):
#     if request.POST.get('keto'):
#         return render(request, "diets.html", {'keto':dic['keto']})
#     return render(request, "diets.html")