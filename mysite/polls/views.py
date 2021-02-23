from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
# Dùng để viết ra giao diện
# Hàm index hiển thị câu "Hello everyone!"
def index(request):
    myname = "Dev For U"
    items = ["Phone", "Laptop", "Motobike", "Money"]
    context = {"name": myname, "items": items}
    return render(request, "polls/index.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"list_question": list_question}
    return render(request, "polls/question_list.html", context)