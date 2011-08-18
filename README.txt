WsgiUnproxy
===========

When an HTTP proxy forwards traffic to a webserver, the server sees the proxy
IP address rather than the original client IP address. Since the server may
need the IP address for logging or authentication purposes, many HTTP proxies
add an ``X-Forwarded-For`` header indicating the original client IP address.

As WSGI middleware, WsgiUnproxy sits between the WSGI server and your WSGI
application. Before your application sees a request, WsgiUnproxy removes the
``X-Forwarded-For`` header and reinstates the client IP address, yielding a
request that looks like it was never proxied to begin with.

Since anyone can add an ``X-Forwarded-For`` header, WsgiUnproxy only uses the
header if it comes from a trusted proxy IP addresses.


Example WSGI application
------------------------

::

    from wsgiunproxy import unproxy

    @unproxy(trusted_proxies=[ '1.2.3.4', '5.6.7.8' ])
    def application(environ, start_response):
        start_response('200 OK', [])
        return ['Your IP address is %s.' % environ.get('REMOTE_ADDR')]


Use with Paste Deployment
-------------------------

WsgiUnproxy can be used in a Paste Deployment pipeline::

    [pipeline:main]
    pipeline =
        WsgiUnproxy
        MyApp

    [filter:WsgiUnproxy]
    use = egg:WsgiUnproxy
    trusted_proxies = 1.2.3.4, 5.6.7.8


Advanced use
------------

If you need to specify a lot of trusted proxies (such as a whole subnet), you
don't have to use give ``trusted_proxies`` as a list. All that WsgiUnproxy asks
is that ``trusted_proxies`` supports the ``in`` operator (e.g. by implementing
``__contains__``).


License
-------

To the extent possible under law, the author has waived all copyright and
related or neighboring rights to WsgiUnproxy.

For more information see:
http://creativecommons.org/publicdomain/zero/1.0/
