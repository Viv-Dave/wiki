from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def page(request, title):
    if title in util.list_entries():
        return render(request, "encyclopedia/wikitemplate.html")
    elif title not in util.list_entries():
        return render(request, "encyclopedia/404page.html")
def create(request):
    return render(request, "encyclopedia/create.html")