Django
======

The Django integration lets you generate imgproxy URLs from source strings
and model file fields. Configure a shared client in Django settings, then
use Python shortcuts or template tags to apply reusable transformations
and generate named sets of image variants.

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

    Python shortcuts work without adding the integration to ``INSTALLED_APPS``.

Configuration
-------------

Define ``IMGPROXYKIT`` in your Django settings:

.. literalinclude:: /examples/integrations/django/settings.py
   :language: python
   :start-at: from

``client.base_url`` is required. Set ``key`` and ``salt`` to your server's
hex-encoded credentials, or omit both if the server accepts unsigned URLs.
See :doc:`../user-guide/client` for other client options.

``transforms`` defines named transformations, and ``variants`` groups
transformations into named sets. Both are optional and can be reused by
Python shortcuts and template tags.

Generate URLs
-------------

Generate variants
-----------------

Templates
---------

Source resolution
-----------------

Next steps
----------
