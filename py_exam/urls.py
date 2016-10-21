from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.main_handler.urls', namespace="surface")),
    url(r'^user/', include('apps.login_reg.urls', namespace="user")),
    url(r'^travels/', include('apps.travels.urls', namespace="travels")),
]
