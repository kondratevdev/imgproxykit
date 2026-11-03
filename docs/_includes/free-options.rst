Dimensions and cropping
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 50 14 8
   :width: 100%
   :class: options-table

   * - Option
     - Description
     - imgproxy
     - Pro
   * - :class:`~imgproxykit.options.Resize`
     - Configure image dimensions and resizing behavior.
     - `Docs <https://docs.imgproxy.net/usage/processing#resize>`__
     - —
   * - :class:`~imgproxykit.options.Size`
     - Set target dimensions, upscaling, and canvas extension.
     - `Docs <https://docs.imgproxy.net/usage/processing#size>`__
     - —
   * - :class:`~imgproxykit.options.ResizingType`
     - Choose the resizing strategy.
     - `Docs <https://docs.imgproxy.net/usage/processing#resizing-type>`__
     - —
   * - :class:`~imgproxykit.options.Width`
     - Set the target width in pixels.
     - `Docs <https://docs.imgproxy.net/usage/processing#width>`__
     - —
   * - :class:`~imgproxykit.options.Height`
     - Set the target height in pixels.
     - `Docs <https://docs.imgproxy.net/usage/processing#height>`__
     - —
   * - :class:`~imgproxykit.options.MinWidth`
     - Set the minimum resulting width in pixels.
     - `Docs <https://docs.imgproxy.net/usage/processing#min-width>`__
     - —
   * - :class:`~imgproxykit.options.MinHeight`
     - Set the minimum resulting height in pixels.
     - `Docs <https://docs.imgproxy.net/usage/processing#min-height>`__
     - —
   * - :class:`~imgproxykit.options.Zoom`
     - Multiply dimensions by one factor or separate X and Y factors.
     - `Docs <https://docs.imgproxy.net/usage/processing#zoom>`__
     - —
   * - :class:`~imgproxykit.options.DPR`
     - Scale an image for high pixel density displays.
     - `Docs <https://docs.imgproxy.net/usage/processing#dpr>`__
     - —
   * - :class:`~imgproxykit.options.Enlarge`
     - Allow upscaling smaller source images.
     - `Docs <https://docs.imgproxy.net/usage/processing#enlarge>`__
     - —
   * - :class:`~imgproxykit.options.Extend`
     - Extend the canvas to the target dimensions.
     - `Docs <https://docs.imgproxy.net/usage/processing#extend>`__
     - —
   * - :class:`~imgproxykit.options.ExtendAspectRatio`
     - Extend the canvas to the requested aspect ratio.
     - `Docs <https://docs.imgproxy.net/usage/processing#extend-aspect-ratio>`__
     - —
   * - :class:`~imgproxykit.options.Gravity`
     - Choose the image area retained when cropping.
     - `Docs <https://docs.imgproxy.net/usage/processing#gravity>`__
     - —
   * - :class:`~imgproxykit.options.Crop`
     - Crop before resizing; dimensions below one are relative.
     - `Docs <https://docs.imgproxy.net/usage/processing#crop>`__
     - —
   * - :class:`~imgproxykit.options.Trim`
     - Trim the surrounding background with optional color and symmetry.
     - `Docs <https://docs.imgproxy.net/usage/processing#trim>`__
     - —
   * - :class:`~imgproxykit.options.Padding`
     - Add padding using CSS side order; specify at least one side.
     - `Docs <https://docs.imgproxy.net/usage/processing#padding>`__
     - —

Orientation and effects
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 50 14 8
   :width: 100%
   :class: options-table

   * - Option
     - Description
     - imgproxy
     - Pro
   * - :class:`~imgproxykit.options.AutoRotate`
     - Apply the source EXIF orientation before processing.
     - `Docs <https://docs.imgproxy.net/usage/processing#auto-rotate>`__
     - —
   * - :class:`~imgproxykit.options.Rotate`
     - Rotate clockwise by a multiple of 90 degrees.
     - `Docs <https://docs.imgproxy.net/usage/processing#rotate>`__
     - —
   * - :class:`~imgproxykit.options.Flip`
     - Flip the image horizontally and/or vertically.
     - `Docs <https://docs.imgproxy.net/usage/processing#flip>`__
     - —
   * - :class:`~imgproxykit.options.Blur`
     - Apply Gaussian blur with the given sigma.
     - `Docs <https://docs.imgproxy.net/usage/processing#blur>`__
     - —
   * - :class:`~imgproxykit.options.Sharpen`
     - Apply sharpening with the given sigma.
     - `Docs <https://docs.imgproxy.net/usage/processing#sharpen>`__
     - —
   * - :class:`~imgproxykit.options.Background`
     - Fill the background with a hex or RGB color, or explicitly disable filling.
     - `Docs <https://docs.imgproxy.net/usage/processing#background>`__
     - —
   * - :class:`~imgproxykit.options.Watermark`
     - Apply the watermark image configured on the imgproxy server.
     - `Docs <https://docs.imgproxy.net/usage/processing#watermark>`__
     - —
   * - :class:`~imgproxykit.options.Pixelate`
     - Set the pixelation block size.
     - `Docs <https://docs.imgproxy.net/usage/processing#pixelate>`__
     - —

Output and quality
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 50 14 8
   :width: 100%
   :class: options-table

   * - Option
     - Description
     - imgproxy
     - Pro
   * - :class:`~imgproxykit.options.Format`
     - Set the output image format.
     - `Docs <https://docs.imgproxy.net/usage/processing#format>`__
     - —
   * - :class:`~imgproxykit.options.Quality`
     - Set output image quality.
     - `Docs <https://docs.imgproxy.net/usage/processing#quality>`__
     - —
   * - :class:`~imgproxykit.options.FormatQuality`
     - Set quality for each supplied output format.
     - `Docs <https://docs.imgproxy.net/usage/processing#format-quality>`__
     - —
   * - :class:`~imgproxykit.options.MaxBytes`
     - Reduce output quality to meet the requested byte limit.
     - `Docs <https://docs.imgproxy.net/usage/processing#max-bytes>`__
     - —
   * - :class:`~imgproxykit.options.SkipProcessing`
     - Skip processing listed formats when source and output formats match.
     - `Docs <https://docs.imgproxy.net/usage/processing#skip-processing>`__
     - —
   * - :class:`~imgproxykit.options.Raw`
     - Stream the unchecked source file without processing.
     - `Docs <https://docs.imgproxy.net/usage/processing#raw>`__
     - —
   * - :class:`~imgproxykit.options.EnforceThumbnail`
     - Use an embedded HEIC or AVIF thumbnail when available.
     - `Docs <https://docs.imgproxy.net/usage/processing#enforce-thumbnail>`__
     - —

Metadata and color
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 50 14 8
   :width: 100%
   :class: options-table

   * - Option
     - Description
     - imgproxy
     - Pro
   * - :class:`~imgproxykit.options.StripMetadata`
     - Remove image metadata.
     - `Docs <https://docs.imgproxy.net/usage/processing#strip-metadata>`__
     - —
   * - :class:`~imgproxykit.options.KeepCopyright`
     - Preserve copyright information when stripping metadata.
     - `Docs <https://docs.imgproxy.net/usage/processing#keep-copyright>`__
     - —
   * - :class:`~imgproxykit.options.StripColorProfile`
     - Convert the embedded profile to sRGB and remove it.
     - `Docs <https://docs.imgproxy.net/usage/processing#strip-color-profile>`__
     - —
   * - :class:`~imgproxykit.options.PreserveHDR`
     - Preserve high bit depth instead of converting to 8 bit.
     - `Docs <https://docs.imgproxy.net/usage/processing#preserve-hdr>`__
     - —

Limits
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 50 14 8
   :width: 100%
   :class: options-table

   * - Option
     - Description
     - imgproxy
     - Pro
   * - :class:`~imgproxykit.options.MaxSrcResolution`
     - Override source megapixel limit.
     - `Docs <https://docs.imgproxy.net/usage/processing#max-src-resolution>`__
     - —
   * - :class:`~imgproxykit.options.MaxSrcFileSize`
     - Override source byte limit.
     - `Docs <https://docs.imgproxy.net/usage/processing#max-src-file-size>`__
     - —
   * - :class:`~imgproxykit.options.MaxAnimationFrames`
     - Override animation frame limit.
     - `Docs <https://docs.imgproxy.net/usage/processing#max-animation-frames>`__
     - —
   * - :class:`~imgproxykit.options.MaxAnimationFrameResolution`
     - Override frame megapixel limit.
     - `Docs <https://docs.imgproxy.net/usage/processing#max-animation-frame-resolution>`__
     - —
   * - :class:`~imgproxykit.options.MaxResultDimension`
     - Override output dimension limit.
     - `Docs <https://docs.imgproxy.net/usage/processing#max-result-dimension>`__
     - —

URL and response
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 50 14 8
   :width: 100%
   :class: options-table

   * - Option
     - Description
     - imgproxy
     - Pro
   * - :class:`~imgproxykit.options.Preset`
     - Reference named presets configured on the imgproxy server.
     - `Docs <https://docs.imgproxy.net/usage/processing#preset>`__
     - —
   * - :class:`~imgproxykit.options.CacheBuster`
     - Add an escaped version string to the signed URL to bypass caches.
     - `Docs <https://docs.imgproxy.net/usage/processing#cache-buster>`__
     - —
   * - :class:`~imgproxykit.options.Expires`
     - Reject the URL after the given Unix timestamp.
     - `Docs <https://docs.imgproxy.net/usage/processing#expires>`__
     - —
   * - :class:`~imgproxykit.options.Filename`
     - Set the response filename using URL-safe Base64 encoding.
     - `Docs <https://docs.imgproxy.net/usage/processing#filename>`__
     - —
   * - :class:`~imgproxykit.options.ReturnAttachment`
     - Request attachment disposition for downloading.
     - `Docs <https://docs.imgproxy.net/usage/processing#return-attachment>`__
     - —

