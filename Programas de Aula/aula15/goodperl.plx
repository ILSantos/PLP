#!/usr/bin/perl

# Um programa em Perl que manipula uma lista

@vetor = (1, 2, 3, 4);
$numel = $#vetor;
print "O vetor contem $numel elementos:\n";
print @vetor;
print "\n";

$primeiro = $vetor[0];
print "O primeiro elemento da lista eh $primeiro\n";

$primeiro = shift @vetor;
print "O primeiro elemento da lista era $primeiro:\n";
print @vetor;
print "\n";
