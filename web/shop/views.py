from rest_framework import generics
from django.shortcuts import render, redirect
from .models import Mobiletechnic, Category
from .serializers import ShopSerializer
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm
from .tasks import send_spam_email
from .service import send

class ShopAPIView(generics.ListAPIView):
    queryset = Mobiletechnic.objects.all()
    serializer_class = ShopSerializer


def index(request):
    return render(request, 'index.html')


def allproducts(request):
    products = Mobiletechnic.objects.all()
    return render(request, 'allproducts.html', {'products': products})


def addtobusket(request, id):
    product = Mobiletechnic.objects.get(id=id)
    if request.session.get("busket", False):
        if request.session.get("busket").get(str(id), False):
            request.session["busket"][str(id)] += 1
        else:
            request.session["busket"][str(id)] = 1
    else:
        request.session["busket"] = {str(id): 1}

    request.session.save()  # Сохранение изменений сессии

    print("Корзина", id, request.session.get("busket"))

    return redirect('allproducts')


def busket(request):
    busket = request.session.get("busket", {})
    busket = [
        {
            "product": Mobiletechnic.objects.get(id=id),
            "count": count
        } for id, count in busket.items()]
    total_count = sum([item["count"] for item in busket])
    return render(request, 'busket.html', {'busket': busket, "total_count": total_count})


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)