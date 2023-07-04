from django.urls import path
from .views import EspecialidadCreateView, SoporteCreateView, TicketCreateView, TicketDetailView, TicketListView, TicketUpdateView, TicketDeleteView

urlpatterns = [
    path('especialidad/create/', EspecialidadCreateView.as_view(), name='especialidad-create'),
    path('soporte/create/', SoporteCreateView.as_view(), name='soporte-create'),
    path('ticket/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/', TicketListView.as_view(), name='ticket-list'),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket-update'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket-delete'),
]