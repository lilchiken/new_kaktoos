from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from recension.models import Recension


def create_page_obj_from_paginator(queryset, request):
    return Paginator(queryset, 1).get_page(request.GET.get('page'))


def index(request):
    first = Recension.objects.first()
    all_recensions = Recension.objects.all()
    page_obj = create_page_obj_from_paginator(all_recensions, request)
    return render(request, 'recensions/index.html', {'page_obj': page_obj})


def single(request, rec_id):
    rec = get_object_or_404(Recension, id=rec_id)
    return render(request, 'recensions/single.html', {'rec': rec})
