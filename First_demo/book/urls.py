from django.urls import path
from .import views

urlpatterns = [
    # 此处的次url为空白，就对应book/
    path('',views.book, name = 'book'),
    path('detail/<book_id>/',views.book_detail, name = 'book_detail')
]