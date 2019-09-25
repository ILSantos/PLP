my @lista = (1, 2, 3);
print "@lista\n";

foreach my $it (@lista) {
  # A variável $it é um apelido para cada elemento da lista,
  # portanto o incremento abaixo altera a lista
  $it++;
}

print "@lista \n";
