=============================
Contributing to desidatamodel
=============================

Introduction
~~~~~~~~~~~~

This page is about contributing to the
DESI data model documentation; it is not about the data model itself.

Examples and Other Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 1

    examples/index

Directory Tree
~~~~~~~~~~~~~~

Please follow these rules when creating or updating directories within the
data model.

1. All directories must have an index.rst file.
2. The title of every index.rst file contains *only* the name of the directory it is in.
3. Each index.rst contains the following items in its toctree:

   a. Links to index.rst files in any subdirectories.
   b. Links to files in that directory.

4. Every file must have a title.  For example::

    ===================
    fibermap-EXPID.fits
    ===================

Code setup
~~~~~~~~~~

To build the data model locally, you first need to install the following::

    pip install sphinx-toolbox sphinx-rtd-theme

Building the Documents
~~~~~~~~~~~~~~~~~~~~~~

To build the docs::

    sphinx-build -W --keep-going -b html doc doc/_build/html

Then view ``doc/_build/html/index.html`` in a web browser.  If you have
installed the `sphinx-rtd-theme Python package`_, the docs will be formatted
using the ReadTheDocs theme as they will appear at
https://desidatamodel.readthedocs.io

Sphinx will often print warnings and claim that the "build succeeded" when
in fact there were syntax errors that break the output. You must pay attention
to the warnings and fix them!

Also note that Spinx builds documents incrementally.  That is, if you run
:command:`sphinx-build`, change one file, and then run :command`sphinx-build`
again, it will only rebuild the changed file.  Normally this is fine, but
if the change causes the directory tree to change, for example, adding
a file to a table of contents, then the entire document tree should be rebuilt.
This can be done by simply adding the ``-E`` option to :command`sphinx-build`::

    sphinx-build -E -W --keep-going -b html doc doc/_build/html

desidatamodel_ also includes unit tests; you can run these locally before
opening a PR using::

    pytest py/desidatamodel/test

.. _`sphinx-rtd-theme Python package`: https://pypi.org/project/sphinx-rtd-theme/
.. _desidatamodel: https://github.com/desihub/desidatamodel

Units
~~~~~

We encourage the documentation of units as well as types. Although not *every*
FITS file specifies units, we want units to be documented anyway.  FITS
images that have units should have a ``BUNIT`` header keyword.  FITS
table columns that have units should have a ``TUNITxx`` keyword. For the purposes
of documentation though, we want the units to be specified, even if they
don't actually appear in the file being documented.

Units should follow the `FITS Standard`_, in particular following Section 4.3, and Tables 3, 4,
and 5 in that document.

You can test units for validity by using `Astropy Units`_. This package
already supports the FITS Standard. The ``desidatamodel`` package itself
already uses this internally.  In fact, we have added some units that
DESI considers acceptable, even if they do not strictly follow the FITS Standard.

Here are some examples of units that are used in this data model, as well as
a few common gotchas.

===================================== ============== =================================================================
Unit                                  FITS Standard? Comment
===================================== ============== =================================================================
``um``                                Yes            Micrometers, :math:`\mu m`.
``Angstrom``                          Yes            Ångström.
``photon``                            Yes            Number of photons.
``count``                             Yes            Number of counts, usually electrons.
``adu``                               Yes            Closely related to ``counts``.
``deg``                               Yes            Degrees.
``arcsec``                            Yes            Seconds of arc.  Not time!
``mag``                               Yes            Standard astronomical magnitude. *Not* the same as a ``maggie``.
``pc``                                Yes            Parsec.
``Jy``                                Yes            Jansky.
``10**-17 erg/(s cm2 Angstrom)``      Yes            Common unit of spectrophotometric flux.
``10**+34 (s2 cm4 Angstrom2) / erg2`` Yes            Inverse variance of flux.
``A``                                 Yes, but...    ``A`` is the unit for amperes not Ångström.
``maggie``                            No, but OK     Standard prefix is also OK: ``nanomaggie``.
``mgy``                               No, but OK     Abbreviation for ``maggie``.
``electron/Angstrom``                 No, but OK     Used in some calibration files.
``ergs``                              **No**         ``erg``, not ``ergs``.
``sec``                               **No**         ``s`` for seconds, not ``sec``. Even though ``arcsec`` is OK.
===================================== ============== =================================================================

.. _`FITS Standard`: https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf
.. _`Astropy Units`: https://docs.astropy.org/en/stable/units/index.html

Tips and Tests
~~~~~~~~~~~~~~

You can browse some :doc:`examples <examples/index>`.

Cross-Referencing
+++++++++++++++++

To a file
---------

Here is how you make a :doc:`direct link to a file <examples/spPlate>`::

    Here is how you make a :doc:`direct link to a file <examples/spPlate>`

Note that the link must take into account the directory structure.
So for example, if you're in the directory ``DESI_SPECTRO_SIM/PIXPROD/NIGHT``
and want to refer to a file in ``DESI_SPECTRO_DATA/NIGHT``, the link has
to have the form::

    :doc:`link to real data <../../../DESI_SPECTRO_DATA/NIGHT/real_data_file>`

or::

    :doc:`link to real data </DESI_SPECTRO_DATA/NIGHT/real_data_file>`

That is, you can use a relative or absolute path.

Within a file
-------------

You can also cross-reference sections within files, however the notation is
somewhat different. There are two methods.  The first involves creating
an explicit reference point in the target document.  For example, in the
spPlate file we referenced above, we can label HDU5::

    .. _spplate-hdu5-plugmap:

    HDU5
    ----

    EXTNAME = PLUGMAP

Then we use ``:ref:`` to cross-reference that label. Here's a link to that
:ref:`section of the spPlate file <spplate-hdu5-plugmap>`::

    :ref:`section of the spPlate file <spplate-hdu5-plugmap>`

Note however, that this label must be globally unique!

Alternatively, one can use "raw" ReStructuredText constructions. Here's a link
to another `section of the spPlate file`_ we already linked to above::

    link to another `section of the spPlate file`_

    .. _`section of the spPlate file`: examples/spPlate.html#hdu6

.. _`section of the spPlate file`: examples/spPlate.html#hdu6

Note this time that the section name may be upper case (``HDU6``), but the
HTML anchor is lower case ``#hdu6``.

To a HDU
--------

The latter form can be used to create cross references to individual HDUs in
other files.  This would have the (strict!) form::

    HDU5
    ----

    See `HDU1 in some-other-file <../../some-other-file.html#hdu2`_.

In other words, with this notation, the data model for HDU2 in ``some-other-file``
will be used as the data model for HDU5 in the file with the cross-reference.

Environment variables
+++++++++++++++++++++

Here is how to highlight an :envvar:`ENVIRONMENT_VARIABLE`::

    Here is how to highlight an :envvar:`ENVIRONMENT_VARIABLE`

Optional Keywords and Columns
+++++++++++++++++++++++++++++

Sometimes HDU in a file might not have all of the header keywords or a table
might not have all the columns described in the data model.
Sometimes this is expected, and these items should be
marked as optional, so we can focus on *required* items that might be
missing. The optional notation leverages reStructuredText's footnote notation.
Here is an example using table columns::

    Required Data Table Columns
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ========= ======== ===== ===========
    Name      Type     Units Description
    ========= ======== ===== ===========
    target    char[20]
    OPT1 [1]_ int16
    V_mag     float32  mag
    vdisp     float64  km/s
    OPT2 [1]_ float32
    ========= ======== ===== ===========

    .. [1] Optional

Note how ``.. [1] Optional`` is added to the bottom.  This keeps Sphinx from
complaining about undefined footnotes, but also makes it easy for humans to
see what this notation means.  ``.. [1] Optional`` only needs to be added
once per file, not once per table.

Optional HDUs
+++++++++++++

This is a work in progress.

Strings
+++++++

Depending on how data sets are collated, it sometimes happens that sets of
strings may be written out to FITS files with different lengths.

For example, data sets A and B are supposedly identical (same columns,
same types, etc.).  However set A has a string-valued column ``NAME`` that has values
from the set ``{'one', 'two', 'three'}``, while in set B the same column has
values from the set ``{'one', 'two', 'six'}``.  When written out, file A
has the ``NAME`` column represented as ``char[5]`` (``5A`` in FITS notation), while file B
has the same column represented as ``char[3]`` (``3A``).

To account for differences like this, one can use::

    Required Data Table Columns
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ========= ======== ===== ===========
    Name      Type     Units Description
    ========= ======== ===== ===========
    ...
    NAME      char[*]
    ...
    ========= ======== ===== ===========

to represent the fact that the actual length of the string doesn't matter.
