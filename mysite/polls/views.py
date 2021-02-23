from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Dùng để viết ra giao diện
# Hàm index hiển thị câu "Hello everyone!"
def index(request):
    myname = "Dev For U"
    items = ["Phone", "Laptop", "Motobike"]
    context = {"name": myname, "items": items}
    return render(request, "polls/index.html", context)