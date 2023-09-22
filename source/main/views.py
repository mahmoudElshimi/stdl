from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewItem(forms.Form):
    item = forms.CharField(label="New Item")


class DelItem(forms.Form):
    item = forms.IntegerField(label="Item Num? ")


def index(request, name: str = ""):
    if "items" not in request.session:
        request.session["items"] = []

    return render(
        request,
        "main/index.html",
        {
            "items": request.session["items"],
        },
    )


def new_item(request):
    """Add a new item to items list"""
    if request.method == "POST":
        form = NewItem(request.POST)
        form.is_valid()
        item = form.cleaned_data["item"]
        request.session["items"] += [item]
        return HttpResponseRedirect(reverse("main:index"))

    return render(
        request,
        "main/new_item.html",
        {
            "form": NewItem,
        },
    )


def del_item(request):
    """Add a new item to items list"""
    if request.method == "POST":
        form = DelItem(request.POST)
        form.is_valid()
        item = form.cleaned_data["item"]
        request.session.modified = True
        items = request.session["items"]
        if item == 0:
            del request.session["items"]
        elif 0 < item <= len(items):
            items.pop(int(item - 1))
        else:
            return render(
                request,
                "main/del_item.html",
                {
                    "form": DelItem,
                    "error": item,
                },
            )

        return HttpResponseRedirect(reverse("main:index"))

    return render(
        request,
        "main/del_item.html",
        {
            "form": DelItem,
        },
    )
