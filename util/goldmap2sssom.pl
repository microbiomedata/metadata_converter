#!/usr/bin/perl -w

use strict;

print "#license: \"https://creativecommons.org/publicdomain/zero/1.0/\"\n";
print "#mapping_date: \"2020-06-36\"\n";
print "#mapping_provider: https://microbiomedata.org/\n";
print "#creator_label:\n";
print "#  - Jagadish Sundaramurthi\n";
print "#  - Bill Duncan\n";
print "#curie_map:\n";
print "#  gold.vocab: \"https://microbiomedata/schema/ddl/\"\n";
print "#  mixs: \"https://microbiomedata/schema/mixs#\"\n";
print "#  skos: \"http://www.w3.org/2004/02/skos/core#\"\n";
my @cols = qw(
    subject_id
    subject_label   
    predicate_id    
    object_id       
    object_label
    match_type
    subject_source
    object_source
    confidence
    comment
    );

print join("\t", @cols). "\n";
# e.g. ../nmdc-metadata//metadata-translation/src/data/GOLD-to-mixs-map.tsv
while(<>) {
    chomp;
    s@[\r\n]+$@@g;
    next if m@^database@;
    my ($db, $tbl, $field, $x) = split(/\t/);
    if ($db ne 'gold') {
        die $_;
    }
    my @vals = ("gold.vocab:$field",
                $field,
                "skos:exactMatch",
                "mixs:$x",
                $x,
                "SSSOMC:HumanCurated",
                "gold.vocab",
                "mixs",
                "1.0",
                "."
        );
    
    print join("\t", @vals). "\n";                
}
