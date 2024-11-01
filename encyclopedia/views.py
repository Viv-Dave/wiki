from django.shortcuts import render, redirect
import markdown2
from . import util
from random import choice
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
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title in util.list_entries():
            return render(request, "encyclopedia/create.html", {
                "error": "An entry with this title already exists.",
                "title": title,
                "content": content
            })
        util.save_entry(title, content)
        return redirect("pages", title=title)

    return render(request, "encyclopedia/create.html")

def random(request):
    random_entry = choice(util.list_entries())
    html_content = markdown2.markdown(util.get_entry(random_entry))
    return render(request, "encyclopedia/wikitemplate.html", {
        "content":html_content,
        "title": random_entry
    })
