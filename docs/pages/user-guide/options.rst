Processing options
==================

Processing options describe the image you want imgproxy to produce. Import
option classes from ``imgproxykit.options`` and collect them in a
:class:`~imgproxykit.Transform`. Scalar options can also be supplied as keyword
arguments; see :doc:`transformations` for both forms and their ordering.

This page groups common options by task. For accepted arguments and links to
imgproxy's processing documentation, see :doc:`../api-reference/options`.

Dimensions and cropping
-----------------------

Use :class:`~imgproxykit.options.Resize` to set dimensions and resizing mode.
``fit`` preserves the image within the requested bounds, while ``fill`` fills
the requested dimensions by cropping. Use :class:`~imgproxykit.options.Gravity`
to choose the retained area.

.. literalinclude:: /examples/options/resize.py
   :language: python
   :start-at: from imgproxykit

Here, ``ce`` selects center gravity and ``dpr=2`` requests twice the pixel
density for the 300 by 300 target. Smaller sources are subject to imgproxy's
upscaling settings.

Related options:

* :class:`~imgproxykit.options.Width`, :class:`~imgproxykit.options.Height`,
  :class:`~imgproxykit.options.Size` and
  :class:`~imgproxykit.options.ResizingType` set individual sizing
  parameters.
* :class:`~imgproxykit.options.Enlarge` controls upscaling;
  :class:`~imgproxykit.options.Extend` and
  :class:`~imgproxykit.options.ExtendAspectRatio` control
  extending the canvas.
* :class:`~imgproxykit.options.Crop`, :class:`~imgproxykit.options.Zoom` and
  :class:`~imgproxykit.options.Trim` adjust the source area.
* :class:`~imgproxykit.options.MinWidth` and
  :class:`~imgproxykit.options.MinHeight` add sizing constraints.
* :class:`~imgproxykit.options.EnforceThumbnail` selects an embedded HEIC or
  AVIF thumbnail when available.
* :class:`~imgproxykit.options.Padding` adds space around the image;
  :class:`~imgproxykit.options.Background` sets its color.

Format, quality, and metadata
-----------------------------

Use :class:`~imgproxykit.options.Format` or the ``format`` keyword to choose an
output format, and
:class:`~imgproxykit.options.Quality` or ``quality`` to set encoding quality. A
background color is useful
when converting a transparent image to JPEG:

.. literalinclude:: /examples/options/format.py
   :language: python
   :start-at: from imgproxykit

The example requests JPEG output with a white background, quality 85, and
metadata stripping. Hex background colors omit the leading ``#``.

Related options:

* :class:`~imgproxykit.options.FormatQuality` sets quality for a particular
  format.
* :class:`~imgproxykit.options.MaxBytes` sets a target maximum output file size.
* :class:`~imgproxykit.options.StripMetadata`,
  :class:`~imgproxykit.options.KeepCopyright` and
  :class:`~imgproxykit.options.StripColorProfile` control
  metadata and color profile retention.
* :class:`~imgproxykit.options.PreserveHDR` controls HDR preservation for
  supported outputs.

Effects and orientation
-----------------------

A small resize combined with :class:`~imgproxykit.options.Blur` can produce a
preview placeholder:

.. literalinclude:: /examples/options/effects.py
   :language: python
   :start-at: from imgproxykit

Other options include :class:`~imgproxykit.options.Sharpen`,
:class:`~imgproxykit.options.Pixelate`,
:class:`~imgproxykit.options.AutoRotate`, :class:`~imgproxykit.options.Rotate`
and
:class:`~imgproxykit.options.Flip`. :class:`~imgproxykit.options.Watermark`
applies an image configured on the imgproxy server;
it does not upload a watermark image from your application.

.. note::

    Image output depends on your imgproxy version, configuration, source image,
    and supported formats. The client does not check server capabilities.

Source and animation limits
---------------------------

Use per-request limits when different image sources need different bounds:

.. literalinclude:: /examples/options/limits.py
   :language: python
   :start-at: from imgproxykit

This requests a source limit of 20 megapixels and 5,000,000 bytes.

.. important::

    :class:`~imgproxykit.options.MaxSrcResolution` and
    :class:`~imgproxykit.options.MaxSrcFileSize` require
    `IMGPROXY_ALLOW_SECURITY_OPTIONS
    <https://docs.imgproxy.net/latest/configuration/options#security>`__ set to
    ``true`` on the server. Generating a URL does
    not enable this setting.

    :class:`~imgproxykit.options.MaxAnimationFrames`,
    :class:`~imgproxykit.options.MaxAnimationFrameResolution` and
    :class:`~imgproxykit.options.MaxResultDimension` also override server limits
    and require that setting.

Configure server-wide limits on imgproxy when per-request overrides are not
needed.

URL behavior and presets
------------------------

These options control behavior beyond image dimensions and encoding:

* :class:`~imgproxykit.options.Preset` references named settings on the server.
  See
  :ref:`server-presets` for an example combining presets with other options.
* :class:`~imgproxykit.options.Expires` sets an expiration time as a Unix
  timestamp in seconds.
* :class:`~imgproxykit.options.CacheBuster` changes the URL to distinguish
  cached variants.
* :class:`~imgproxykit.options.Filename` and
  :class:`~imgproxykit.options.ReturnAttachment` control download-related
  behavior.
* :class:`~imgproxykit.options.Raw` and
  :class:`~imgproxykit.options.SkipProcessing` control serving the source
  without the usual
  processing; consult their API entries for the differences.

Omitted and explicit values
---------------------------

Omitted option arguments remain ``None`` and leave their values to imgproxy.
Explicit ``False`` and zero values are preserved in the URL; they are not
silently omitted. Booleans are serialized as ``1`` or ``0``.

Type annotations describe accepted argument types. They do not imply that
every value is validated at runtime or that the server supports every option.
Refer to each option's documentation for its meaning and requirements.

Next steps
----------

* :doc:`../api-reference/options` — all built-in options and their arguments.
* :doc:`../api-reference/types` — supported formats, positions, and other
  values.
* :doc:`transformations` — reuse options and combine them with presets.
