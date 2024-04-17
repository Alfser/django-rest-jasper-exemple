from rest_framework import routers

from .viewset import PessoaViewSet


routers = routers.DefaultRouter()
routers.register(r'pessoas', PessoaViewSet)