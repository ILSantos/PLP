#!/usr/bin/perl
#hash bang -> que programa vai executar

# Verifica se uma cadeia pertence a linguagem da expressao
# regular
#
# Exemplo de uso
#
#    ./regex.plx 00 "0|(1(0|1)*)"
#    

use strict;

my $cadeia = @ARGV[0];     # o 1o argumento e' a cadeia
my $expressao = $ARGV[1];  # o 2o argumento e' a ER

# O operador =~ verifica se parte da cadeia faz parte da
# linguagem descrita pela expressao regular
#
# Usa-se ^ e $ para obrigar a verificar se a cadeia inteira
# faz parte da linguagem
if ($cadeia =~ /^($expressao)$/) {
	print "'$cadeia' pertence a linguagem\n";
}
else {
	print "'$cadeia' nao pertence a linguagem\n";
}
