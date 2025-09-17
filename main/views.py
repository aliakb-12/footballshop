from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm


# Create your views here.
def show_main(request):
    product_list = Product.objects.exclude(id__isnull = True)   # Remove all null id
    context = {
        'app_name' : 'Man United Football Shop',
        'npm' : '2406495754',
        'name': 'Ali Akbar Murtadha',
        'class': 'PBP A',
        'product_list' : product_list,
    }

    return render(request, "main/main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "main/create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "main/product_detail.html", context)


def show_xml(request):
    pruduct_list = Product.objects.all()
    xml_data = serializers.serialize("xml", pruduct_list)
    return HttpResponse(xml_data, content_type = "application/xml")

def show_xml_by_id(request, product_id):
    try:
        pruduct_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", pruduct_list)
        return HttpResponse(xml_data, content_type = "application/xml")
    except:
        return HttpResponse(status=404)


def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type = "application/json")

def show_json_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        json_data = serializers.serialize("json", product_list)
        return HttpResponse(json_data, content_type = "application/json")
    except:
        return HttpResponse(status=404)


