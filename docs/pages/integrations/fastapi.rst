FastAPI
=======

The FastAPI integration lets you generate imgproxy URLs in route handlers
using FastAPI's dependency injection. Register a configured
:class:`~imgproxykit.Client` once when creating your application, then
inject it into handlers with ``Depends``. The same client is reused across
requests, keeping the imgproxy address and signing credentials in one place.

Installation
------------

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

Register Client
---------------

Call :func:`~imgproxykit.integrations.fastapi.add_imgproxy` while creating
the application. Keep the returned dependency for use in your routes:

.. literalinclude:: /examples/integrations/fastapi_client.py
   :language: python
   :start-at: from typing

The client is stored on ``app.state.imgproxykit_client``.
URL generation makes no network requests. Configure signing
credentials on :class:`~imgproxykit.Client` as described in
:doc:`../user-guide/client`.

Multiple clients
----------------

Register each client separately and use its returned dependency in
``Depends``. This example injects both a signed and an unsigned client:

.. literalinclude:: /examples/integrations/fastapi_multiple_clients.py
   :language: python
   :start-at: from typing

The first client uses ``app.state.imgproxykit_client``. The additional
client uses the attribute supplied through ``name``, here
``app.state.unsigned_imgproxy``. A name that is already present on
``app.state`` raises ``ValueError``.

Unsigned URLs require an imgproxy server configured to accept them.

Next steps
----------

* :doc:`../user-guide/transformations` describes reusable transformations.
* :doc:`../user-guide/variants` shows how to generate several image URLs.
* :doc:`../api-reference/fastapi` documents the registration function.
