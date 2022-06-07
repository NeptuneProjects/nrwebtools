from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Block29
from .forms import Block29Form

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)


class Block29View(TemplateView):
    template_name = 'block29.html'

    def get(self, request):
        form = Block29Form()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = Block29Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            formatted = Block29.format(data)
        context = {'form': form, 'data': data, 'formatted': formatted}
        return render(request, self.template_name, context)
