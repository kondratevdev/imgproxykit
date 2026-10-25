from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def images(request: HttpRequest) -> HttpResponse:
    """Display an image URL and named image variants."""
    return render(
        request,
        'images.html',
        {'source': request.GET.get('source')},
    )
