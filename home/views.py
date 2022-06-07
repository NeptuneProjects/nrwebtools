from django.shortcuts import render

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    # today = datetime.datetime.now().date()
    # context = {"today": today}
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")