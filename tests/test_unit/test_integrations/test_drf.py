# Optional integration tests require their framework.
import pytest

try:
    from rest_framework import serializers
except ImportError:  # pragma: no cover
    pytest.skip(
        reason='djangorestframework is not installed',
        allow_module_level=True,
    )

from typing import Any

from django.conf import LazySettings
from django.db.models import ImageField, Model
from django.db.models.fields.files import FieldFile

from imgproxykit import Transform
from imgproxykit.integrations.drf import ImgproxyURLField, ImgproxyVariantsField


class _Image(Model):
    """Provide a model instance for file fields without database access."""

    class Meta:
        app_label = 'imgproxykit'


class _ImageSerializer(serializers.Serializer[Any]):
    """Generate image URLs using inline transformations."""

    url = ImgproxyURLField(
        source='image',
        transform=Transform(width=160),
    )
    images = ImgproxyVariantsField(
        source='image',
        variants={'small': Transform(width=160)},
    )


class _NamedImageSerializer(_ImageSerializer):
    """Generate image URLs using transformations from Django settings."""

    url = ImgproxyURLField(source='image', transform='preview')
    images = ImgproxyVariantsField(source='image', variants='responsive')


@pytest.mark.parametrize(
    ('field_class', 'options', 'message'),
    [
        (
            ImgproxyURLField,
            {'read_only': False},
            'read_only must be True',
        ),
        (
            ImgproxyURLField,
            {'write_only': True},
            'write_only must be False',
        ),
        (
            ImgproxyVariantsField,
            {'variants': {}, 'read_only': False},
            'read_only must be True',
        ),
        (
            ImgproxyVariantsField,
            {'variants': {}, 'write_only': True},
            'write_only must be False',
        ),
    ],
)
def test_invalid_access_options(
    *,
    field_class: type[ImgproxyURLField] | type[ImgproxyVariantsField],
    options: dict[str, Any],
    message: str,
) -> None:
    """Reject field options that conflict with read-only output."""
    with pytest.raises(ValueError, match=message):
        field_class(**options)


def test_custom_child() -> None:
    """Reject replacing the URL child used to describe variant values."""
    with pytest.raises(TypeError, match='child cannot be supplied'):
        ImgproxyVariantsField(variants={}, child=serializers.CharField())


@pytest.mark.parametrize(
    'source',
    [
        None,
        '',
        FieldFile(_Image(), ImageField(), ''),
    ],
)
def test_empty_source(*, source: str | FieldFile | None) -> None:
    """Return null for empty sources without requiring imgproxy settings."""
    assert ImgproxyURLField().to_representation(source) is None
    assert ImgproxyVariantsField(variants={}).to_representation(source) is None


@pytest.mark.parametrize(
    'serializer_class',
    [_ImageSerializer, _NamedImageSerializer],
)
def test_image_urls(
    settings: LazySettings,
    *,
    serializer_class: type[_ImageSerializer],
) -> None:
    """Serialize a source into a transformed URL and named variants."""
    transform = Transform(width=160)
    variants = {'small': transform}
    settings.IMGPROXYKIT = {
        'client': {'base_url': 'https://images.example.com'},
        'transforms': {'preview': transform},
        'variants': {'responsive': variants},
    }

    serializer = serializer_class({'image': 'https://example.com/photo.jpg'})
    expected = (
        'https://images.example.com/unsafe/width:160/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )
    assert serializer.data == {  # pyright: ignore[reportUnknownMemberType]
        'url': expected,
        'images': {'small': expected},
    }
