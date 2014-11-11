.. header:: `Home </>`_ > `Fun with Lists </fwl/>`_ > `Python </fwl/py/>`_

Fun with Lists
~~~~~~~~~~~~~~

Python
^^^^^^

.. contents::
    :depth: 2
    :backlinks: top

.. sectnum::

Removing Elements
#################

All values equal to x
=====================

.. include:: p0029.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 5, 6, 1]


.. include:: p0029.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 5, 6, 1]


.. include:: p0029.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4, 4, 5, 6, 1, 4]
    
Duplicates
==========

.. caution::
   This approach will not preserve the order of the list items.

.. include:: p0021.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 5, 6]

First element
=============

.. include:: p0025.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    1


.. include:: p0025.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [2, 3, 4, 5, 6]


.. include:: p0025.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [2, 3, 4, 5, 6]


.. include:: p0025.py
    :code: python
    :start-after: # -(3)
    :end-before: # -(/3)

::

    [2, 3, 4, 5, 6]


.. include:: p0025.py
    :code: python
    :start-after: # -(4)
    :end-before: # -(/4)

::

    [1, 2, 3, 4, 5, 6]

Last element
============

.. include:: p0024.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    6


.. include:: p0024.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 4, 5]


.. include:: p0024.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4, 5]


.. include:: p0024.py
    :code: python
    :start-after: # -(3)
    :end-before: # -(/3)

::

    [1, 2, 3, 4, 5]


.. include:: p0024.py
    :code: python
    :start-after: # -(4)
    :end-before: # -(/4)

::

    [1, 2, 3, 4, 5, 6]

nth element
===========

.. include:: p0026.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    3


.. include:: p0026.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 4, 5, 6]


.. include:: p0026.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 4, 5, 6]


.. include:: p0026.py
    :code: python
    :start-after: # -(3)
    :end-before: # -(/3)

::

    [1, 2, 4, 5, 6]


.. include:: p0026.py
    :code: python
    :start-after: # -(4)
    :end-before: # -(/4)

::

    [1, 2, 3, 4, 5, 6]


.. include:: p0026.py
    :code: python
    :start-after: # -(5)
    :end-before: # -(/5)

::

    [1, 2, 4, 5, 6]


.. include:: p0026.py
    :code: python
    :start-after: # -(6)
    :end-before: # -(/6)

::

    [1, 2, 3, 4, 5, 6]

Replacing Elements
##################

All values equal to x
=====================

.. include:: p0033.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 0, 0, 5, 6, 1, 0]


.. include:: p0033.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 0, 0, 5, 6, 1, 0]


.. include:: p0033.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4, 4, 5, 6, 1, 4]

First element
=============

.. include:: p0030.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [0, 2, 3, 4]


.. include:: p0030.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [0, 2, 3, 4]


.. include:: p0030.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4]
    
Last element
============

.. include:: p0031.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 0]


.. include:: p0031.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 0]


.. include:: p0031.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4]
    
nth element
===========

.. include:: p0032.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 0, 4]


.. include:: p0032.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 0, 4]


.. include:: p0032.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4]
 
Sorting
#######

Alphabetically (case-insensitive)
=================================

.. include:: p0005.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    ['a', 'B', 'C', 'd']


.. include:: p0005.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    ['d', 'C', 'B', 'a']


.. include:: p0005.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    ['a', 'B', 'C', 'd']

Alphabetically (case-sensitive)
===============================

.. include:: p0004.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    ['B', 'C', 'a', 'd']


.. include:: p0004.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    ['d', 'C', 'B', 'a']


.. include:: p0004.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    ['B', 'C', 'a', 'd']

Ascending order
===============

.. include:: p0007.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    ['d', 'c', 'b', 'a']


.. include:: p0007.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    ['a', 'c', 'd', 'b']


.. include:: p0007.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    ['d', 'c', 'b', 'a']

Strings by length
=================

.. include:: p0006.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    ['B', 'dd', 'CCC', 'aaaa']


.. include:: p0006.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    ['aaaa', 'B', 'CCC', 'dd']


.. include:: p0006.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    ['B', 'dd', 'CCC', 'aaaa']
     
Other
#####

Add up all values in a list of numbers
======================================

.. include:: p0013.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    13236.1545

Append to a list
================

.. include:: p0002.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4]

Apply a function to every list element
======================================

.. include:: p0016.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    1
    2
    3
    4


.. include:: p0016.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [2, 4, 6, 8]


.. include:: p0016.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [2, 4, 6, 8]

Cartesian product of 2 lists (vectors)
======================================

.. include:: p0035.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


.. include:: p0035.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
    
Cartesian product of n lists (vectors)
======================================

.. include:: p0036.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [(0, 2, 4),
     (0, 2, 5),
     (0, 3, 4),
     (0, 3, 5),
     (1, 2, 4),
     (1, 2, 5),
     (1, 3, 4),
     (1, 3, 5)]

Check if 2 lists have at least 1 common element
===============================================

.. include:: p0056.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    True

Check if a list contains the value x
====================================

.. include:: p0012.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    yes

Count the number of times x appears in a list
=============================================

.. include:: p0014.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    2

Difference of 2 lists
=====================

.. include:: p0039.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2]


.. include:: p0039.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2]


.. include:: p0039.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2]

Difference of n lists
=====================

.. include:: p0040.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [2, 4]


.. include:: p0040.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [2, 4]

First n elements of a list
==========================

n = 2


.. include:: p0022.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2]

First n non-x elements of a list
================================

.. include:: p0034.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 3, 4]


.. include:: p0034.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 3, 4]

Flatten a list of lists
=======================

.. include:: p0043.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 5, 6, 7, 8, 9]

Insert x after the first occurence of y
=======================================

.. include:: p0046.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 5, 3, 6, 2]


.. include:: p0046.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 4, 5, 3, 6, 2]


.. include:: p0046.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 5, 3, 6, 2]

Insert x before the first occurence of y
========================================

.. include:: p0047.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 5, 4, 6, 2]


.. include:: p0047.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 4, 5, 4, 6, 2]


.. include:: p0047.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 4, 5, 4, 6, 2]

Intersection of 2 lists
=======================

.. include:: p0019.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [3, 4]


.. include:: p0019.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [3, 4]


.. include:: p0019.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [3, 4]

Intersection of n lists
=======================

.. include:: p0037.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [3]


.. include:: p0037.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [3]

Iterate over every other element of a list
==========================================

.. include:: p0017.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    1
    3
    5

Iterate over index/value pairs of a list
========================================

.. include:: p0015.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    0: 1
    1: 2
    2: 7
    3: 13221
    4: 4

Iterate over the elements of a list
===================================

.. include:: p0018.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    1
    2
    3
    4

Largest element from a list of numbers
======================================

.. include:: p0010.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    13221

Last n elements of a list
=========================

n = 2


.. include:: p0023.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [5, 6]

Length of a list
================

.. include:: p0008.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    4

Merge 2 lists
=============

.. include:: p0044.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 5, 6]


.. include:: p0044.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3]


.. include:: p0044.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [4, 5, 6]


.. include:: p0044.py
    :code: python
    :start-after: # -(3)
    :end-before: # -(/3)

::

    [1, 2, 3, 4, 5, 6]


.. include:: p0044.py
    :code: python
    :start-after: # -(4)
    :end-before: # -(/4)

::

    [4, 5, 6]

Permutations of list elements
=============================

.. include:: p0083.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [('a', 'b', 'c'),
     ('a', 'c', 'b'),
     ('b', 'a', 'c'),
     ('b', 'c', 'a'),
     ('c', 'a', 'b'),
     ('c', 'b', 'a')]


.. include:: p0083.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


.. include:: p0083.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

Prepend an element to a list
============================

.. include:: p0045.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4]


.. include:: p0045.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 4]


.. include:: p0045.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [2, 3, 4]

Reverse the order of a list
===========================

.. include:: p0009.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [4, 3, 2, 1]


.. include:: p0009.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [4, 3, 2, 1]


.. include:: p0009.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4]

Smallest element from a list of numbers
=======================================

.. include:: p0011.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    1

Symmetric difference of 2 lists
===============================

.. include:: p0041.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 5, 6]


.. include:: p0041.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 5, 6]


.. include:: p0041.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 5, 6]

Symmetric difference of n lists
===============================

.. include:: p0042.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [2, 6, 7, 8]


.. include:: p0042.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [2, 6, 7, 8]

Union of 2 lists
================

.. include:: p0020.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 5, 6]


.. include:: p0020.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 4, 5, 6]


.. include:: p0020.py
    :code: python
    :start-after: # -(2)
    :end-before: # -(/2)

::

    [1, 2, 3, 4, 5, 6]

Union of n lists
================

.. include:: p0038.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 5, 6, 7, 8]


.. include:: p0038.py
    :code: python
    :start-after: # -(1)
    :end-before: # -(/1)

::

    [1, 2, 3, 4, 5, 6, 7, 8]

Zero-pad a list from the left
=============================

.. include:: p0027.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [0, 0, 0, 0, 0, 0, 1, 2, 3, 4]

Zero-pad a list from the right
==============================

.. include:: p0028.py
    :code: python
    :start-after: # -(0)
    :end-before: # -(/0)

::

    [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]


.. footer:: Copyright 2014 `Matthias Eisen </>`__
