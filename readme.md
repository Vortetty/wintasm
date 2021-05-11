# WintASM

## Commands

### NOP

A simple no operation

```arm
nop
```

### SET

Set a location in memory

```arm
xor <value 1> <value 2> <output memory location>
```

### XOR

XOR a value with another and store the result

```arm
xor <value 1> <value 2> <output memory location>
```

### JMPIF

Jump if, valid operators are as follows

- Equal to (`==`)
- Not equal to (`!=`)
- Greater than (`>`)
- Less than (`<`)
- Greater than or Equal to (`>=`)
- Less than or Equal to (`<=`)

```arm
jmpif <value 1> <operator> <value 2> <line number to jump to>
```

## Notes for contributors

- Make sure to convert this to a mediawiki format using [pandoc](https://github.com/jgm/pandoc/releases/) by running `pandoc -w mediawiki readme.md -o readme.wiki`
- Update the page on [esolangs.org](https://esolangs.ord)
