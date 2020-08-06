from django.conf.urls import url, include
from profiles.views import sde, businessanalyst
urlpatterns = [
    url(r"sde", sde, name="sde"),
    url(r"businessanalyst", businessanalyst, name="businessanalyst"),
]
