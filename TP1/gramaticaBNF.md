# Gramática BNF do C++

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
