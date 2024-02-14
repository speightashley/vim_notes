# Buffers, Windows and Tabs

## Buffers

A buffer is a text file that is currently open. It is held in memory.

We can have multiple buffers open at once.

```bash
> nvim file1.txt file2.txt
```

The above will open two files in two separate buffers.

### Listing Buffers

To list the buffers that are currently open, we can use the `buffers` command:

Within nvim we need to type :buffers to get a list of the buffers.

### Navigating Through Buffers

To navigate through the buffers we can use the `:bnext` and `:bprevious` commands.
To go to a specific buffer, we can use the `:buffer + number` command.

A quicker way is to use the key binding `<leader> b b`

`<CTRL + o>` or `<CTRL + i>` navigates backwards and forwards through buffers to
the previous and next buffer location respectively.

Go to the previous edited buffer with `<CTRL + ^>`

### Closing Buffers

To close a buffer we can use the vim command `:bd` and then tab to the file
name.

Alternative key binding is `<leader> b d`.

#### Bonus: Close All Buffers

To close all buffers we can use the command `:qall`
To save and close all buffers we can use the command `:wqall`

## Windows

A window is what holds a buffer. We see buffers by having them in windows.
Not seeing a buffer in a window doesn't mean the buffer is not open.
To open a new window we can use the `:vnew` command.

We can go to the terminal and then `nvim file.txt`
When inside vim, we can use `:split file2.txt`

This will open a new window with two files in it.

We can also do a `:vsplit file3.txt` to open a new window with three files
in it.

To close a window we can use the key binding `<leader> w d`

To create a new file in a new window, we can use the command `:new file.txt`

## Tabs

A tab is a collection of windows. We can have multiple tabs open at once.

We can open a new tab with the command `:tabnew`

We can close a tab with the command `:tabclose`

To cycle through tabs we can use `gt`

In tabs we can have the same files open but in different "views".

For example, in tab1 we might have a file1.txt and a file2.txt
In tab2 we might have a file3.txt in different splits.

### Useful Tab Commands

```bash
:tabnew file.txt Open file.txt in a new tab
:tabclose Close the current tab
:tabnext Go to next tab
:tabprevious Go to previous tab
:tablast Go to last tab
:tabfirst Go to first tab
```
