from django.urls import include, path
from rest_framework import routers
from quickstart import views as quickstart_views
from django.contrib import admin
from snippets import views as snippets_views

router = routers.DefaultRouter()

router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)

router.register(r'snippets', snippets_views.SnippetViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('snippets.urls')),

]

