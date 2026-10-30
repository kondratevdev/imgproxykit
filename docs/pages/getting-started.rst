Getting started
===============

Build a transformed image URL, then define reusable variants for your
application. You will need an imgproxy server to serve the resulting URLs.

Installation
------------

imgproxykit requires Python 3.12 or newer:

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add imgproxykit

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add imgproxykit

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install imgproxykit

.. tip::

    To try the examples locally, start a test imgproxy container with Docker:

    .. code-block:: bash

        docker run -d --rm \
          --name imgproxy-test \
          -p 127.0.0.1:8080:8080 \
          ghcr.io/imgproxy/imgproxy:latest

    The examples below connect to this container at ``http://localhost:8080``.
    It accepts unsigned URLs without additional configuration.

    See the `imgproxy installation guide
    <https://docs.imgproxy.net/latest/installation>`__ for other setup options.

.. _quick-start:

Build a thumbnail
-----------------

Connect :class:`~imgproxykit.Client` to the local container and describe a
thumbnail with :class:`~imgproxykit.Transform`. The source is a public sample
image; you can replace it with another image URL accessible to imgproxy:

.. literalinclude:: /examples/getting_started/local_thumbnail.py
   :language: python
   :start-at: from imgproxykit

The example prints a URL pointing to your local imgproxy server. Open it in
your browser to view the 300×300 WebP thumbnail.

Build variants
--------------

To generate several sizes of the same image, define a set of transformations.
Reuse ``client`` and ``source_url`` from above, keep quality and format in a
base transformation, then use :meth:`~imgproxykit.Transform.extend` to
create a new transformation for each width without changing the base:

.. literalinclude:: /examples/getting_started/variants.py
   :language: python
   :start-at: from imgproxykit

The example prints three URLs for widths of 320, 640, and 1280 pixels.
Open them to compare the sizes; each image keeps the source proportions
and uses the shared WebP format and quality setting.

.. tip::

    When finished, stop the test container:

    .. code-block:: bash

        docker stop imgproxy-test

You've learned how to build image URLs and variants. Next, explore client
configuration and more ways to compose transformations.

Next steps
----------

* :doc:`user-guide/client` — client configuration and signed URLs.
* :doc:`user-guide/transformations` — compose and reuse processing settings.
* :doc:`user-guide/variants` — reusable sets and typed variant names.
