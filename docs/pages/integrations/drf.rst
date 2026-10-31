Django REST Framework
=====================

`Django REST Framework (DRF) <https://www.django-rest-framework.org/>`__
is a toolkit for building Web APIs with Django. Use imgproxykit's serializer
fields to return image URLs and named variants, with transformations from
Django settings or defined directly on the fields.

Explore the `DRF quickstart
<https://www.django-rest-framework.org/tutorial/quickstart/>`__
and the `project on GitHub
<https://github.com/encode/django-rest-framework>`__.

Installation
------------

In your DRF project, install imgproxykit with Django REST Framework support:

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add 'imgproxykit[drf]'

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add 'imgproxykit[drf]'

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install 'imgproxykit[drf]'

The extra installs Django and Django REST Framework.

Configuration
-------------

Define ``IMGPROXYKIT`` in your Django settings. The client, transformations,
variant sets, and source resolver are shared with the :doc:`Django integration
<django>`:

.. literalinclude:: /examples/integrations/django/settings.py
   :language: python
   :lines: 1-19

.. code-annotations::

   1. Configure the shared client. ``base_url`` is required.
   2. Use your server's hex-encoded key and salt, or omit both if the server
      accepts unsigned URLs.
   3. Optional named transformations shared with the Django integration.
   4. Optional named sets of transformations for generating variants.

Serializer fields
-----------------

Use :class:`~imgproxykit.integrations.drf.ImgproxyURLField` for one URL
and :class:`~imgproxykit.integrations.drf.ImgproxyVariantsField` for named
variants. Set ``source`` to the original image field:

.. literalinclude:: /examples/integrations/drf/serializer.py
   :language: python
   :lines: 1-19

.. code-annotations::

   1. Use the named transformation from
      ``IMGPROXYKIT['transforms']['thumbnail']``.
   2. Use the named variant set from ``IMGPROXYKIT['variants']['product']``.

For a ``ModelSerializer``, use the model's file field as ``source`` and include
the generated fields in ``Meta.fields``. Request context is not required.

.. note::

    Both fields are read-only. Empty strings, ``None``, and model file
    fields without an associated file produce ``null``. Empty sources
    are not passed to the source resolver.

Inline transformations
----------------------

Pass a :class:`~imgproxykit.Transform` or a mapping of transformations
directly instead of referring to Django settings by name:

.. literalinclude:: /examples/integrations/drf/inline.py
   :language: python
   :lines: 1-23

.. code-annotations::

   1. Pass a ``Transform`` directly instead of a configured name.
   2. Map variant names to their transformations.

Omit ``transform`` from ``ImgproxyURLField`` to generate a URL without
processing options. ``ImgproxyVariantsField`` always requires ``variants``.

File uploads
------------

Use a standard DRF ``ImageField`` to accept uploads, alongside the generated
fields used in the response:

.. code-block:: python

    image = serializers.ImageField(write_only=True, required=False)  # (1)!
    thumbnail = ImgproxyURLField(source='image', transform='thumbnail')
    images = ImgproxyVariantsField(source='image', variants='product')

.. code-annotations::

   1. Accept uploads with a standard DRF field. The generated fields remain
      read-only and appear in the response.

In a ``ModelSerializer``, include all three fields in ``Meta.fields``.
Configure an appropriate parser for the upload endpoint, as described in
`DRF's file upload documentation
<https://www.django-rest-framework.org/api-guide/fields/#file-upload-fields>`__.

Source resolution
-----------------

Nonempty sources use the Django source resolver. Strings are passed unchanged;
file fields use ``.url``. Relative URLs are not expanded using the request.
See :doc:`django` to configure source resolution.

Next steps
----------

* `DRF documentation <https://www.django-rest-framework.org/>`__
  covers serializers, views, authentication, and API schemas.
* `DRF on GitHub <https://github.com/encode/django-rest-framework>`__
  provides the source code, issues, and contribution guide.
* :doc:`django` describes shared settings and source resolution.
* :doc:`../api-reference/drf` documents the serializer fields and arguments.
