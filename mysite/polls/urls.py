from django.urls import path
from . import views # để liên kết url với view tương ứng, ta cần import views (from thư mục hiện tại, ta import views)

app_name = "polls"

urlpatterns = [
    path('<int:q_id>', views.vote, name="vote"),
    path('detail/<int:question_id>', views.viewDetail, name="view_detail"),
    path('list/', views.viewlist, name="view_list"),
    path('', views.index, name="index"),
]