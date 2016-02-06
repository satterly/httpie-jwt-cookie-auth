httpie-jwt-cookie-auth
======================

`JWT <https://tools.ietf.org/html/rfc7519>`_ Cookie auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.

HTTP requests will have a cookie called ``access_token`` set to the supplied JWT token and if the JWT token includes an ``xsrfToken`` claim it will be extracted and the value added as the ``X-XSRF-TOKEN`` header.

This method of presenting a JWT token via cookies and including the XSRF token in the JWT is advocated by `Stormpath <https://stormpath.com/blog/where-to-store-your-jwts-cookies-vs-html5-web-storage/>`_ to overcome the security concerns of local storage, sessions and `Cross-Site Request Forgery attacks <https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)>`_. A claim set with an ``xsrfToken`` looks like the following:

.. code-block:: javascript

    {
      "sub": "1234567890",
      "name": "John Doe",
      "admin": true,
      "xsrfToken": "5tjRtlJYSiSh$w*sY%maphAnvDYGu6s0"
    }

Example with Cookie and XSRF headers

.. code-block:: bash

    GET / HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Cookie: access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsInhzcmZUb2tlbiI6IjV0alJ0bEpZU2lTaCR3KnNZJW1hcGhBbnZEWUd1NnMwIn0.BpA85MrtO7U8UvAsSwuoQcTDKwMDqMGwA1y6pscskC0
    Host: www.google.com
    User-Agent: HTTPie/0.9.3
    X-XSRF-TOKEN: 5tjRtlJYSiSh$w*sY%maphAnvDYGu6s0

Installation
------------

.. code-block:: bash

    $ pip install httpie-jwt-cookie-auth

You should now see ``jwt-cookie`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=jwt-cookie --auth='jwt:secret' example.org

Configuration
-------------

By default, the cookie is called ``access_token`` and the XSRF header is called ``X-XSRF-TOKEN`` however both can be overridden using configuration file settings, for example:

.. code-block:: javascript

    {
        "jwt_cookie_name": "id_token",
        "jwt_xsrf_header": "Csrf-Token"
    }

Examples
--------

To authenticate a client request when a JWT must be verified before use include the secret:

.. code-block:: bash

    $ http --auth-type=hmac --auth="jwt:secret" example.org

To authenticate a client request when there is no requirement for the JWT to be verified:

.. code-block:: bash

    $ http --auth-type=hmac --auth="jwt:" example.org

License
-------

Copyright (c) 2016 Nick Satterly. Available under the MIT License.
