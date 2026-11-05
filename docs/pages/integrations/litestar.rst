Litestar
========

`Litestar <https://litestar.dev/>`__ is a Python ASGI framework
with dependency injection and OpenAPI schema generation.
Use imgproxykit's plugin integration to inject a client into route
handlers and return image URLs and named variants in typed response models.

Explore the `Litestar documentation <https://docs.litestar.dev/2/>`__
and the `project on GitHub <https://github.com/litestar-org/litestar>`__.

Installation
------------

In your Litestar project, install imgproxykit with Litestar support:

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add 'imgproxykit[litestar]'

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add 'imgproxykit[litestar]'

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install 'imgproxykit[litestar]'

Configuration
-------------

Add :class:`~imgproxykit.integrations.litestar.ImgproxyPlugin` when creating
the application. Pass one client positionally to register it as ``imgproxy``:

.. literalinclude:: /examples/integrations/litestar/settings.py
   :language: python

The same client is reused across requests. See :doc:`../user-guide/client`
to configure signing credentials.

Generate URLs
-------------

Use ``Client.url`` to generate a URL and return it in a response dataclass:

.. literalinclude:: /examples/integrations/litestar/client.py
   :language: python

.. code-annotations::

   1. Inject the client registered under the default name ``imgproxy``.

Mark the handler parameter with ``NamedDependency[Client]`` and match its
name to the registered dependency. Pass a ``Transform`` object to configure
processing options. Omit ``transform`` to generate a URL without processing
options.

Generate variants
-----------------

Use :meth:`~imgproxykit.Client.variants` with a mapping or a dataclass class
to generate several URLs for the same source:

.. tab-set::

    .. tab-item:: Mapping

        Pass a mapping of names and transformations and use a dictionary field
        in the response dataclass:

        .. literalinclude:: /examples/integrations/litestar/mapping_variants.py
           :language: python

        .. code-annotations::

           1. Map variant names to their transformations.
           2. Return the generated dictionary in the response dataclass.

    .. tab-item:: Dataclass

        Declare image variants as a dataclass and use it as a field in a
        response dataclass:

        .. literalinclude:: /examples/integrations/litestar/variants.py
           :language: python

        .. code-annotations::

           1. Associate each URL field with a transformation using ``Annotated``.
           2. Return a ``ProductImages`` instance in the response dataclass.

        See the Dataclass tab in :ref:`Generate variants <dataclass-variants>`
        for declaration requirements.

Use a dataclass for a fixed set of variants with named fields in the OpenAPI
schema. Use a mapping when variant names can vary.

Multiple clients
----------------

Give each client a unique name in ``clients`` to register multiple clients
on the same application. Each key is a dependency name matching a handler
parameter:

.. literalinclude:: /examples/integrations/litestar/multiple_clients.py
   :language: python

.. code-annotations::

   1. Use a different name for each client. Add more clients the same way.
   2. Inject each client using its registered dependency name.

.. warning::

   Names must be unique within the application's dependencies. Reusing a name
   raises ``ValueError`` during application initialization. Pass either one
   positional client or ``clients``, never both.

Next steps
----------

* `Litestar documentation <https://docs.litestar.dev/2/>`__
  covers route handlers, dependencies, validation, and API schemas.
* `Litestar on GitHub <https://github.com/litestar-org/litestar>`__
  provides the source code, issues, and contribution guide.
* :doc:`../user-guide/variants` shows how to generate several image URLs.
* :doc:`../api-reference/litestar` documents the plugin.
