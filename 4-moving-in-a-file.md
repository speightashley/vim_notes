# Moving in a File

## Char Navigation

```bash
h        move left
j        move down
k        move up
l        move right
```

## Counting Moves

We can use numbers with all of the motion commands.

```bash
5j       move down 5 lines
10k      move up 10 lines

Or

5<up>   move up 5 lines
5<down> move down 5 lines
```

## Word Navigation

We can navigate using word characters.
The following are all word related commands:

```bash
w        move to the start of the next word
W        move to the start of the next word
e        move to the end of the next word
E        move to the end of the next word including punctuation
b        move to the start of the previous word
B        move to the start of the previous word
```

## Line Navigation

We can navigate using line characters.
The following are all line related commands:

```bash
0        move to the start of the line
$        move to the end of the line
^        move to the first non-whitespace character of the line
g_       move to the last non-whitespace character of the line
n|       move to the nth character of the line
```

## Navigate with finding letters

`f<letter>` will move to the first occurrence of the letter
`F<letter>` will move to the last occurrence of the letter
`t<letter>` will move to the next occurrence of the letter
`T<letter>` will move to the previous occurrence of the letter

## Sentence and Paragraph Navigation

`(` will move to the previous sentence
`)` will move to the next sentence

`{` will move to the previous paragraph
`}` will move to the next paragraph

## Navigating parentheses and braces

`%` will move to the matching brace

It works for:

```java
()
{}
[]
```

## Scrolling up and down

`Ctrl-u` will scroll up
`Ctrl-d` will scroll down
`Ctrl-f` will scroll down a screen
`Ctrl-b` will scroll up a screen

## Relative Scrolling

`zt` will scroll up a page
`zb` will scroll down a page
`zz` will scroll to the middle of the screen

## Using Marks

Very Useful! We can set markers in the text and jump to them.

`m<letter>` will set a mark
`'<letter>` will jump to the mark

`:marks` will list all the marks

## Jumps in vim

```plaintext
'       Go to the marked line
`       Go to the marked position
G       Go to the line
/       Search forward
?       Search backward
n       Repeat the last search, same direction
N       Repeat the last search, opposite direction
%       Find match
(       Go to the last sentence
)       Go to the next sentence
{       Go to the last paragraph
}       Go to the next paragraph
L       Go to the the last line of displayed window
M       Go to the middle line of displayed window
H       Go to the top line of displayed window
[[      Go to the previous section
]]      Go to the next section
:s      Substitute
:tag    Jump to tag definition
```
