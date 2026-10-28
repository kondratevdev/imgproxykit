from http import HTTPMethod

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from test_apps.django.server.serializers import ImageSerializer


def django_images(request: HttpRequest) -> HttpResponse:
    """Display an image URL and named image variants."""
    return render(
        request,
        'images.html',
        {'source': request.GET.get('source')},
    )


@api_view([HTTPMethod.GET])
def drf_images(request: Request) -> Response:
    """Return an image URL and named image variants."""
    serializer = ImageSerializer({'image': request.query_params.get('source')})
    return Response(serializer.data)  # pyright: ignore[reportUnknownMemberType]
