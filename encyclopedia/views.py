from django.shortcuts import render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    entryPage = util.get_entry(name)
    if entryPage is not None: 
        return render(request, "encyclopedia/entry.html", {
            "entry":markdown.markdown(entryPage),
            "name":name
        })
    return render(request, "encyclopedia/none.html",{
        "name":name
    })

""" def search(request, entryname):
    entryPage = util.get_entry(entryname)
    if entryPage is None:
        return render(request, "encyclopedia/searchResult.html", {
            "title": util.list_entries()
        })
    else:
         return render(request, "encyclopedia/searchResult.html", {
            "title": util.list_entries()
        }) """


