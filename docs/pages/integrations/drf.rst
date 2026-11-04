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

.. code-annotations::

   1. Configure the shared client. ``base_url`` is required.
   2. Use your server's hex-encoded key and salt, or omit both if the server
      accepts unsigned URLs.
   3. Optional named transformations.
   4. Optional named sets of transformations for generating variants.

Generate URLs
-------------

Use :class:`~imgproxykit.integrations.drf.ImgproxyURLField` with a named
transformation or a ``Transform`` object. Set ``source`` to the original
image field:

.. tab-set::

    .. tab-item:: Named transform

        Use a transformation name from ``IMGPROXYKIT['transforms']``:

        .. literalinclude:: /examples/integrations/drf/url.py
           :language: python

        .. code-annotations::

           1. Select ``IMGPROXYKIT['transforms']['thumbnail']``.

    .. tab-item:: Transform

        Pass a ``Transform`` object directly:

        .. literalinclude:: /examples/integrations/drf/inline_url.py
           :language: python

        .. code-annotations::

           1. Define the thumbnail transformation on the field.

Omit ``transform`` to generate a URL without processing options.

Generate variants
-----------------

Use :class:`~imgproxykit.integrations.drf.ImgproxyVariantsField` with a named
set, a mapping, or a dataclass class to generate several URLs for the same
source:

Both fields are read-only. ``ImgproxyVariantsField`` returns a dictionary of
URLs for all three declaration styles.

.. tab-set::

    .. tab-item:: Named set

        Use a set name from ``IMGPROXYKIT['variants']``:

        .. literalinclude:: /examples/integrations/drf/variants.py
           :language: python

        .. code-annotations::

           1. Select ``IMGPROXYKIT['variants']['product']``.

        The configured set can be a mapping or a dataclass class.

    .. tab-item:: Mapping

        Pass a mapping of names and transformations directly:

        .. literalinclude:: /examples/integrations/drf/mapping_variants.py
           :language: python

        .. code-annotations::

           1. Map variant names to their transformations.

    .. tab-item:: Dataclass

        Pass a dataclass class to reuse a typed variant declaration:

        .. literalinclude:: /examples/integrations/drf/dataclass_variants.py
           :language: python

        .. code-annotations::

           1. Associate each URL field with a transformation using ``Annotated``.
           2. Return the generated URLs as a dictionary.

        The field's schema remains a dictionary of URLs. Dataclass field names are
        not automatically exposed as named properties in the API schema.

        See the Dataclass tab in :ref:`Generate variants <dataclass-variants>`
        for declaration requirements.

For a ``ModelSerializer``, use the model's file field as ``source`` and include
the generated fields in ``Meta.fields``.

Source resolution
-----------------

Both fields read the value selected by ``source``, such as ``source='image'``.

.. tip::

    Empty strings, ``None``, and model file fields without an associated file
    return ``null``. The source resolver is not called for these values.

.. include:: /_includes/django-source-resolution.rst

Next steps
----------

* `DRF documentation <https://www.django-rest-framework.org/>`__
  covers serializers, views, authentication, and API schemas.
* `DRF on GitHub <https://github.com/encode/django-rest-framework>`__
  provides the source code, issues, and contribution guide.
* :doc:`django` describes shared settings and source resolution.
* :doc:`../api-reference/drf` documents the serializer fields and arguments.
