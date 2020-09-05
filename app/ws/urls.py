from django.urls import path
from django.contrib import admin
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view

from ws.views import ValueList, ValueDetail

schema_view = get_swagger_view(title='VALUE ARRAY WEB API')


urlpatterns = [
    path('front/betsy/irish/embargo/admin/', admin.site.urls),

    # Swagger API
    path(
        'api/',
        schema_view,
        name='api_array'
    ),

    # tree
    path(
        'value_array/',
        ValueList.as_view(),
        name=ValueList.name
    ),
    re_path(
        '^value_array/(?P<pk>[0-9]+)/$',
        ValueDetail.as_view(),
        name=ValueDetail.name
    ),
]