from django.urls import path
from . import views # để liên kết url với view tương ứng, ta cần import views (from thư mục hiện tại, ta import views)

urlpatterns = [
    path('list/', views.viewlist, name="view_list"),
    path('', views.index, name="index"),
]