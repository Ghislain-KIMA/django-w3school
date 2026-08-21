from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Member



ROOT_TEMPLATE = "members"



def members(request):
    context = {
        "mymembers": Member.objects.all()
    }
    return render(request, f"{ROOT_TEMPLATE}/all_members.html", context)


def details(request, id):
    context = {
        "mymember": get_object_or_404(Member, pk=id)
    }
    return render(request, f"{ROOT_TEMPLATE}/details.html", context)


def main(request):
    return render(request, f"{ROOT_TEMPLATE}/main.html")


def testing(request):
    context = {
        'mymembers': Member.objects.all().values(),
    }
    return render(request, 'template.html', context)
