# Um programa em Perl que tenta utilizar uma variável que não foi declarada
#
# Sempre utilize o modo "strict" nos seus programas em Perl. Caso esse modo não fosse
# especificado, a variável seria declarada no momento do seu uso

use strict;

$x = "hello";
print "x = <<$x>>\n";
