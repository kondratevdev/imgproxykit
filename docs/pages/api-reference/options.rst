Processing options
==================

Import built-in options from ``imgproxykit.options`` and pass their instances
to the :class:`~imgproxykit.Transform` constructor. Constructors describe
accepted
arguments; imgproxy applies processing behavior and server defaults.

Scalar options accept their ``value`` either positionally or by keyword,
for example ``Blur(2)`` or ``Blur(value=2)``. Options with multiple arguments
and options accepting structured values use keyword-only arguments, except
:class:`~imgproxykit.options.Preset`, which accepts preset names as positional
arguments.

Base option
-----------

.. autoclass:: imgproxykit.options.Option
   :members:

Built-in options
----------------

AutoRotate
~~~~~~~~~~

.. autoclass:: imgproxykit.options.AutoRotate
   :members:

Background
~~~~~~~~~~

.. autoclass:: imgproxykit.options.Background
   :members:

Blur
~~~~

.. autoclass:: imgproxykit.options.Blur
   :members:

CacheBuster
~~~~~~~~~~~

.. autoclass:: imgproxykit.options.CacheBuster
   :members:

Crop
~~~~

.. autoclass:: imgproxykit.options.Crop
   :members:

DPR
~~~

.. autoclass:: imgproxykit.options.DPR
   :members:

EnforceThumbnail
~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.EnforceThumbnail
   :members:

Enlarge
~~~~~~~

.. autoclass:: imgproxykit.options.Enlarge
   :members:

Expires
~~~~~~~

.. autoclass:: imgproxykit.options.Expires
   :members:

Extend
~~~~~~

.. autoclass:: imgproxykit.options.Extend
   :members:

ExtendAspectRatio
~~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.ExtendAspectRatio
   :members:

Filename
~~~~~~~~

.. autoclass:: imgproxykit.options.Filename
   :members:

Flip
~~~~

.. autoclass:: imgproxykit.options.Flip
   :members:

Format
~~~~~~

.. autoclass:: imgproxykit.options.Format
   :members:

FormatQuality
~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.FormatQuality
   :members:

Gravity
~~~~~~~

.. autoclass:: imgproxykit.options.Gravity
   :members:

Height
~~~~~~

.. autoclass:: imgproxykit.options.Height
   :members:

KeepCopyright
~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.KeepCopyright
   :members:

MaxAnimationFrameResolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.MaxAnimationFrameResolution
   :members:

MaxAnimationFrames
~~~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.MaxAnimationFrames
   :members:

MaxBytes
~~~~~~~~

.. autoclass:: imgproxykit.options.MaxBytes
   :members:

MaxResultDimension
~~~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.MaxResultDimension
   :members:

MaxSrcFileSize
~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.MaxSrcFileSize
   :members:

MaxSrcResolution
~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.MaxSrcResolution
   :members:

MinHeight
~~~~~~~~~

.. autoclass:: imgproxykit.options.MinHeight
   :members:

MinWidth
~~~~~~~~

.. autoclass:: imgproxykit.options.MinWidth
   :members:

Padding
~~~~~~~

.. autoclass:: imgproxykit.options.Padding
   :members:

Pixelate
~~~~~~~~

.. autoclass:: imgproxykit.options.Pixelate
   :members:

Preset
~~~~~~

.. autoclass:: imgproxykit.options.Preset
   :members:

PreserveHDR
~~~~~~~~~~~

.. autoclass:: imgproxykit.options.PreserveHDR
   :members:

Quality
~~~~~~~

.. autoclass:: imgproxykit.options.Quality
   :members:

Raw
~~~

.. autoclass:: imgproxykit.options.Raw
   :members:

Resize
~~~~~~

.. autoclass:: imgproxykit.options.Resize
   :members:

ResizingType
~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.ResizingType
   :members:

ReturnAttachment
~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.ReturnAttachment
   :members:

Rotate
~~~~~~

.. autoclass:: imgproxykit.options.Rotate
   :members:

Sharpen
~~~~~~~

.. autoclass:: imgproxykit.options.Sharpen
   :members:

Size
~~~~

.. autoclass:: imgproxykit.options.Size
   :members:

SkipProcessing
~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.SkipProcessing
   :members:

StripColorProfile
~~~~~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.StripColorProfile
   :members:

StripMetadata
~~~~~~~~~~~~~

.. autoclass:: imgproxykit.options.StripMetadata
   :members:

Trim
~~~~

.. autoclass:: imgproxykit.options.Trim
   :members:

Watermark
~~~~~~~~~

.. autoclass:: imgproxykit.options.Watermark
   :members:

Width
~~~~~

.. autoclass:: imgproxykit.options.Width
   :members:

Zoom
~~~~

.. autoclass:: imgproxykit.options.Zoom
   :members:

