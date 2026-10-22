# Сверка processing options

Дата: 2026-10-22. Сравнение с [официальной документацией 4.0.x](https://docs.imgproxy.net/usage/processing#processing-options).

В [OptionType](../../imgproxykit/types.py) представлены все 45 опций без отметки Pro. Отсутствуют 39 Pro-опций:

| Группа | Опции |
| --- | --- |
| Геометрия | `resizing_algorithm`, `objects_position`, `crop_aspect_ratio` |
| Цвет и эффекты | `background_alpha`, `adjust`, `brightness`, `contrast`, `saturation`, `monochrome`, `duotone`, `unsharp_masking`, `blur_areas`, `blur_detections`, `draw_detections`, `crop_objects`, `colorize`, `gradient` |
| Watermark и SVG | `watermark_url`, `watermark_text`, `watermark_size`, `watermark_rotate`, `watermark_shadow`, `style` |
| Метаданные | `dpi`, `color_profile` |
| Сжатие | `autoquality`, `jpeg_options`, `png_options`, `webp_options`, `avif_options` |
| Страницы и анимация | `page`, `pages`, `disable_animation` |
| Видео | `video_thumbnail_second`, `video_thumbnail_keyframes`, `video_thumbnail_tile`, `video_thumbnail_animation` |
| Прочее | `fallback_image_url`, `hashsum` |

Дополнительно отсутствуют Pro-возможности существующих опций:

- `FormatType`: [`best`](https://docs.imgproxy.net/usage/processing#best-format).
- `Gravity` и `Crop`: [`obj`, `objw`](https://docs.imgproxy.net/usage/processing#gravity), списки классов и весов; текущий API имеет только позицию и два числовых смещения.
- `WatermarkPosition`: [`ch`](https://docs.imgproxy.net/usage/processing#watermark).

Проверенные локальные источники: [опции](../../imgproxykit/options/__init__.py), [типы](../../imgproxykit/types.py), [Gravity](../../imgproxykit/options/gravity.py), [Crop](../../imgproxykit/options/crop.py).

Версии окружения различаются: [интеграционные тесты](../../tests/fixtures/imgproxy.py) используют v4.0.0, [Docker Compose](../../docker-compose.yaml) — v3.31.0. Сверка касается наличия API, а не проверки всех аргументов и поведения сервера.
