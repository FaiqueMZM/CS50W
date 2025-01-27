from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("faique/", views.faique, name="faique"),
    path("inaas/", views.inaas, name="inaas"),
    path("<str:name>/", views.greet, name="greet"),
]