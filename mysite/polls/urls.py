from django.urls import path
from . import views # để liên kết url với view tương ứng, ta cần import views (from thư mục hiện tại, ta import views)

urlpatterns = [
    path('welcome/', views.func_1, name="func_1"),
    path('', views.index, name="index"),
]