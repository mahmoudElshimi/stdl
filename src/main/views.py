from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Items


class NewItem(forms.Form):
    item = forms.CharField(label="New Item")


class DelItem(forms.Form):
    item = forms.IntegerField(label="Item Num? ")


def index(request, name: str = ""):
    """Print All Items"""
    all_items = [i[1] for i in Items.objects.values_list()]
    return render(
        request,
        "main/index.html",
        {
            "items": all_items,
        },
    )


def new_item(request):
    """If method is post:
        Extract The Item From The HttpResponse && Create A New One.
    else:
        View The Form For Creating A New Item.
    """
    if request.method == "POST":
        form = NewItem(request.POST)
        form.is_valid()
        item = Items(item=form.cleaned_data["item"])
        item.save()
        return HttpResponseRedirect(reverse("main:index"))

    return render(
        request,
        "main/new_item.html",
        {
            "form": NewItem,
        },
    )


def del_item(request):
    """If method is post:
        Extract The Item's Num From The HttpResponse && Get Its Id Then Delete
        Its Object && If Num==0: Delete All Objects.
    else:
        View The Form For Deleting An Item.
    """
    all_items = Items.objects.values_list()
    if request.method == "POST":
        form = DelItem(request.POST)
        form.is_valid()
        item = form.cleaned_data["item"]

        if item == 0:
            Items.objects.all().delete()

        elif 0 < item <= len(all_items):
            """ Check For Boundaries. """
            item -= 1
            Items.objects.get(id=all_items[item][0]).delete()

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



def test(request, name: str = ""):
    return HttpResponse("Django Is Running OK!")
