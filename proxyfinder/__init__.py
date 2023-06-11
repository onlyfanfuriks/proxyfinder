"""
Copyright © 2023 Onlyfanfuriks <onlyfanfuriks@gmail.com>. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__title__ = 'ProxyFinder'
__package__ = 'proxyfinder'
__version__ = '0.0.1'
__short_description__ = 'Proxy finder and checker. Finds public proxies from multiple sources and concurrently checks them. Supports HTTP(S) and SOCKS4/5.'  # noqa
__author__ = 'Onlyfanfuriks'
__author_email__ = 'onlyfanfuriks@gmail.com'
__url__ = 'https://github.com/onlyfanfuriks/proxyfinder'
__license__ = 'The MIT License (MIT)'
__copyright__ = 'Copyright 2023 Onlyfanfuriks'


import logging  # noqa
import warnings  # noqa

from .api import Broker  # noqa
from .checker import Checker  # noqa
from .judge import Judge  # noqa
from .providers import Provider  # noqa
from .proxy import Proxy  # noqa
from .server import ProxyPool, Server  # noqa

logger = logging.getLogger('asyncio')
logger.addFilter(logging.Filter('has no effect when using ssl'))

warnings.simplefilter('always', UserWarning)
warnings.simplefilter('once', DeprecationWarning)


__all__ = (Proxy, Judge, Provider, Checker, Server, ProxyPool, Broker)
