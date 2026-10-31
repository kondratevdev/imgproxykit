from urllib.parse import urljoin

from django.db.models.fields.files import FieldFile


def resolve_image_source(source: str | FieldFile) -> str:
    """Return an absolute source URL for a string or model file field."""
    url = source.url if isinstance(source, FieldFile) else source
    return urljoin('https://media.example.com/', url)  # (1)!


print(resolve_image_source('/media/photo.jpg'))
print(resolve_image_source('https://storage.example.com/photo.jpg'))
