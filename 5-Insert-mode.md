# Insert Mode

## Ways to enter insert mode

```vim
i    Insert text before the cursor
I    Insert text before the first non-blank character of the line
a    Append text after the cursor
A    Append text at the end of line
o    Starts a new line below the cursor and insert text
O    Starts a new line above the cursor and insert text
s    Delete the character under the cursor and insert text
S    Delete the current line and insert text, synonym for "cc"
gi   Insert text in same position where the last insert mode was stopped
gI   Insert text at the start of line (column 1)
```

## Repeating in insert mode

If you enter insert mode with the following:

```vim
10i hello <esc>
```

It will say hello ten times.

## Getting text from the clipboard in insert mode

```vim
<C-r>
```

Will enter the registry

We can then select the letter of the registry we want to paste
and the text will appear in the buffer

To put things in the register:

`"ay` + the command to select what you want.

For example:

`"ayiw` will put the word under the cursor in the register a
