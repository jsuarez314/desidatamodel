# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
==================
desidatamodel.stub
==================

Generate data model files from FITS files.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
from .binary_table_format import binary_table_format
from .data_format import data_format
from .extrakey import extrakey
from .file_size import file_size
from .fits_column_format import fits_column_format
from .parse_header import parse_header
from .process_file import process_file
#
# This is a template.
#
rst = """{titlehighlight}
{title}
{titlehighlight}

General Description
===================

Summary
-------

*This section should be filled in with a high-level description of this file.
In general, you should remove or replace the emphasized text (\*this text
is emphasized\*) in this document.*

Naming Convention
-----------------

``{filename}``, where ...
*Give a human readable description of the filename, e.g.
``blat-{{EXPID}}`` where ``{{EXPID}}`` is the 8-digit exposure ID.*

regex: ``{filename}``
*Give a regular expression for this filename.
For example, a six-digit number would correspond to ``[0-9]{{6}}``.*

File Type
---------

{filetype}, {filesize}  *This section gives the type of the file and its approximate size.*

Contents
========

{contents_table}

FITS Header Units
=================

{hdu_sections}

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

"""