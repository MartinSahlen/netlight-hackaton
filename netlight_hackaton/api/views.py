from rest_framework.decorators import api_view


@api_view()
def shit(request):
    return Response({'shit': 'YO'})
