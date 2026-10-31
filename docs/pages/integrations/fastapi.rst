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

Register a client
-----------------

Call :func:`~imgproxykit.integrations.fastapi.add_imgproxy` while creating
the application. Keep the returned dependency for use in your routes:

.. literalinclude:: /examples/integrations/fastapi/client.py
   :language: python

.. code-annotations::

   1. Register the client once and keep the returned dependency. The client
      is stored on ``app.state.imgproxykit_client``.
   2. Inject the registered client into the route handler. The same client
      is reused across requests.

URL generation makes no network requests. See :doc:`../user-guide/client`
to configure signing credentials.

Return variants
---------------

Declare image variants as a dataclass and use it as a field in a Pydantic
response model:

.. literalinclude:: /examples/integrations/fastapi/variants.py
   :language: python

.. code-annotations::

   1. Associate each URL field with a transformation using ``Annotated``.
   2. Include the dataclass in the response model. FastAPI documents its
      string fields in the OpenAPI schema.
   3. Generate a dataclass instance containing the URLs. Pydantic serializes
      it as a nested object.

See :ref:`dataclass-variants` for declaration requirements.

Multiple clients
----------------

Register each client separately and use its returned dependency in
``Depends``. This example injects both a signed and an unsigned client:

.. literalinclude:: /examples/integrations/fastapi/multiple_clients.py
   :language: python

.. code-annotations::

   1. Register a signed client under the default name. Replace the example
      key and salt with your imgproxy credentials.
   2. Give the unsigned client a separate name on ``app.state``.
   3. Use each registration's returned dependency to inject its client.

Registering a name already present on ``app.state`` raises ``ValueError``.
Unsigned URLs require an imgproxy server configured to accept them.

Next steps
----------

* `FastAPI documentation <https://fastapi.tiangolo.com/>`__
  covers route handlers, dependencies, validation, and API schemas.
* `FastAPI on GitHub <https://github.com/fastapi/fastapi>`__
  provides the source code, issues, and contribution guide.
* :doc:`../user-guide/variants` shows how to generate several image URLs.
* :doc:`../api-reference/fastapi` documents the registration function.
