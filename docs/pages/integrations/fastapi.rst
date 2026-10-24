FastAPI
=======

Register a :class:`~imgproxykit.Client` on your FastAPI application and
inject it into route handlers with ``Depends``.

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

The client is stored on ``app.state.imgproxykit_client`` and reused across
requests. URL generation makes no network requests. Configure signing
credentials on :class:`~imgproxykit.Client` as described in
:doc:`../user-guide/client`.

Multiple clients
----------------

Supply a different ``name`` for each additional client. The name is the
attribute used on ``app.state``:

.. literalinclude:: /examples/integrations/fastapi_multiple_clients.py
   :language: python
   :start-at: get_preview_imgproxy =

Use the returned dependency in ``Depends`` in the same way as
``get_imgproxy``. A name that is already present on ``app.state`` raises
``ValueError``.

Dependencies resolve their client on the application handling the request.
When sharing a router between applications, register the same name on each
application.

Next steps
----------

* :doc:`../user-guide/transformations` describes reusable transformations.
* :doc:`../user-guide/variants` shows how to generate several image URLs.
* :doc:`../api-reference/fastapi` documents the registration function.
