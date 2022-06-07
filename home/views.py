from django.shortcuts import render
import datetime

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    today = datetime.datetime.now().date()
    return render(request, "index.html", {"today": today})