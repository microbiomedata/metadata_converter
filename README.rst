metadata_converter
==================

This repo contains code and target outputs for a metadata converter with a
focus on environmental sample metadata.

Source schemas/templates/variable lists are in a variety of different formats.
We choose the biolinkml schema language as our base representation (see below).
We convert all source schemas to biolinkml. From here we convert to other representations
such as json-schema.

Currently the sources we have include:

 * neon
     * `code <src/metadata_converter/neon.py>`__
     * `schema products <target/neon/>`__
     * `docs <docs/neon/>`__
 * kbase
     * `code <src/metadata_converter/kbase.py>`__
     * `schema products <target/kbase/>`__
     * `docs <docs/kbase/>`__
 * mixs
     * INCOMPLETE
     * code is currently external
     * `schema products <target/mixs/>`__
     * `docs <docs/mixs/>`__


Mappings
========

See `mappings folder <mappings/>` __

Building Targets
================

Help:

.. code-block:: sh

    make test
    make all

Mappings
========

TODO

