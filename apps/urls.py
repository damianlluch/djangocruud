from django.urls import include, path
from django.contrib import admin

from theme import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books_fbv_user/', include('books_fbv_user.urls', namespace='books_fbv_user')),
    path('', views.home),
]
