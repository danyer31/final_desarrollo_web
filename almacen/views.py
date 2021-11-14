from django.db import models
from django.urls.base import reverse
from .models import Cliente, Venta
from django.views.generic import DetailView, ListView
from django.views.generic.edit import (CreateView, DeleteView, UpdateView)


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = '__all__'
    success_url = 'cliente'

    def get_success_url(self):
        return reverse('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = '__all__'
    success_url = 'cliente'

    def get_success_url(self):
        return reverse('cliente_detail', kwargs={'pk': self.kwargs['pk']})

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_delete.html'
    fields = '__all__'
    success_url = 'cliente'

    def get_success_url(self):
        return reverse('cliente_list')

class VentaListView(ListView):
    model = Venta
    template_name = 'venta_list.html'

class VentaDetailView(DetailView):
    model = Venta
    template_name = 'venta_detail.html'

class VentaCreateView(CreateView):
    model = Venta
    template_name = 'venta_form.html'
    fields = '__all__'
    success_url = 'venta'

    def get_success_url(self):
        return reverse('venta_list')

class VentaUpdateView(UpdateView):
    model = Venta
    template_name = 'venta_form.html'
    fields = '__all__'
    success_url = 'venta'

    def get_success_url(self):
        return reverse('venta_detail', kwargs={'pk': self.kwargs['pk']})

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'venta_delete.html'
    fields = '__all__'
    success_url = 'venta'

    def get_success_url(self):
        return reverse('venta_list')