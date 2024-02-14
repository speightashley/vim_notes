# Vim Grammars

## How to learn the language

There is only one grammar rule in vim and that is:

`verb + noun`

### Nouns (Motions)

```bash
h    Left
j    Down
k    Up
l    Right
w    Move forward to the beginning of the next word
}    Jump to the next paragraph
$    Go to the end of the line
```

### Verbs (Operators)

Vim has 16 operators but in reality we only need to use 3 of them.

```bash
y    Yank text (copy)
d    Delete text and save to register
c    Delete text, save to register, and start insert mode
```

With what have learnt above, we can start using them.

## Examples

Let's say that we have the following:

```javascript
const learn = "vim";
```

To yank the text from your current location we can type:

```bash
y$
```

To delete from the current location to the end of the line we can type:

```bash
d$
```

To delete from the current location to the end of the line and start insert
mode we can type:

```bash
c$
```

To yank two chars to the left:

```bash
y2h
```

To delete two chars to the left:

```bash
d2h
```

To delete two words:

```bash
d2w
```

## More Nouns (Text Objects)

There are two object based nouns that we can use in vim.

```vim
i + object    Inner text object
a + object    Outer text object
```

If we have, for example, `(this)` or `[that]` we can use the text object
notation to select the text that we want to yank or delete.

```bash
di(  // Deletes the text inside the parentheses
da(  // Deletes the text and the parentheses
diw  // Deletes the text inside the parentheses if you are hovered over a word
```

### Some examples with HTML

```html
<div>
  <h1>Header1</h1>
  <p>Paragraph1</p>
  <p>Paragraph2</p>
</div>
```

If we have the cursor over `Header1`: We can use `dit` to delete the text
inside the tag.

To deletes the text and the tag we can use `dat`

If we are on the `<div>` tag, we can use `dit` to delete the `h1` and `p`
tags and content

To delete everything, we can use `dat`

To delete `div` we can use `di<`

## Common Text Object Identifiers

```vim
w         A Word
p         A paragraph
s         A sentence
( or )    A pair of ( )
{ or }    A pair of { }
[ or ]    A pair of [ ]
< or >    A pair of < >
t         XML tags
"         A pair of " "
'         A Pair of ' '
`         A pair of ` `
```

More can be found by searching `:h text-objects`
