##################
django-mathfilters
##################

.. image:: https://secure.travis-ci.org/dbrgn/django-mathfilters.png?branch=master
    :alt: Build status
    :target: http://travis-ci.org/dbrgn/django-mathfilters

.. image:: https://coveralls.io/repos/dbrgn/django-mathfilters/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/dbrgn/django-mathfilters

.. image:: https://pypip.in/d/django-mathfilters/badge.png
    :alt: PyPI download stats
    :target: https://crate.io/packages/django-mathfilters


django-mathfilters is a pip-installable module that provides different simple
math filters for Django.

Django provides an ``add`` template filter, but no corresponding subtracting,
multiplying or dividing filters.

Django ticket `#361 <https://code.djangoproject.com/ticket/361>`_ has been
closed as *wontfix*, so I had to create an alternative that is easy to install
in a new Django project.

It currently supports ``int``, ``float``, ``Decimal`` and ``cDecimal`` types, or
any other type that can be converted to int or float.


Installation
============

::

    $ pip install django-mathfilters

Then add ``mathfilters`` to your ``INSTALLED_APPS``.


Usage
=====

You need to load ``mathfilters`` at the top of your template. The script
provides the following filters:

* ``sub`` – subtraction
* ``mul`` – multiplication
* ``div`` – division
* ``abs`` – absolute value
* ``mod`` – modulo

**Example:**

::

    {% load mathfilters %}

    ...

    <h1>Basic math filters</h1>

    <ul>
        <li>8 + 3 = {{ 8|add:3 }}</li>

        <li>13 - 17 = {{ 13|sub:17 }}</li>

        {% with answer=42 %}
        <li>42 * 0.5 = {{ answer|mul:0.5 }}</li>
        {% endwith %}

        {% with numerator=12 denominator=3 %}
        <li>12 / 3 = {{ numerator|div:denominator }}</li>
        {% endwith %}

        <li>|-13| = {{ -13|abs }}</li>
    </ul>


Changelog
=========

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


License
=======

`MIT License <http://www.tldrlegal.com/license/mit-license>`_, see LICENSE file.
