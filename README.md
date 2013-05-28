Brainfuck-Compiler
==================

Brainfuck compiler in python designed for a spoj problem
it doesn't have the input parameter installed ,will soon add it

Brainfuck ---

The brainfuck programming language is an esoteric programming language noted for its extreme minimalism. 
It is a Turing tarpit, designed to challenge and amuse programmers, and was not made to be suitable for practical use.

Commands:::

The eight language commands, each consisting of a single character:
Character   Meaning

greater than		increment the data pointer (to point to the next cell to the right).
less than			decrement the data pointer (to point to the next cell to the left).
plus sign 			increment (increase by one) the byte at the data pointer.
minus sign			decrement (decrease by one) the byte at the data pointer.
Full stop			output the byte at the data pointer.
comma				accept one byte of input, storing its value in the byte at the data pointer.
open bracket		if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump 				it forward to the command after the matching ] command.

close bracket		if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, 			jump it back to the command after the matching [ command.

[ and ] match as parentheses usually do: each [ matches exactly one ] and vice versa, the [ comes first, and there can be no unmatched [ or ] between the two.

Brainfuck programs can be translated into C using the following substitutions, assuming ptr is of type unsigned char* and has been initialized to point to an array of zeroed bytes:
brainfuck command 	C equivalent
(Program Start) 	char array[30000];
char *ptr=array;
  greater than		++ptr;
  less than			--ptr;
  plus sign			++*ptr;
  minus sign		--*ptr;
  Full stop			putchar(*ptr);
  comma				*ptr=getchar();
  open bracket		while (*ptr) {
  close bracket		}

An additional command % is supported by the compiler :
%    To give a comment,every character after this character is treated as a comment in that line.

Hope its helpful..
