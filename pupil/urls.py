from django.urls import path
from .views import get_all,get_by_id

urlpatterns=[
    path("all/",get_all),
    path("<int:pupil_id>",get_by_id)
]