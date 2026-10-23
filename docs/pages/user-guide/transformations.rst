Transform
=========

A :class:`~imgproxykit.Transform` defines how imgproxy should process an
image, including its dimensions, quality, and output format. Pass it to
:class:`~imgproxykit.Client` when building a URL, and reuse the same
transformation across different source images.

.. tip::

    Use the :ref:`local Docker server <user-guide-docker>` on port 8080 for
    the examples in this chapter.

Create a transformation
-----------------------

Pass structured options as positional arguments and simple settings as
keyword arguments:

.. literalinclude:: /examples/transformations/create_transform.py
   :language: python
   :lines: 10-27

``thumbnail`` combines a 300×300 crop, quality 85, and WebP output format.
Pass it to ``client.url()`` through the ``transform`` argument and open the
printed URL to see the result. The :doc:`options` chapter explains the
available option classes and their arguments.

Reuse a transformation
----------------------

Transformations are immutable and designed for reuse. Define a transformation
once and use it for different source images; building a URL does not change
its settings. Built-in option instances are immutable too.

For example, reuse a 300×300 WebP thumbnail transformation across product
images:

.. literalinclude:: /examples/transformations/reuse_transform.py
   :language: python
   :start-at: from imgproxykit

``thumbnail_urls`` contains a URL for each source, using the same crop and
format. You can keep ``thumbnail`` at module level and reuse it across
requests. To use different settings, create a new transformation.

Compose transformations
-----------------------

Group related settings in separate transformations, then unpack their
``options`` to combine them. You can add more options to the result:

.. literalinclude:: /examples/transformations/composition.py
   :language: python
   :lines: 12-34

``thumbnail`` combines the quality and format from ``base`` with the crop
from ``square``. ``retina`` uses the same options with twice the pixel
density. Each composition creates a new transformation; the original
transformations remain unchanged.

Unpacking appends options without merging or replacing them. Keep shared
groups focused on different settings to avoid conflicting options.

Next steps
----------

Continue with :doc:`options` to explore processing options and their values.
See the :doc:`Transform API reference <../api-reference/transform>` for all
transformation arguments.
