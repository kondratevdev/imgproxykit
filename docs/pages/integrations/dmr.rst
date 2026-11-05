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

.. code-annotations::

   1. Configure the shared client with your imgproxy server's URL.
   2. Use your server's hex-encoded key and salt, or omit both if the server
      accepts unsigned URLs.
   3. Define the ``thumbnail`` transformation used by the URL example.
   4. Define the ``product`` variant set used by the variants example.

Generate URLs
-------------

Generate a URL with ``imgproxy_url`` and return it in a Pydantic response model.

The examples use ``PydanticFastSerializer`` with Pydantic response models.
See DMR's `Pydantic plugin guide
<https://django-modern-rest.readthedocs.io/en/latest/pages/plugins.html#pydanticfastserializer>`__
for serializer options.

.. tab-set::

    .. tab-item:: Named transform

        Use a transformation name from ``IMGPROXYKIT['transforms']``:

        .. literalinclude:: /examples/integrations/dmr/url.py
           :language: python

        .. code-annotations::

           1. Select ``IMGPROXYKIT['transforms']['thumbnail']``.

    .. tab-item:: Transform

        Pass a ``Transform`` object directly:

        .. literalinclude:: /examples/integrations/dmr/inline_url.py
           :language: python

        .. code-annotations::

           1. Define the thumbnail transformation directly in the call.

Omit the transformation argument to generate a URL without processing options.

Generate variants
-----------------

Use ``imgproxy_variants`` with a named set, a mapping, or a dataclass class
to generate several URLs for the same source:

.. tab-set::

    .. tab-item:: Named set

        Use a set name from ``IMGPROXYKIT['variants']`` and validate the generated
        dictionary with a nested response model:

        .. literalinclude:: /examples/integrations/dmr/variants.py
           :language: python

        .. code-annotations::

           1. Declare the expected variant names in the response model.
           2. Select ``IMGPROXYKIT['variants']['product']``. Named sets always return
              a dictionary, even when configured with a dataclass class.
           3. Build the response model from the generated dictionary.

    .. tab-item:: Mapping

        Pass a mapping of names and transformations directly:

        .. literalinclude:: /examples/integrations/dmr/mapping_variants.py
           :language: python

        .. code-annotations::

           1. Declare the expected variant names in the response model.
           2. Map variant names to their transformations.
           3. Build the response model from the generated dictionary.

    .. tab-item:: Dataclass

        Pass a dataclass class to get an instance with typed URL fields:

        .. literalinclude:: /examples/integrations/dmr/dataclass_variants.py
           :language: python

        .. code-annotations::

           1. Associate each URL field with a transformation using ``Annotated``.
           2. Include the dataclass in the Pydantic response model.
           3. Generate a ``ProductImages`` instance and return it in the response.
              Pydantic serializes it as a nested object.

        See the Dataclass tab in :ref:`Generate variants <dataclass-variants>`
        for declaration requirements.

Use a dataclass or a Pydantic model for a fixed set of variants. Their named
URL fields appear in the OpenAPI schema. If variant names can vary, use
``images: dict[str, str]`` and return the generated dictionary directly.

Source resolution
-----------------

Both ``imgproxy_url`` and ``imgproxy_variants`` accept a source string or a
model file field, such as ``product.image``.

.. include:: /_includes/django-source-resolution.rst

.. warning::

    Django shortcuts pass empty values to the source resolver too. The default
    resolver returns an empty string as it is, but a model file field without
    an associated file raises ``ValueError``.
    Check for an associated file before calling a shortcut if the image
    is optional.

Next steps
----------

* `DMR documentation <https://django-modern-rest.readthedocs.io/en/latest/>`__
  covers controllers, validation, serializers, and API schemas.
* `DMR on GitHub <https://github.com/wemake-services/django-modern-rest>`__
  provides the source code, issues, and contribution guide.
* :doc:`../user-guide/variants` describes reusable variant sets.
* :doc:`../api-reference/django` documents the shared client and shortcuts.
