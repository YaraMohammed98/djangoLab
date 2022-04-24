from django.urls import path
from .views import index,new,edit,delete
from .views import book
from .views import author


urlpatterns = [
    path('',index , name="home"),
    path('new',new,name="create_book"),
    path('<int:book_id>', book, name="book_info"),
    path('<int:book_id>/edit', edit, name="book_edit"),
    path('<int:book_id>/delete', delete, name="book_delete"),


    path('author/<int:author_id>',author,name="author_info")
]
