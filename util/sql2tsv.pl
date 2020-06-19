#!/usr/bin/perl

my $fn = $ARGV[0];

print "# source: $fn\n";
print "table\tfield\ttype\tdefault\n";

my $table;
while(<>) {
    chomp;
    if (m@create table (\S+)@i) {
        $table = parse_token($1);
    }
    else {
        if ($table) {
            if (m@^\s*\)@) {
                # not guaranteed to work in the general case
                $table = undef;
            }
            else {
                next if m@^\s*$@;
                s@,\s*$@@;
                if (m@^\s*(\S+) (.*)@) {
                    my $field = parse_token($1);
                    my ($type,$default) = parse_type($2);
                    print "$table\t$field\t$type\t$default\n";
                }
            }
        }
    }
}
exit 0;

sub parse_token {
    my ($s) = @_;
    $s =~ s@\"@@g;
    $s =~ s@\'@@g;
    if ($s =~ m@(\S+)\.(\S+)@) {
        # ignore db name
        $s = $2;
    }
    return $s;
}
sub parse_type {
    $_ = shift;
    my $t = 'string';
    $t = 'string' if m@varchar@i;
    $t = 'string' if m@string@i;
    $t = 'integer' if m@integer@i;
    $t = 'time' if m@time@i;
    $t = 'number' if m@number@i;

    my $d = "";
    if (m@default\s+(\S+)@i) {
        $d = parse_token($1);
    }
    return ($t,$d);
}
