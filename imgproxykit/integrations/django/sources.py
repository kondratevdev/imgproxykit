from django.db.models.fields.files import FieldFile
from django.utils.module_loading import import_string

from imgproxykit.integrations.django.settings import Settings, get_config


def resolve_source(source: str | FieldFile) -> str:
    """
    Resolve an image source using Django's configured resolver.

    Call ``source_resolver`` with the original string or file field. The
    setting accepts a callable or a dotted import path to one. It must
    return a URI understood by the imgproxy server.
    This allows projects to resolve relative media URLs or construct storage
    URIs such as ``s3://bucket/key`` without accessing the field's URL first.

    Without a resolver, return strings unchanged and use ``FieldFile.url``
    for file fields. Relative URLs are not expanded automatically.

    Args:
        source: Source string or model file field, including empty fields.

    Returns:
        Source URI to pass to the configured client.
    """
    resolver = get_config()[Settings.source_resolver.value]  # pyright: ignore[reportTypedDictNotRequiredAccess]
    if isinstance(resolver, str):
        resolver = import_string(resolver)
    return resolver(source)


def default_source_resolver(source: str | FieldFile) -> str:
    """
    Return a source string unchanged or use a file field's storage URL.

    Relative URLs are not expanded.

    Raises:
        ValueError: If the file field has no associated file, as with
            direct access to ``FieldFile.url``.
    """
    return source.url if isinstance(source, FieldFile) else source
