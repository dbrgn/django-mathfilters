Changelog
=========

Possible log types are ``[add]``, ``[bug]``, ``[change]`` and ``[info]``.

---

v1.0.0 (2020-02-10)

- [change] Drop support for Python <3.3 and Django <1.11
- [change] Drop support for cdecimal (#20)

v0.4.0 (2016-04-12)

- [add] New float/decimal friendly ``addition`` filter

v0.3.0 (2014-07-22)

- [add] New ``intdiv`` filter for integer division
- [bug] Fixed an encoding bug in ``setup.py``
- [info] Python 3.4 and Django 1.6 support

v0.2.1 (2013-10-09)

- [add] Use ``cdecimal`` instead of ``decimal`` if available
- [add] When combining ``float`` and ``Decimal`` values, automatically convert
  float to Decimal

v0.2.0 (2013-07-23)

- [add] New ``mod`` filter

v0.1.3 (2012-12-04)

- [add] Support for ``Decimal`` type

v0.1.2 (2012-10-09)

- [add] Initial version
