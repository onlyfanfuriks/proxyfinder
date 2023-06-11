
API Reference
=============


.. _proxyfinder-api-broker:

Broker
------

.. autoclass:: proxyfinder.api.Broker
    :members: grab, find, serve, stop, show_stats


.. _proxyfinder-api-proxy:

Proxy
-----

.. autoclass:: proxyfinder.proxy.Proxy
    :members: create, types, is_working, avg_resp_time, geo, error_rate, get_log
    :member-order: groupwise


.. _proxyfinder-api-provider:

Provider
--------

.. autoclass:: proxyfinder.providers.Provider
    :members: proxies, get_proxies
    :member-order: groupwise
