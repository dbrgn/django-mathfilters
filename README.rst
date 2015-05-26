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


django-mathfilters is a pip-installable Python 2/3 module that provides
different simple math filters for Django.

Django provides an ``add`` template filter, but no corresponding subtracting,
multiplying or dividing filters.

Django ticket `#361 <https://code.djangoproject.com/ticket/361>`_ has been
closed as *wontfix*, so I had to create an alternative that is easy to install
in a new Django project.

It currently supports ``int``, ``float``, ``Decimal`` and ``cDecimal`` types, or
any other type that can be converted to int or float.

**WARNING: Note that when you have the ``cdecimal`` package installed, I assume
all ``Decimal`` values that are passed to the tag are of ``cdecimal`` type. If
they aren't, weird things may happen.**


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
* ``intdiv`` – integer (floor) division
* ``abs`` – absolute value
* ``mod`` – modulo
* ``addition`` – replacement for the ``add`` filter with support for float /
  decimal types

**Example:**

.. sourcecode:: html

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


Version Support
===============

This module supports Python 2.6–2.7 and 3.2–3.4 as well as PyPy and PyPy3.

Supported Django versions are 1.1 through 1.8.

See https://travis-ci.org/dbrgn/django-mathfilters for the full build matrix.


License
=======

`MIT License <http://www.tldrlegal.com/license/mit-license>`_, see LICENSE file.
