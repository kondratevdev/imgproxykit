.. admonition:: Run imgproxy locally
    :collapsible: closed

    The examples use a local imgproxy server at ``http://localhost:8080``.

    Start this container to try the examples:

    .. code-block:: bash

        docker run -d --rm \
          --name imgproxy-guide \
          -p 127.0.0.1:8080:8080 \
          -e 'IMGPROXY_ALLOW_SECURITY_OPTIONS=true' \
          -e 'IMGPROXY_PRESETS=thumbnail=resize:fill:300:300,small=resize:fill:96:96' \
          ghcr.io/imgproxy/imgproxy:v4.0.0

    This server accepts unsigned URLs and enables security options used in
    the examples. If the container is already running, reuse it.
    Run an example and open the printed URL in your browser.

    When finished, stop the container:

    .. code-block:: bash

        docker stop imgproxy-guide

