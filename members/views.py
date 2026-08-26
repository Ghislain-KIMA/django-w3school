from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member


TEMPLATE_DIR = "members"


def members(request):
    context = {
        "mymembers": Member.objects.all()
    }
    return render(request, f"{TEMPLATE_DIR}/members.html", context)


def member(request, slug):
    context = {
        "mymember": get_object_or_404(Member, slug=slug)
    }
    return render(request, f"{TEMPLATE_DIR}/member.html", context)


def main(request):
    return render(request, f"{TEMPLATE_DIR}/home.html")


def testing(request):
    context = {
        'mymembers': Member.objects.all().values(),
    }
    return render(request, 'template.html', context)
