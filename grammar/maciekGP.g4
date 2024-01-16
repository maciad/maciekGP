grammar maciekGP;

program : statement+ EOF;

statement : assignment 
          | ifStatement 
          | loopStatement 
          | print
          ;

assignment : variable '=' expression;

ifStatement : 'if' '(' condition ')' blockStatement (else blockStatement)?;

condition : expression comparator expression;

blockStatement : '{' statement* '}';

loopStatement : 'loop' (constant | variable) blockStatement;

print : 'print' '(' expression ')';

expression : constant
           | variable
           | nestedExpression
           | read
           ;

nestedExpression : '(' expression operator expression ')';

read : 'read()';

operator : '*' | '/' | '+' | '-' | '%';
comparator : '==' | '!=' |'<' | '>' | '<=' | '>=';
else : 'else';

constant : INT;
variable : 'x_'INT;

COMMENT : '//' ~[\r\n]* -> skip;
WS : [ \t\r\n]+ -> skip;
INT : [0-9]+;