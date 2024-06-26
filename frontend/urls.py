from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('login/', index),
    path('register/', index),
    path('dashboard/', index),
    path('book/<int:bookId>', index),
    path('editor/<int:bookId>', index)
]