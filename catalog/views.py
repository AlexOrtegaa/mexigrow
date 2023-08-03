from django.shortcuts import render
from django.views import generic

from .models import Proyect, ProyectInstance

# Create your views here.
def index(request):
    return render (request, 'index.html', context={})

class ProyectListView(generic.ListView):
    model = Proyect
    queryset = Proyect.objects.all()
    paginate_by = 10

class ProyectDetailView(generic.DetailView):
    model = Proyect

from django.contrib.auth.mixins import LoginRequiredMixin

class OwnedProyectsByUserListView(LoginRequiredMixin,generic.ListView):
    model = ProyectInstance
    template_name ='catalog/proyectinstance_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ProyectInstance.objects.filter(investor=self.request.user).order_by('date_acquired')
    
class OwnedProyectsByUserDetailView(LoginRequiredMixin,generic.DetailView):
    model = ProyectInstance
    template_name ='catalog/proyectinstance_detail_owned_user.html'
    paginate_by = 10
    context_object_name = 'pi'
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Proyect

from django.contrib.auth.mixins import PermissionRequiredMixin

class ProyectCreate(PermissionRequiredMixin, CreateView):
    model = Proyect
    fields = ['title','summary','mini_summary','company', 'date_published', 'expected_interest_rate']
    initial={'date_published':'01/01/2024'}
    permission_required = 'catalog.can_add_proyects'


class ProyectUpdate(PermissionRequiredMixin, UpdateView):
    model = Proyect
    fields = ['title','summary','mini_summary','company', 'date_published', 'expected_interest_rate']
    permission_required = 'catalog.can_add_proyects'

class ProyectDelete(PermissionRequiredMixin, DeleteView):
    model = Proyect
    success_url = reverse_lazy('proyects')
    permission_required = 'catalog.can_add_proyects'



class ProyectInstanceCreate(PermissionRequiredMixin, CreateView):
    model = ProyectInstance
    fields = ['id','proyect','date_acquired','date_of_end_contract', 'investment', 'investor']
    initial={'date_acquired':'01/01/2024', 'date_of_end_contract': '01/01/2024'}
    permission_required = 'catalog.can_add_instance_proyect'

class ProyectInstanceUpdate(PermissionRequiredMixin, UpdateView):
    model = ProyectInstance
    fields = ['id','proyect','date_acquired','date_of_end_contract', 'investment', 'investor']
    permission_required = 'catalog.can_add_instance_proyect'

class ProyectInstanceDelete(PermissionRequiredMixin, DeleteView):
    model = ProyectInstance
    success_url = reverse_lazy('proyects')
    permission_required = 'catalog.can_add_instance_proyect'