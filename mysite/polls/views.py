from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Dùng để viết ra giao diện
# Hàm index hiển thị câu "Hello everyone!"
def index(request):
    return HttpResponse("Hello everyone!")

def func_1(request):
    return HttpResponse("<h1>Welcome to DevForU</h1><div>I'm ThinhTPT, a web developer</div>")