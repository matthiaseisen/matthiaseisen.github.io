.. header:: `Home </>`_ > `Pillow by Example </pillow/>`_ > `Basics </pillow/basics/>`_ > `Crop </pillow/basics/crop/>`_

Pillow by Example
~~~~~~~~~~~~~~~~~

Cropping Images
===============

.. contents::
    :depth: 2
    :backlinks: top

.. sectnum::

Preparations
------------

Import Pillow:

.. include:: crop.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

Load the original image:

.. include:: crop.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

.. figure:: flowers.jpg

    The original image (250px * 188px)

Cropping
--------

100px * 100px starting at the top-left corner
.............................................

.. include:: crop.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

.. figure:: img2.jpg

    Cropped to 100px * 100px starting at the top-left corner

100px * 100px starting at the bottom-right corner
.................................................

.. include:: crop.py
    :code: python
    :start-after: # -(3)
    :end-before: # -(/3)

.. figure:: img3.jpg

    100px * 100px starting at the bottom-right corner

100px * 150px starting in the center
....................................

.. include:: crop.py
    :code: python
    :start-after: # -(4)
    :end-before: # -(/4)

.. figure:: img4.jpg

    100px * 150px starting in the center

Pad the image to a square
.........................

.. include:: crop.py
    :code: python
    :start-after: # -(5)
    :end-before: # -(/5)

.. figure:: img5.jpg

    Padded to a square

.. footer:: Copyright 2014 `Matthias Eisen </>`__
