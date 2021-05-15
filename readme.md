# WintASM

## Basics

- Memory locations are defined with a hex number after `0m`, an example for memory location 255 is `0mff`
- Integers can be defined with the prefix `0b` for binary, `0x` for hex, or none for decimal
- Char strings can be defined with `"` before and after the text
- Values can be memory locations or ints
- Line numbering starts on 1
- Memory locations can be any number, big or small
- Multiple comment formats are supported, those being as follows:

    ```text
    /*
    i am a comment
    i cover many lines though
    */
    
    // i am a comment
    
    # i am a comment

    ; i am a comment
    ```

  - Note that block comments cannot begin on the same line as other code

## Hard-Mode Commands (the bare minimum to run any calculation with enough memory for said operation)

### NAND

NAND a value with another and store the result

```arm
nand <value 1> <value 2> <output memory location>
```

### JMPIF

Jump if condition is true

Valid operators are as follows

- Equal to (`==`)
- Not equal to (`!=`)
- Greater than (`>`)
- Less than (`<`)
- Greater than or Equal to (`>=`)
- Less than or Equal to (`<=`)

```arm
jmpif <value 1> <operator> <value 2> <line number to jump to>
```

## Other Commands (includes hard mode commands)

### NOP

A simple no operation

```arm
nop
```

### SET

Set a location in memory

```arm
set <memory location> <value>
```

### XOR

XOR a value with another and store the result

```arm
xor <value 1> <value 2> <output memory location>
```

### AND

AND a value with another and store the result

```arm
and <value 1> <value 2> <output memory location>
```

### NOT

NOT a value with another and store the result

```arm
not <value 1> <value 2> <output memory location>
```

### DISP

Display values or memory locations in terminal

Valid methods are as follows:

- Chr (`0`)
- Dec (`1`)
- Hex (`2`)
- Bin (`3`)

```arm
disp <method> <mem location ...>
```

### LODIR

Load all modules from a directory, it must contain files named like `op_<module name>.py`, each module must contain a function with the same name as the file matching the python type `Callable[[List[int], int, int, str, List[str], Dict[str, Any]], None]`

```arm
lodir <string with directory>
```

## Notes for contributors

- Make sure to convert this to a mediawiki format using [pandoc](https://github.com/jgm/pandoc/releases/) by running `pandoc -w mediawiki readme.md -o readme.wiki`
- Update the page on [esolangs.org](https://esolangs.org/wiki/Main_Page)
