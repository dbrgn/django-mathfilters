##################
django-mathfilters
##################

django-mathfilters is a pip-installable module that provides different simple
math filters for Django.

Django provides an ``add`` template filter, but no corresponding subtracting,
multiplying or dividing filters.

Django ticket `#361 <https://code.djangoproject.com/ticket/361>`_ has been
closed as *wontfix*, so I had to create an alternative that is easy to install
in a new Django project.


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


License
=======

`MIT License <http://www.tldrlegal.com/license/mit-license>`_, see LICENSE file.
