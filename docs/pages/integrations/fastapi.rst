FastAPI
=======

`FastAPI <https://fastapi.tiangolo.com/>`__ is a Python API framework
based on type hints, with data validation and OpenAPI schema generation.
Use imgproxykit's dependency integration to inject a client into route
handlers and return image URLs and named variants in typed response models.

Explore the `FastAPI tutorial <https://fastapi.tiangolo.com/tutorial/>`__
and the `project on GitHub <https://github.com/fastapi/fastapi>`__.

Installation
------------

In your FastAPI project, install imgproxykit with FastAPI support:

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add 'imgproxykit[fastapi]'

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add 'imgproxykit[fastapi]'

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install 'imgproxykit[fastapi]'

Configuration
-------------

Call :func:`~imgproxykit.integrations.fastapi.add_imgproxy` while creating
the application. Keep the returned dependency for use in your routes:

.. literalinclude:: /examples/integrations/fastapi/settings.py
   :language: python

The same client is reused across requests. See :doc:`../user-guide/client`
to configure signing credentials.

Generate URLs
-------------

Use ``Client.url`` to generate a URL and return it in a Pydantic response
model:

.. literalinclude:: /examples/integrations/fastapi/client.py
   :language: python

.. code-annotations::

   1. Inject the registered client into the route handler.

Pass a ``Transform`` object to configure processing options. Omit ``transform``
to generate a URL without processing options.

Generate variants
-----------------

Use ``Client.variants`` with a mapping or a dataclass class to generate
several URLs for the same source:

.. tab-set::

    .. tab-item:: Mapping

        Pass a mapping of names and transformations and use a dictionary field
        in the response model:

        .. literalinclude:: /examples/integrations/fastapi/mapping_variants.py
           :language: python

        .. code-annotations::

           1. Map variant names to their transformations.
           2. Return the generated dictionary in the response model.

    .. tab-item:: Dataclass

        Declare image variants as a dataclass and use it as a field in a Pydantic
        response model:

        .. literalinclude:: /examples/integrations/fastapi/variants.py
           :language: python

        .. code-annotations::

           1. Associate each URL field with a transformation using ``Annotated``.
           2. Return a ``ProductImages`` instance in the response model.

        See the Dataclass tab in :ref:`Generate variants <dataclass-variants>`
        for declaration requirements.

Use a dataclass for a fixed set of variants with named fields in the OpenAPI
schema. Use a mapping when variant names can vary.

Multiple clients
----------------

Give each client a unique ``name`` to register multiple clients on the same
application. Each call returns a dependency for that client:

.. literalinclude:: /examples/integrations/fastapi/multiple_clients.py
   :language: python

.. code-annotations::

   1. Use a different name for each client. Add more clients the same way.
   2. Inject each client with its returned dependency.

Names must be unique within the application. Reusing a name raises
``ValueError``.

Next steps
----------

* `FastAPI documentation <https://fastapi.tiangolo.com/>`__
  covers route handlers, dependencies, validation, and API schemas.
* `FastAPI on GitHub <https://github.com/fastapi/fastapi>`__
  provides the source code, issues, and contribution guide.
* :doc:`../user-guide/variants` shows how to generate several image URLs.
* :doc:`../api-reference/fastapi` documents the registration function.
