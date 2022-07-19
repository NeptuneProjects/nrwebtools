from django.shortcuts import render

TEMPLATE_DIRS = 'os.path.join(BASE_DIR, "templates")'

def ruadparserapp(request):
    return render(request, "ruadparserapp.html")
