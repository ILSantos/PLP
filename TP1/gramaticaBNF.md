# Gramática da Linguagem C++

Conter _pelo menos_ as partes da gramática que permitem escrever programas contendo:

- uma declaração/definição de função
- tipos de dados inteiros e de ponto flutuante (equivalente a `int` e `double` em C)
- uma chamada de função (sendo possível retornar um valor)
- um comando de seleção (`if`)
- um comando de repetição (`for, while` ou equivalente)
- literais de inteiros e de pontos flutuantes (pelo menos o essencial, sendo opcional incluir sufixos, prefixos e bases)
- variáveis e parâmetros dos tipos elencados
- expressões algébricas contendo pelo menos os operadores aritméticos e sub-expressões com parênteses

Identificar a gramática de expressões e discutir como a linguagem especifica precedência e associatividade de operadores. Se a linguagem é descrita com recursão explícita, então basta incluir a gramática de expressões no relatório. O relatório deve conter a tabela de precedência e associatividade da linguagem. Compare a tabela com a da linguagem de referência. O número de níveis parece adequado? Argumente.

### BNF

    <INICIO> ::= <ATRIBUIÇÃO> | <REPETIÇÃO> | <CONDIÇÃO>

    <ATRIBUIÇÃO> ::= <TIPO> <IDENTIFICADOR> "=" <ARITMÉTICOS> ";" | <TIPO> <IDENTIFICADOR> ";" | <IDENTIFICADOR> "=" <ARITMÉTICOS> ";" | <IDENTIFICADOR> "++" ";" | <IDENTIFICADOR> "--" ";" | <ATRIBUI_FUNÇÃO>
    
    <IDENTIFICADOR> ::= ([a-z, A-Z])* ([0-9_])+
    
    <NUMERO> ::= ([0-9])+
    
    <NUMERO_REAL> ::= ([0-9])+ | ([0-9])* . ([0-9])*

    <TIPO> ::= "int" | "float" | "char" | "void"
    
    <ARITMÉTICOS> ::= <EXPRESSÃO> ("+" | "-" | "/" | "*") <EXPRESSÃO>
    
    <EXPRESSÃO> ::= <NÚMERO_INTEIRO> | <NÚMERO_REAL>
    
    <CONDIÇÃO> ::= "if" "(" <COMPARAÇÃO> ")" "{" <BLOCO> "}"

    <REPETIÇÃO> ::= <PARA>
    
    <PARA> ::= "for" "(" <ATRIBUIÇÃO> ";" <COMPARAÇÃO> ";" 
    
    <ATRIBUIÇÃO> ")" "{" <BLOCO> "}"
    
    <FUNÇÃO> ::= <TIPO> <IDENTIFICADOR> "(" ")" "{" <BLOCO> "}"
    
    <ATRIBUI_FUNÇÃO> ::= <IDENTIFICADOR> ( "<<" | ">>" ) "\"" <IDENTIFICADOR> "\"" ";" 

    <COMPARAÇÃO> ::= <ATRIBUI_COND> ("==" | "!=" | ">" | "<" | ">=" | "<=") <ATRIBUI_COND> | <ATRIBUI_COND> |  <ATRIBUI_COND> ("==" | "!=" | ">" | "<" | ">=" | "<=") <ATRIBUI_COND> (("&&" | "||" ) <ATRIBUI_COND> ("==" | "!=" | ">" | "<" | ">=" | "<=") <ATRIBUI_COND>)+ 

    <ATRIBUI_COND> ::= <IDENTIFICADOR> | <NUMERO> | "true" | "false"  
