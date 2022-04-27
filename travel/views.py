from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone

# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        header = 'Travel Service Agency'
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['header'] = header
        context['now'] = timezone.now()
        return context
    
class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        header = 'Travel Service Agency'
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['header'] = header
        context['now'] = timezone.now()
        return context
    
class ServiceView(TemplateView):
    template_name = 'services.html'
    
    def get_context_data(self, **kwargs):
        header = 'Travel Service Agency'
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['header'] = header
        context['now'] = timezone.now()
        return context
    
class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        header = 'Travel Service Agency'
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['header'] = header
        context['now'] = timezone.now()
        return context