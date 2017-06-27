Django SizedImageField
======================


What is it ?
------------

SizedImageField is a Django field which will automatically resize image to fit a defined dimension.
Because it inherits from ImageField, all the usual ImageField attributes are available.
It uses PIL which is already a requirement to use Django ImageField.


Example
-------

.. code-block:: python

    from sizedimagefield.fields import SizedImageField

    class Article(models.Model):

        thumbnail = SizedImageField('thumbnail', width=150, height=150, upload_to='articles/')



Compatibilities
---------------

It has only been tested with Django 1.11 and Python 3.6.


Installation
------------

Installing from pypi (using pip). ::

    pip install django-sizedimagefield


Installing from github. ::

    pip install -e git://github.com/makinacorpus/django-sizedimagefield.git#egg=django-sizedimagefield

Add ``sizedimagefield`` in your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        'sizedimagefield',
        [...]
    ]


The application doesn't have any special requirement.


Licensing
---------

Please see the LICENSE file.

Contacts
--------

.. image:: https://drupal.org/files/imagecache/grid-3/Logo_slogan_300dpi.png
    :target: http://www.makina-corpus.com
