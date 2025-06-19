from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/index.html"
    title = "Welcome to Road Transport System"   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        
        return context