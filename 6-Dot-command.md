# The dot command

```vim
.     Repeat the last command
```

## How to use it

```javascript
let i = 0;
let j = 0;
let k = 0;
```

If we want to change all of the `let` declarations with `const`
we can use the dot command to repeat the last command.

- Search for `let` with `/let/`
- Change the text with `cwconst<esc>`
- Navigate to the next instance with `n`
- Repeat the command with `.`

## Multi line repeat

```javascript
let one = "1";
let two = "2";
let three = "3";
const foo = "bar';
let four = "4";
let five = "5";
let six = "6";
let seven = "7";
let eight = "8";
let nine = "9";
```

Your goal is to delete all lines except the `"foo"` line. First, delete the first
three lines with `d2j`, then to the line below the "foo" line. On the next line,
use the dot command twice. The full command is `d2jj..`
