from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Dùng để viết ra giao diện
# Hàm index hiển thị câu "Hello everyone!"
def index(request):
    return HttpResponse("Hello everyone!")