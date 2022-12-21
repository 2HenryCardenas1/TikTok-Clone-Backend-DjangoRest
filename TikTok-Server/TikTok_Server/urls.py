"""TikTok_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from comment.api.routes import router_comment
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from video.api.routes import router_video

schema_view = get_schema_view(
    openapi.Info(
        title="TikTok API",
        default_version='v1',
        description="API for TikTok-Clone",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cardenashenryesteban@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc'),

    # Router de users
    path('api/', include('users.api.router')),
    # Router de videos
    path('api/', include(router_video.urls)),
    # Router de comments
    path('api/', include(router_comment.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
