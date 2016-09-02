# A relatively simple WSGI application.
import sys
from wsgiref.util import setup_testing_defaults
from datetime import datetime
import time

started = datetime.now()
accessed = 0


def application(environ, start_response):
    global accessed
    setup_testing_defaults(environ)

    accessed = accessed + 1
    delta = datetime.now() - started
    elapsed = time.strftime('%H:%M:%S', time.gmtime(delta.total_seconds()))

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    content = []
    content.append('## App uwsgi python %s' % sys.version_info.major)
    content.append('App started on %s' % started)
    content.append('App accessed %s times' % accessed)
    content.append('App running for %s' % elapsed)
    return '\n'.join(content)
