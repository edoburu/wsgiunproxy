def unproxy(trusted_proxies):
    """ Decorates a WSGI application function, rewriting HTTP_X_FORWARDED_FOR
        and REMOTE_ADDR in the WSGI environment to present the true remote IP
        address to the wrapped WSGI application.

        trusted_proxies is a list or set of proxy IP addresses that are trusted
        to provide a true X-Forwarded-For header.
    """

    def decorator(wsgi_app):
        def application(environ, start_response):
            remote_addr = environ.get('REMOTE_ADDR')
            x_forwarded_for = environ.get('HTTP_X_FORWARDED_FOR')

            def env_set(key, value):
                """ Sets or deletes the given key in the environ dict. """
                if value:
                    environ[key] = value
                elif key in environ:
                    del environ[key]

            while remote_addr in trusted_proxies and x_forwarded_for:
                # Extract the right-most (latest) ip from X-Forwarded-For
                i = x_forwarded_for.rfind(',')
                remote_addr= x_forwarded_for[i + 1:].strip()
                x_forwarded_for = x_forwarded_for[0:i].strip() if i >= 0 else None

            env_set('REMOTE_ADDR', remote_addr)
            env_set('HTTP_X_FORWARDED_FOR', x_forwarded_for)

            return wsgi_app(environ, start_response)

        return application

    return decorator


def paste_filter_factory(global_config, **settings):
    """ Provide a filter factory for Paste Deployment. """

    trusted_proxies=set(proxy.strip() for proxy in settings['trusted_proxies'].split(','))
    return unproxy(trusted_proxies=trusted_proxies)
