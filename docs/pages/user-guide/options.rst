Options
========

Options define individual processing settings, such as image dimensions,
quality, and crop position. Import option classes from ``imgproxykit.options``
and combine their instances in a :class:`~imgproxykit.Transform`. Simple
settings can also be passed as keyword arguments.

.. tip::

    Use the :ref:`local Docker server <user-guide-docker>` on port 8080 for
    the examples in this chapter.

Scalar options
--------------

Scalar options accept a single value. Pass an option instance to
``Transform``, or use the equivalent keyword argument:

.. literalinclude:: /examples/options/scalar_options.py
   :language: python
   :lines: 10-26

``Quality(85)`` and ``quality=85`` create the same option, as do
``Format('webp')`` and ``format='webp'``. Both forms can be used together
in one transformation. Choose whichever fits how you organize your settings.

Structured options
------------------

Structured options group related settings in named arguments. For example,
:class:`~imgproxykit.options.Resize` combines dimensions and resizing mode,
while :class:`~imgproxykit.options.Gravity` selects the crop position:

.. literalinclude:: /examples/options/resize.py
   :language: python
   :lines: 8-25

``Resize.fill()`` requests a 300×300 crop, ``Gravity.center()`` keeps the
center, and ``dpr=2`` requests twice the pixel density. Pass structured
options as positional arguments to ``Transform``; scalar keywords can
follow them.

Omitted arguments use imgproxy's defaults. For example, leaving
``Resize.enlarge`` unset lets the server decide whether to upscale a small
source. Explicit ``False`` and zero values are preserved.

.. _server-presets:

Server presets
--------------

:class:`~imgproxykit.options.Preset` references processing settings defined
on the imgproxy server. Pass preset names as positional arguments and
combine them with other options:

.. literalinclude:: /examples/transformations/presets.py
   :language: python
   :lines: 8-25

The guide's Docker server defines ``thumbnail`` as a 300×300 crop and
``small`` as a 96×96 crop. This example references both presets in that
order and requests quality 85 and WebP output. Imgproxy resolves their
settings; the library sends the preset names without loading or expanding
their definitions.

Available options
-----------------

Built-in options cover resizing and cropping, formats and quality, effects,
metadata, source limits, and URL behavior. For example,
:class:`~imgproxykit.options.Blur` adds blur,
:class:`~imgproxykit.options.Background` sets a background color, and
:class:`~imgproxykit.options.Filename` sets the download filename.
See the :doc:`Options API reference <../api-reference/options>` for the full
list and constructor arguments.

Some options require server configuration. For example, source limit
options require ``IMGPROXY_ALLOW_SECURITY_OPTIONS=true``. Supported formats
and processing features
depend on your imgproxy installation; type annotations do not check server
capabilities. See the `imgproxy configuration documentation
<https://docs.imgproxy.net/latest/configuration/options>`__ for server settings.

Next steps
----------

Continue with :doc:`variants` to generate named sets of image URLs.
See the :doc:`Options API reference <../api-reference/options>` for all
processing options and their arguments.
