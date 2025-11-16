from django.contrib import admin
from django.urls import path
from vehiclesapp.views import create_view, list_view, update_view, delete_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # LISTA PRINCIPAL
    path('', list_view),

    # CREATE
    path('create/', create_view),

    # UPDATE
    path('update/<int:id>/', update_view),

    # DELETE
    path('delete/<int:id>/', delete_view),
]
