from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def page(request, title):
    if title in util.list_entries():
        entry_content = util.get_entry(title)
        html_content = markdown2.markdown(entry_content)
        return render(request, "encyclopedia/wikitemplate.html", {
            "content": html_content,
            "title": title
        })
    else:
        return render(request, "encyclopedia/404page.html")
def create(request):
    return render(request, "encyclopedia/create.html")