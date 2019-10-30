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

## C++ Grammar

The C++ Programming Language

statement:

    labeled-statement
    expression-statement
    compound-statement
    selection-statement
    iteration-statement
    jump-statement

labeled-statement:

    identifier : statement
    case constant-expression : statement
    default : statement

expression-statement:

    expression_opt ;

compound-statement:

    { statement-seq_opt }

statement-seq:

    statement
    statement-seq statement

selection-statement:

    if (  condition  ) statement
    if (  condition  ) statement else statement
    switch (  condition  ) statement

condition:

    expression
    type-specifier-seq declarator = assignment-expression

iteration-statement:

    while ( condition ) statement
    do statement while (  expression  ) ;
    for (  for-init-statement condition_opt ; expression_opt  ) statement

for-init-statement:

    expression-statement
    simple-declaration

jump-statement:

    break ;
    continue ; 
    return expression_opt ; 
    goto identifier ;

## Grammar summary

 C++ Internacional Standard

### Keywords

typedef-name:

    identifier

namespace-name:

    identifier
    namespace-alias

namespace-alias:

    identifier

class-name:

    identifier
    simple-template-id

enum-name:

    identifier

template-name:

    identifier

### Lexical conventions

hex-quad:

    hexadecimal-digit hexadecimal-digit hexadecimal-digit hexadecimal-digit 

universal-character-name:

    \u hex-quad
    \U hex-quad hex0quad

preprocessing-token:

    header-name
    identifier
    pp-number
    character-literal
    user-defined-character-literal
    string-literal
    user-defined-string-literal
    preprocessing-op-or-punc
    each non-white-space character that cannot be one of the above

token:

    identifier
    keyword
    literal
    operator
    punctuator

header-name:

    <  h-char-sequence  >
    " q-char-sequence "

h-char-sequence:

    h-char
    h-char-sequence h-char

h-char:

    any member of the source character set except new-line and > 

q-char-sequence:

    q-char
    q-char-sequence q-char

q-char:

    any member of the source character set except new-line and "

pp-number:

    digit
    . digit 
    pp-number digit
    pp-number identifier-nondigit
    pp-number ' digit 
    pp-number ' nondigit 
    pp-number e sign
    pp-number E sign
    pp-number p sign
    pp-number P sign
    pp-number .

identifier:

    identifier-nondigit
    identifier identifier-nondigit
    identifier digit

identifier-nondigit:

    nondigit
    universal-character-name

nondigit: one of

    a b c d e f g h i j k l m n o p q r s t u v w x y z
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _

digit: one of

    0 1 2 3 4 5 6 7 8 9 

preprocessing-op-or-punc: one of

    {    }      [         ]      #     ##     (    )  
    <:   :>     <%       %>     %:    %:%:     ;     :     ...
    new delete  ?        ::     .     .*      
    +    -      *        /      %     ^       &     |       ~
    !    =      <        >      +=    -=      *=    /=      %=
    ^=   &=     |=      <<      >>    >>=     <<=   ==      !=
    <=   >=     &&      ||      ++     --      ,     ->*      ->
    and and_eq  bitand  bitor   compl  not    not_eq
    or  or_eq   xor     xor_eq

literal:

    integer-literal
    character-literal
    floating-literal
    string-literal
    boolean-literal
    pointer-literal
    user-defined-literal

integer-literal:

    binary-literal integer-suffix_opt
    octal-literal  integer-suffix_opt
    decimal-literal integer-suffix_opt
    hexadecimal-literal integer-suffix_opt

binary-literal:

    0b binary-digit
    0B binary-digit
    binary-literal ' opt binary-digit

octal-literal:

    0
    octal-literal ' opt octal-digit

decimal-literal:

    nonzero-digit
    decimal-literal ' opt digit

hexadecimal-literal:

    hexadecimal-prefix hexadecimal-digit-sequence

binary-digit:

    0
    1

octal-digit: one of

    0 1 2 3 4 5 6 7

nonzero-digit: one of

    1 2 3 4 5 6 7 8 9

hexadecimal-prefix: one of

    0x 0X

hexadecimal-digit-sequence:

    hexadecimal-digit
    hexadecimal-digit-sequence ' opt hexadecimal-digit

hexadecimal-digit: one of

    0 1 2 3 4 5 6 7 8 9
    a b c d e f
    A B C D E F 

integer-suffix:

    unsigned-suffix long-suffix_opt
    unsigned-suffix long-long-suffix_opt
    long-suffix unsigned-suffix_opt
    long-long-suffix unsigned-suffix_opt

unsigned-suffix: one of

    u U

long-suffix: one of

    l L

long-long-suffix: one of

    ll LL

character-literal:

    encoding-prefix_opt ' c-char-sequence '

encoding-prefix: one of

    u8 u U L

c-char-sequence:

    c-char
    c-char-sequence c-char

c-char:

    any member of the source character set except
        the single-quote ', backslash \, or new-line character
    escape-sequence
    universal-character-name

escape-sequence:

    simple-escape-sequence
    octal-escape-sequence
    hexadecimal-escape-sequence

simple-escape-sequence: one of

    \' \" \? \\
    \a \b \f \n \r \t \v

octal-escape-sequence:

    \ octal-digit
    \ octal-digit octal-digit
    \ octal-digit octal-digit octal-digit

hexadecimal-escape-sequence:

    \x hexadecimal-digit
    hexadecimal-escape-sequence hexadecimal-digit

floating-literal:

    decimal-floating-literal
    hexadecimal-floating-literal

decimal-floating-literal:

    fractional-constant exponent-part_opt floating-suffix_opt
    digit-sequence exponent-part floating-suffix_opt

hexadecimal-floating-literal:

    hexadecimal-prefix hexadecimal-fractional-constant binary-exponent-part floating-suffix_opt
    hexadecimal-prefix hexadecimal-digit-sequence binary-exponent-part floating-suffix_opt

fractional-constant:

    digit-sequence_opt . digit-sequence
    digit-sequence .

hexadecimal-fractional-constant:

    hexadecimal-digit-sequence_opt . hexadecimal-digit-sequence
    hexadecimal-digit-sequence .

exponent-part:

    e sign_opt digit-sequence
    E sign_opt digit-sequence

binary-exponent-part:

    p sign_opt digit-sequence
    P sign_opt digit-sequence

sign: one of

    + -

digit-sequence:

    digit
    digit-sequence ' opt digit

floating-suffix: one of

    f l F L

string-literal:

    encoding-prefix_opt " s-char-sequence_opt " 
    encoding-prefix_opt R raw-string

s-char-sequence:

    s-char
    s-char-sequence s-char

s-char:

    any member of the source character set except
        the double-quote ", backslash \, or new-line character
    escape-sequence
    universal-character-name

raw-string:

    " d-char-sequence_opt ( r-char-sequence_opt ) d-char-sequence_opt " 

r-char-sequence:

    r-char
    r-char-sequence r-char

r-char:

    any member of the source character set, except
        a right parenthesis ) followed by the initial d-char-sequence (which may be empty) followed by a double-quote ".

d-char-sequence:

    d-char
    d-char-sequence d-char

d-char:

    any member of the basic source character set except:
    space, the left parenthesis (, the right parenthesis ), the backslash \, and the control characters representing horizontal tab, vertical tab, form feed, and newline.

boolean-literal:

    false
    true

pointer-literal:

    nullptr

user-defined-literal:

    user-defined-integer-literal
    user-defined-floating-literal
    user-defined-string-literal 
    user-defined-character-literal

user-defined-integer-literal:

    decimal-literal ud-suffix
    octal-literal ud-suffix
    hexadecimal-literal ud-suffix
    binary-literal ud-suffix

user-defined-floating-literal:

    fractional-constant exponent-partopt ud-suffix
    digit-sequence exponent-part ud-suffix
    hexadecimal-prefix hexadecimal-fractional-constant binary-exponent-part ud-suffix
    hexadecimal-prefix hexadecimal-digit-sequence binary-exponent-part ud-suffix

user-defined-string-literal:

    string-literal ud-suffix

user-defined-character-literal:

    character-literal ud-suffix

ud-suffix:

    identifier

### Basic Concepts

translation-unit:

    declaration-seq_opt

### Expressions

primary-expression:

    literal
    this
    (  expression  )
    id-expression
    lambda-expression
    fold-expression

id-expression:

    unqualified-id
    qualified-id

unqualified-id:

    identifier
    operator-function-id
    conversion-function-id
    literal-operator-id
    ~ class-name
    ~ decltype-specifier
    template-id

qualified-id:

    nested-name-specifier template_opt unqualified-id

nested-name-specifier:

    ::
    type-name ::
    namespace-name ::
    decltype-specifier :: 
    nested-name-specifier identifier ::
    nested-name-specifier template_opt simple-template-id ::

lambda-expression:

    lambda-introducer lambda-declarator_opt compound-statement

lambda-introducer:

    [  lambda-capture_opt   ]

lambda-declarator:

    (  parameter-declaration-clause  ) decl-specifier-seq_opt
        noexcept-specifier_opt attribute-specifier-seq_opt trailing-return-type_opt

lambda-capture:

    capture-default
    capture-list
    capture-default , capture-list

capture-default:

    &
    =

capture-list:

    capture ...opt
    capture-list , capture ...opt

capture:

    simple-capture
    init-capture

simple-capture:

    identifier
    & identifier
    this
    * this

init-capture:

    identifier initializer
    & identifier initializer

fold-expression:

    ( cast-expression fold-operator ...  )
    ( ... fold-operator cast-expression  )
    ( cast-expression fold-operator ... fold-operator cast-expression )

fold-operator: one of

    + - * / % ^ & | << >>
    += -= *= /= %= ^= &= |= <<= >>= =
    == != < > <= >= && || , .* ->*

postfix-expression:

    primary-expression
    postfix-expression [ expr-or-braced-init-list ]
    postfix-expression ( expression-listopt )
    simple-type-specifier ( expression-listopt )
    typename-specifier ( expression-listopt )
    simple-type-specifier braced-init-list
    typename-specifier braced-init-list
    postfix-expression . templateopt id-expression
    postfix-expression -> templateopt id-expression
    postfix-expression . pseudo-destructor-name
    postfix-expression -> pseudo-destructor-name
    postfix-expression ++
    postfix-expression --
    dynamic_cast < type-id > ( expression )
    static_cast < type-id > ( expression )
    reinterpret_cast < type-id > ( expression )
    const_cast < type-id > ( expression )
    typeid ( expression )
    typeid ( type-id )