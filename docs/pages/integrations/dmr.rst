Django Modern REST
==================

`Django Modern REST (DMR)
<https://django-modern-rest.readthedocs.io/en/latest/>`__ is a typed REST
framework for Django with sync and async support and OpenAPI schema generation.
Use imgproxykit's Django shortcuts in DMR controllers to return image URLs
and named variants in typed response models.

Explore the `DMR getting started guide
<https://django-modern-rest.readthedocs.io/en/latest/pages/getting-started.html>`__
and the `project on GitHub
<https://github.com/wemake-services/django-modern-rest>`__.

Installation
------------

In your DMR project, install imgproxykit with Django support:

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

The integration uses the Django shortcuts directly. No DMR-specific plugin
or addition to ``INSTALLED_APPS`` is required.

Configuration
-------------

Define ``IMGPROXYKIT`` in your Django settings. These settings are shared with
the :doc:`Django integration <django>`:

.. literalinclude:: /examples/integrations/django/settings.py
   :language: python
   :lines: 1-19

.. code-annotations::

   1. Configure the shared client with your imgproxy server's URL.
   2. Use your server's hex-encoded key and salt, or omit both if the server
      accepts unsigned URLs.
   3. Define the ``thumbnail`` transformation used by the URL example.
   4. Define the ``product`` variant set used by the variants example.

Return an image URL
-------------------

Generate a URL with ``imgproxy_url`` and return it in a Pydantic response model.
URL generation makes no network requests; imgproxy processes the image when
its URL is requested.

The examples use ``PydanticFastSerializer`` for JSON requests and responses.
See DMR's `Pydantic plugin guide
<https://django-modern-rest.readthedocs.io/en/latest/pages/plugins.html#pydanticfastserializer>`__
for serializer options.

.. literalinclude:: /examples/integrations/dmr/url.py
   :language: python

.. code-annotations::

   1. Apply ``IMGPROXYKIT['transforms']['thumbnail']`` to the source image.
   2. Return the generated URL as a string in the response model.

See DMR's guides to `controllers
<https://django-modern-rest.readthedocs.io/en/latest/pages/using-controller/index.html>`__
and `path parameters
<https://django-modern-rest.readthedocs.io/en/latest/pages/components/path.html>`__
for request parsing and handler definitions.

Return variants
---------------

For several image sizes, use ``imgproxy_variants`` and a nested response model.
Keep the imports and ``_SOURCE_URL`` from the previous example,
replacing the shortcut import with
``from imgproxykit.integrations.django import imgproxy_variants``:

.. literalinclude:: /examples/integrations/dmr/variants.py
   :language: python
   :start-at: class ProductImages

.. code-annotations::

   1. Expose ``small`` and ``large`` as named fields in the response model
      and its OpenAPI schema.
   2. Generate URLs with ``IMGPROXYKIT['variants']['product']``.
   3. Validate the generated mapping against the response model. Keep its
      fields in sync with the configured variant names.

Use ``images: dict[str, str]`` and return the mapping directly when variant
names can vary. A dedicated model describes a fixed set of fields in the API.
See DMR's `OpenAPI guide
<https://django-modern-rest.readthedocs.io/en/latest/pages/openapi/openapi.html>`__
to publish the schema and interactive API documentation.

Model file fields
-----------------

For a product loaded from your database, pass ``product.image`` directly to
``imgproxy_url`` in the controller. Here, ``Product`` is your Django model
with an optional image field. ``ProductPath`` declares a ``product_id: int``
path parameter using a Pydantic model. Imports, the Django model, path model,
and the route are omitted from this snippet:

.. literalinclude:: /examples/integrations/dmr/model_file.py
   :language: python
   :start-at: class ProductResponse

.. code-annotations::

   1. Generate a URL only when the file field has an associated file;
      otherwise return ``None``, serialized as JSON ``null``.

Without the empty-field check, the default source
resolver raises ``ValueError`` for a field without an associated file.

Source resolution
-----------------

Both shortcuts use the shared Django source resolver: strings are passed
unchanged and model file fields use ``.url``. Relative URLs are not expanded
automatically. See :doc:`django` to configure relative URLs and storage URIs.

Next steps
----------

* `DMR documentation <https://django-modern-rest.readthedocs.io/en/latest/>`__
  covers controllers, validation, serializers, and API schemas.
* `DMR on GitHub <https://github.com/wemake-services/django-modern-rest>`__
  provides the source code, issues, and contribution guide.
* :doc:`../user-guide/variants` describes reusable variant sets.
* :doc:`../api-reference/django` documents the shared client and shortcuts.
