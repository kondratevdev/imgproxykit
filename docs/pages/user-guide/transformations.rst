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
   :show-output:
   :lines: 1-15

.. code-annotations::

   1. Pass structured processing options as positional option instances.
   2. Pass scalar options as keywords. ``quality=85`` is equivalent to
      ``Quality(85)``.

Pass ``thumbnail`` to ``client.url()`` to apply it to an image.
See :doc:`options` for available options and their arguments.

Reuse a transformation
----------------------

Define a transformation once and use it with different source images:

.. literalinclude:: /examples/transformations/reuse_transform.py
   :language: python
   :show-output:
   :lines: 1-19

.. code-annotations::

   1. Transformations and built-in options are immutable. You can keep
      ``thumbnail`` at module level and reuse it across requests.

Each URL uses the same transformation with a different source.

Compose transformations
-----------------------

Use :meth:`~imgproxykit.Transform.extend` to create a new transformation
with additional options:

.. literalinclude:: /examples/transformations/extend.py
   :language: python
   :show-output:
   :lines: 1-15

.. code-annotations::

   1. Shared quality and output format.
   2. Append a square crop, leaving ``base`` unchanged.
   3. Append a pixel density option, leaving ``thumbnail`` unchanged.

The generated URLs show the options retained by each transformation.
New positional options follow existing options; scalar keywords come last,
in keyword order.

To combine reusable groups, pass another transformation's unpacked
``options`` to ``extend()``:

.. literalinclude:: /examples/transformations/composition.py
   :language: python
   :show-output:
   :lines: 1-12

.. code-annotations::

   1. Unpack ``square.options`` to append its options to ``base``.
      Both original transformations remain unchanged.

``extend()`` appends options without merging or replacing them. For example,
``base.extend(quality=70)`` retains both quality options. Imgproxy resolves
the resulting settings and determines the processing pipeline.

Next steps
----------

Continue with :doc:`options` to explore processing options and their values.
See the :doc:`Transform API reference <../api-reference/transform>` for all
transformation arguments.
