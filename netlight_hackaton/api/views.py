from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def get_shit(request):
    return Response({'shit': 'YO'})
