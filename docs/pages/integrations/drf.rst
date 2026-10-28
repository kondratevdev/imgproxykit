Django REST Framework
=====================

Generate imgproxy URLs using DRF serializers. Return a single image URL
or a dictionary of named variants using transformations configured
in Django settings.

Installation
------------

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

Define ``IMGPROXYKIT`` in your Django settings. This integration shares
the client, named transformations, variant sets, and source resolver with
the :doc:`Django integration <django>`:

.. literalinclude:: /examples/integrations/django/settings.py
   :language: python
   :start-at: from

``client.base_url`` is required. Set ``key`` and ``salt`` to your server's
hex-encoded credentials, or omit both if the server accepts unsigned URLs.

Serializer fields
-----------------

Use :class:`~imgproxykit.integrations.drf.ImgproxyURLField` for one URL
and :class:`~imgproxykit.integrations.drf.ImgproxyVariantsField` for a
dictionary of named URLs. Both fields read the original image from
``source``:

.. literalinclude:: /examples/integrations/drf/serializer.py
   :language: python
   :start-at: from rest_framework

``transform='thumbnail'`` selects ``IMGPROXYKIT['transforms']['thumbnail']``.
``variants='product'`` selects ``IMGPROXYKIT['variants']['product']``.
The response contains a ``thumbnail`` URL and an ``images`` dictionary with
``small`` and ``large`` URLs.

The same field declarations work in a ``ModelSerializer``: use the model's
file field as ``source`` and include the generated fields in ``Meta.fields``.
Request context is not required, and URL generation makes no network requests.

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
   :start-at: from rest_framework

Omit ``transform`` from ``ImgproxyURLField`` to generate a URL without
processing options. ``ImgproxyVariantsField`` always requires ``variants``.

File uploads
------------

Use a standard DRF ``ImageField`` to accept uploads, alongside the generated
fields used in the response:

.. code-block:: python

    image = serializers.ImageField(write_only=True, required=False)
    thumbnail = ImgproxyURLField(source='image', transform='thumbnail')
    images = ImgproxyVariantsField(source='image', variants='product')

In a ``ModelSerializer``, include all three fields in ``Meta.fields``.
Configure an appropriate parser for the upload endpoint, as described in
`DRF's file upload documentation
<https://www.django-rest-framework.org/api-guide/fields/#file-upload-fields>`__.

Source resolution
-----------------

Nonempty source strings and model file fields use the Django integration's
source resolver. By default, strings are passed unchanged and file fields
use their storage URL. Relative URLs are not expanded using the request.
See :doc:`django` for relative media URLs and custom storage URIs.

Next steps
----------

* :doc:`django` describes shared settings and source resolution.
* :doc:`../user-guide/transformations` describes reusable transformations.
* :doc:`../api-reference/drf` documents the serializer fields and arguments.
