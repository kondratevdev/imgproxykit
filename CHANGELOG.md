# Version history

We will follow [Semantic Versioning](https://semver.org/) starting with the `1.0.0` release.
While in `Development Status :: 3 - Alpha` - we will break
all the things without any notices.

After `Development Status :: 4 - Beta` we will still break things
but with a deprecation period.


## 0.5.0 WIP

### Features

- Added `Resize`, `Padding`, and `Background` factories to select resizing
  strategies, configure uniform or symmetric padding, and set or explicitly
  disable background colors, #107
- Added `Client(source_encoding='plain')` to generate URLs with
  percent-encoded sources and imgproxy's `/plain/` marker. Base64 remains
  the default, #106
- Added `Gravity` factories to configure crop positioning without
  using protocol codes, #104
- Added `Transform.extend()` to create a new transformation with additional
  typed options and scalar keyword arguments, preserving the original, #103
- Added `Option.short_name` with documented processing option aliases and
  `Client(use_short_options=True)` to use them in URLs. Full names remain
  the default; options without a separate alias inherit `None`, #79
- Added Django REST Framework integration with read-only serializer fields
  for image URLs and named variants. Reuses Django settings, transformations,
  and source resolution. Supports source strings and model file fields.
  Install with `pip install 'imgproxykit[drf]'`, #77

### Breaking changes

- `PathSerializer` now requires the `source_encoding` keyword-only argument.
  Custom path serializer constructors must accept it. Pass `'base64'` to
  retain the previous source URL representation, #106
- Renamed `arguments_separator` to `argument_separator`,
  and `unsigned_signature` to `unsigned_marker` in `Client`, its serializer
  and signer components, and Django client settings. Update keyword arguments,
  Django settings, and custom component constructors to use the new names, #102
- Removed `imgproxykit.types.OptionType`. Processing option names now use
  `str`, allowing custom options to define their own protocol names, #79
- `PathSerializer` now requires the `use_short_options`
  keyword-only argument, #80

## 0.4.0

### Features

- Added Django integration to configure clients through Django settings
  and generate image URLs and named variants with Python shortcuts
  and template tags. Supports model file fields, reusable named
  transformations, and custom source resolvers.
  Install with `pip install 'imgproxykit[django]'`, #66
- Added FastAPI integration with support for multiple named clients.
  Install with `pip install 'imgproxykit[fastapi]'`, #64
- Added `Client.variants` to generate named image URLs for a single source
  from a mapping of complete transformations. The returned dictionary
  preserves the names, order, and types of variant keys,
  including literal string unions, #59

### Misc

- Added runnable examples to the user guide and API reference, #62
- Added a Variants guide covering reusable transformation sets and typed
  variant names, with examples of transformation composition.
  Updated the README and Getting started to focus on local sources
  and named variants, #59

## 0.3.0

### Breaking changes

- Configuration defaults now live only in `Client`. Direct construction of
  `PathSerializer` requires `arguments_separator`; `UrlSigner` requires
  `key`, `salt`, `signature_size`, and `unsigned_signature`.
  Pass `key=None` and `salt=None` for unsigned signing. `Client` defaults
  are unchanged, #57
- `Preset` now takes preset names as positional arguments, so
  `Preset('thumbnail', 'watermarked')` replaces
  `Preset(names=('thumbnail', 'watermarked'))`. Supplied names keep their
  order, #27
- Added `arguments_separator` parameter to `Client` and `PathSerializer`
  to match `IMGPROXY_ARGUMENTS_SEPARATOR`, defaults to `:`.
  `Client` now passes it to `path_serializer_cls`, so custom path serializer
  constructors must accept this keyword argument, #26

### Misc

- Switched documentation to Sphinx-Immaterial with built-in tabs,
  highlighted API signatures, and streamlined navigation, #58
- Added issue and pull request templates, an AI policy,
  and updated contribution guidelines, #56
- Clarified source and imgproxy URLs with consistent naming across
  documentation examples. Expanded type documentation and added links
  to the API reference and imgproxy settings, #54

## 0.2.1

### Breaking changes

- Replaced the `presets` argument of `Client.url` and `PathBuilder`
  with the `Preset` option, which can be combined with other
  processing options in `Transform`, #12
- Removed the `format` argument of `Client.url`, the `output_format`
  argument of `PathBuilder`, and the `Transform.format` attribute.
  Use `Transform(Format('webp'))` or `Transform(format='webp')` instead.
  Output formats are now serialized as processing options,
  like `format:webp`, instead of source URL extensions, #12 and #18
- `Transform` now accepts option instances as positional arguments
  instead of an `options` tuple. Replace
  `Transform(options=(Resize(width=300), Quality(85)))`
  with `Transform(Resize(width=300), Quality(85))`, #14
- Removed `imgproxykit.builders.PathBuilder`, use
  `imgproxykit.serialization.PathSerializer` instead.
  Renamed `Client.path_builder_cls` to `Client.path_serializer_cls`
- Renamed `imgproxykit.signing.URLSigner` to `UrlSigner`
  and `Client.signer_cls` to `Client.url_signer_cls`, #15
- Removed `imgproxykit.types.EMPTY`. Omitted option arguments,
  signing credentials, and transforms now default to `None`.
  Use `None` instead of `EMPTY` when explicitly omitting a value
- Processing options now use full imgproxy names, like `resize`,
  `width`, and `quality`, instead of `rs`, `w`, and `q`.
  This changes generated URLs and their signatures.
  `OptionType` now lists full names as well, #19
- Custom options must now define `name` as a class attribute
  instead of `_name`

### Features

- Added `unsigned_signature` parameter to `Client` and `UrlSigner`
  to customize the unsigned URL marker, defaults to `unsafe`, #6
- Added `signature_size` parameter to `Client` and `UrlSigner`
  to truncate signatures to match `IMGPROXY_SIGNATURE_SIZE`, #6
- Added scalar keyword arguments to `Transform`, like
  `Transform(width=300, quality=85, format='webp')`.
  They are appended after positional options in keyword order, #20
- Added `ScalarOption` base class for single-value options.
  Subclasses are registered by processing option name and can be
  constructed with `ScalarOption.from_kwarg`, #20
- All single-value options now accept positional values,
  like `Blur(2)` and `Rotate(90)`, #14
- Added `Option.validate` hook, called when an option is constructed,
  for custom argument validation
- Processing option classes can now be subclassed
- Added `ty` type checking to local checks and CI, #22

### Bugfixes

- Fixed northwest and southwest position codes in `Position`
  and `WatermarkPosition`: use `nowe` and `sowe`
  instead of the invalid `now` and `sow`

### Misc

- Added API Reference documentation for the public API, #5
- Added integration tests against an imgproxy server using Docker,
  covering processing options, presets, signing, and source URLs
- Expanded unit tests and enabled doctests for docstrings,
  documentation, and `README.md`, #7
- Reworked documentation with the Sphinx Material theme, a new home page,
  Getting started, and user guides for clients, transformations, and
  processing options. Added linted, type-checked Python examples with
  pytest doctests, #23

## Version 0.1.0

- Initial release
