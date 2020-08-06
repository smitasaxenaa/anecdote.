from django.conf.urls import url, include
from resources.views import resources
urlpatterns = [
    url(r"", resources, name="resources"),

]
