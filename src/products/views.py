from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


# def product_create_view(request):
#     template = 'product_create.html'
#
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the date is good
#             print(my_form.cleaned_data)
#             Product.object.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, template, context)


def product_create_view(request):
    initial_data = {
        'title': "This is Awesome title"
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()
    template = 'product_create.html'
    context = {
        "form": form
    }
    return render(request, template, context)


def product_update_view(request, id=id):
    template = "product_create.html"
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        "form": form
    }
    return render(request, template, context)


def product_list_view(request):
    template = "product_list.html"
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template, context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    template = 'product_detail.html'
    context = {
        "object": obj
    }
    return render(request, template, context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    template = 'product_detail.html'
    context = {
        "object": obj
    }
    return render(request, template, context)


def product_delete_view(request, id):
    template = 'product_delete.html'
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    content = {
        "object": obj
    }
    return render(request, template, content)



