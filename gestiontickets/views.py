from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Especialidad, SoporteTI, Ticket

class EspecialidadCreateView(CreateView):
    model = Especialidad
    fields = ['nombre']
    template_name = 'especialidad_create.html'
    success_url = reverse_lazy('especialidad-list')

class SoporteCreateView(CreateView):
    model = SoporteTI
    fields = ['nombre', 'especialidades', 'imagen_perfil']
    template_name = 'soporte_create.html'
    success_url = reverse_lazy('soporte-list')

class TicketCreateView(CreateView):
    model = Ticket
    fields = ['titulo', 'descripcion', 'soporte']
    template_name = 'ticket_create.html'
    success_url = reverse_lazy('ticket-list')

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'

class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list.html'
    context_object_name = 'tickets'

class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ['titulo', 'descripcion', 'soporte']
    template_name = 'ticket_update.html'
    success_url = reverse_lazy('ticket-list')

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('ticket-list')

