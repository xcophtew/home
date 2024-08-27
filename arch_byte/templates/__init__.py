from pyramid.config import Configurator
from pyramid.response import Response

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
