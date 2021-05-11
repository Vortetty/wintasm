# WintASM

## Basics

- Memory locations are defined with a hex number after `0m`, an example for memory location 255 is `0mff`
- Integers can be defined with the prefix `0b` for binary, `0x` for hex, or none for decimal
- Char strings can be defined with `"` before and after the text
- Values can be memory locations, or ints
- Multiple comment formats are supported, those being as follows:

    ```text
    /*
    i am a comment
    i cover many lines though
    */

    code
    
    // i am a comment

    code
    
    # i am a comment

    code    

    ; i am a comment

    "; i will not be treated as a comment since i'm in a string!"

    ";" i also am not a comment since i start in a string
    ```

    you can see the matches for this example [here](https://pythex.org/?regex=((%3B%7C%5C%23%7C%2F%2F)(%3F%3D(%5B%5E%22%5D*%22%5B%5E%22%5D*%22)*%5B%5E%22%5D*%24).*%7C%2F%5C*(%3F%3D(%5B%5E%22%5D*%22%5B%5E%22%5D*%22)*%5B%5E%22%5D*%24)(.%7C%5Cn)*%3F%5C*%2F(%3F%3D(%5B%5E%22%5D*%22%5B%5E%22%5D*%22)*%5B%5E%22%5D*%24))&test_string=%20%20%20%20%2F*%0A%20%20%20%20i%20am%20a%20comment%0A%20%20%20%20i%20cover%20many%20lines%20though%0A%20%20%20%20*%2F%0A%0A%20%20%20%20code%0A%20%20%20%20%0A%20%20%20%20%2F%2F%20i%20am%20a%20comment%0A%0A%20%20%20%20code%0A%20%20%20%20%0A%20%20%20%20%23%20i%20am%20a%20comment%0A%0A%20%20%20%20code%20%20%20%20%0A%0A%20%20%20%20%3B%20i%20am%20a%20comment%0A%0A%20%20%20%20%22%3B%20i%20will%20not%20be%20treated%20as%20a%20comment%20since%20i%27m%20in%20a%20string!%22%0A%0A%20%20%20%20%22%3B%22%20i%20also%20am%20not%20a%20comment%20since%20i%20start%20in%20a%20string&ignorecase=0&multiline=0&dotall=0&verbose=0)

## Commands

### NOP

A simple no operation

```arm
nop
```

### SET

Set a location in memory

```arm
xor <value 1> <output memory location>
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

## Notes for contributors

- Make sure to convert this to a mediawiki format using [pandoc](https://github.com/jgm/pandoc/releases/) by running `pandoc -w mediawiki readme.md -o readme.wiki`
- Update the page on [esolangs.org](https://esolangs.org/wiki/Main_Page)
