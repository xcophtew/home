from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.pt')
def home_view(request):
    return {'project': 'Arch Byte'}

