from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='index.pt')
def home_view(request):
    return {'project': 'Arch Byte'}

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
