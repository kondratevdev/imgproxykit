Django
======

The Django integration builds imgproxy URLs from source strings and model
file fields. Configure a shared client in Django settings, then use the
shortcuts in views or application code.

Installation
------------

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add 'imgproxykit[django]'

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add 'imgproxykit[django]'

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install 'imgproxykit[django]'

Configuration
-------------

Define ``IMGPROXYKIT`` in your Django settings:

.. code-block:: python

    import os

    from imgproxykit import Transform
    from imgproxykit.integrations.django import SettingsDict

    thumbnail = Transform(width=300, height=300, format='webp')

    IMGPROXYKIT: SettingsDict = {
        'client': {
            'base_url': 'https://imgproxy.example.com',
            'key': os.environ['IMGPROXY_KEY'],
            'salt': os.environ['IMGPROXY_SALT'],
        },
        'transforms': {'thumbnail': thumbnail},
        'variants': {
            'product': {
                'small': thumbnail,
                'large': Transform(width=1280, format='webp'),
            },
        },
    }

``client`` and its ``base_url`` are required. Supply both ``key`` and ``salt``
as hex-encoded strings matching your imgproxy server. Omit both to generate
unsigned URLs; the server must accept them. The remaining client options are
``signature_size`` (default ``32``), ``unsigned_signature`` (``'unsafe'``),
and ``arguments_separator`` (``':'``). See :doc:`../user-guide/client` for
details and signing validation.

``transforms`` and ``variants`` default to empty mappings. Their names refer
to Python transformations, independently of presets on the imgproxy server.
``SettingsDict`` and ``ClientSettingsDict`` are optional type annotations
for checking configuration in your editor or type checker.

Adding ``imgproxykit.integrations.django`` to ``INSTALLED_APPS`` is optional
for these Python helpers. No database migrations are required.

Generate URLs
-------------

Pass a source URI and either a configured transformation name or a
:class:`~imgproxykit.Transform`:

.. code-block:: python

    from imgproxykit import Transform
    from imgproxykit.integrations.django import imgproxy_url

    source = 'https://originals.example.com/products/backpack.jpg'
    thumbnail_url = imgproxy_url(source, 'thumbnail')
    preview_url = imgproxy_url(source, Transform(width=640))
    original_url = imgproxy_url(source)

Omitting the transformation adds no processing options. URL generation
makes no network requests; a running imgproxy server fetches and processes
the source when the generated URL is requested.

Generate variants
-----------------

Use a configured set name or pass a mapping of transformations directly:

.. code-block:: python

    from imgproxykit import Transform
    from imgproxykit.integrations.django import imgproxy_variants

    source = 'https://originals.example.com/products/backpack.jpg'
    product_urls = imgproxy_variants(source, 'product')
    small_url = product_urls['small']

    responsive_urls = imgproxy_variants(
        source,
        {'mobile': Transform(width=480), 'desktop': Transform(width=1440)},
    )

The result is a dictionary of URLs in variant order. The source resolver
runs once for the whole set. Unknown transformation or variant set names
raise ``KeyError``.

Model file fields
-----------------

Both shortcuts accept model ``FileField`` and ``ImageField`` values:

.. code-block:: python

    from imgproxykit.integrations.django import imgproxy_url

    def product_image_url(product):
        if not product.image:
            return None
        return imgproxy_url(product.image, 'thumbnail')

The default resolver returns strings unchanged and reads ``FieldFile.url``
for file fields. An empty file field raises ``ValueError``. Handle missing
images before calling the shortcuts, or provide a resolver with a fallback.

Relative storage URLs such as ``/media/photo.jpg`` are not automatically
expanded. The resolved URI must be accessible to your imgproxy server.

Custom source resolver
----------------------

Set ``source_resolver`` to a callable or its dotted import path. It receives
the original string or file field, including empty fields, and must return
a source URI. For example, resolve media URLs against a public origin:

.. code-block:: python

    # myapp/images.py
    from urllib.parse import urljoin

    from django.db.models.fields.files import FieldFile

    def resolve_image_source(source: str | FieldFile) -> str:
        if isinstance(source, FieldFile):
            if not source:
                return 'https://originals.example.com/placeholder.jpg'
            source = source.url
        return urljoin('https://originals.example.com/', source)

Then add the resolver to your settings:

.. code-block:: python

    IMGPROXYKIT['source_resolver'] = 'myapp.images.resolve_image_source'

A resolver can also construct storage URIs such as ``s3://bucket/key`` from
``FieldFile.name`` without accessing its storage URL. Configure your imgproxy
server to support the returned URI scheme.

Access the client
-----------------

:func:`~imgproxykit.integrations.django.get_client` returns the shared
:class:`~imgproxykit.Client`, created lazily on first use:

.. code-block:: python

    from imgproxykit.integrations.django import get_client

    url = get_client().url('https://originals.example.com/photo.jpg')

Direct client calls accept source strings and bypass Django's source resolver
and named transformation lookup. Use the shortcuts for those features.
Django's ``override_settings(IMGPROXYKIT=...)`` clears the client cache on
entry and exit, so tests use the overridden configuration.

Missing or ``None`` ``IMGPROXYKIT`` settings raise ``ImproperlyConfigured``
when configuration is first accessed.

Next steps
----------

* :doc:`../user-guide/transformations` describes reusable transformations.
* :doc:`../user-guide/variants` covers variant mappings and typed keys.
* :doc:`../api-reference/django` documents the helpers and settings types.
