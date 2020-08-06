from django.conf.urls import url, include
from .views import( userposts_detail_view,
    userposts_list_view, dashboard)

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r'^posts/$', userposts_list_view, name='userposts_list_view'),
    url(r'^posts/(?P<url>\S+)/$', userposts_detail_view, name='userposts_detail_view'),
]
