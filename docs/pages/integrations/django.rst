Django
======

Generate imgproxy URLs from source strings and model file fields in Python
code or Django templates. Configure the client and reusable transformations
in Django settings, then generate individual image URLs or named sets of
image variants.

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

To use template tags, add the integration to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'imgproxykit.integrations.django',
    ]

.. tip::

    Adding the integration to ``INSTALLED_APPS`` is only required for template
    tags.

Configuration
-------------

Define ``IMGPROXYKIT`` in your Django settings:

.. literalinclude:: /examples/integrations/django/settings.py
   :language: python
   :lines: 1-19

.. code-annotations::

   1. Configure the shared client. ``base_url`` is required.
   2. Use your server's hex-encoded key and salt, or omit both if the server
      accepts unsigned URLs.
   3. Optional named transformations for Python shortcuts and template tags.
   4. Optional named sets of transformations for generating variants.

See :doc:`../user-guide/client` for other client options.

Generate URLs
-------------

Use ``imgproxy_url`` with a source string or model file field and a
transformation name from ``IMGPROXYKIT['transforms']``:

.. literalinclude:: /examples/integrations/django/url.py
   :language: python
   :lines: 10-14
   :dedent: 4
   :show-output:

.. code-annotations::

   1. Select ``IMGPROXYKIT['transforms']['thumbnail']``.

You can also pass a ``Transform`` object directly. Omit the transformation
argument to generate a URL without processing options.

Generate variants
-----------------

Use ``imgproxy_variants`` with a set name from ``IMGPROXYKIT['variants']``
to generate several URLs for the same source:

.. literalinclude:: /examples/integrations/django/variants.py
   :language: python
   :lines: 10-16
   :dedent: 4
   :show-output:
   :output-language: python

.. code-annotations::

   1. Select ``IMGPROXYKIT['variants']['product']`` and generate a URL
      for each configured name.

The result is a dictionary of URLs with the configured variant names as keys.
You can also pass a dictionary of names and ``Transform`` objects directly
instead of a set name.

Templates
---------

.. warning::

    Add ``'imgproxykit.integrations.django'`` to ``INSTALLED_APPS`` before
    using the template tags.

Load ``imgproxykit`` in your template, then use ``imgproxy_url`` to display
an image with the ``thumbnail`` transformation configured above:

.. code-block:: django

    {% load imgproxykit %}

    {% if product.image %}
      <img src="{% imgproxy_url product.image 'thumbnail' %}" alt="{{ product.name }}">
    {% endif %}

The source can be a model file field, as shown here, or a source string.
The transformation name is optional; omitting it generates a URL without
processing options.

For a preview that links to a larger image, use ``imgproxy_variants`` with
the configured ``product`` variant set:

.. code-block:: django

    {% load imgproxykit %}
    {% if product.image %}
      {% imgproxy_variants product.image 'product' as images %}
      <a href="{{ images.large }}">
        <img src="{{ images.small }}" alt="{{ product.name }}">
      </a>
    {% endif %}

Source resolution
-----------------

By default, strings are passed unchanged and model file fields use ``.url``.
Relative URLs are not expanded automatically.

Configure `IMGPROXY_BASE_URL
<https://docs.imgproxy.net/latest/configuration/options#source-image-urls>`__
on imgproxy, or set ``IMGPROXYKIT['source_resolver']`` to resolve sources in
Django. The resolver receives the original string or file field and must
return a URI accessible to imgproxy.

Define a resolver in ``myapp/images.py``:

.. literalinclude:: /examples/integrations/django/source_resolver.py
   :language: python
   :lines: 1-13
   :show-output:

.. code-annotations::

   1. Resolve relative paths against the media domain. Absolute URLs keep
      their own domain.

Register the resolver in your Django settings:

.. code-block:: python

    IMGPROXYKIT = {
        # ...
        'source_resolver': 'myapp.images.resolve_image_source',
    }

The setting also accepts a callable directly instead of an import path.

Next steps
----------

* :doc:`dmr` returns image URLs and variants from typed controllers.
* :doc:`drf` returns image URLs and variants from serializer fields.
* :doc:`../api-reference/django` documents the client, URL generation functions,
  source resolution, and settings.
