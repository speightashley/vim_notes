# Searching Files in Via

## Opening and Editing Files

### Opening Files

`:edit <filename>`

If `<filename>` exists, it will open it. If it doesn't exist, it will create it.

### Searching for files in a project

#### Searching in the same directory

`:edit` accepts wild cards to search.

`:edit *.yml<tab>` will open all files ending in `.yml` in the current directory.

#### Searching in subdirectories

`:edit **/*.yml<tab>` will open all files ending in `.yml` in the current and subdirectories.

#### Searching in file explorer (netrw)

The following will open the file explorer that is built into vim.

`:edit .`

`:edit test/unit/`

### Searching for files with Find

We can find files by using `:find`.
For example:

`:find <filename>`

Autocomplete works with :find as well. Just use the `<tab>` key.

#### PATH and where `find` looks

`:find` used the **path** of the current buffer.

By default, your path will look like `path=.,/usr/include,,`

- `.` means to search in the current directory of the existing file
- `,` means to search in the current directory
- `/usr/include` is the directory for C libraries header files.

##### Changing PATH

`:set path+=django_project/` will add `django_project/` to the path

Now that the path has been updated, when we use `:find` it will search in `django_project/`

### Searching in files with Grep

If we need to look for text within files, we can use `:grep` for external files
or `:vim` which is short for `:vimgrep` for internal files.

We need to use the following commands to see the search:

```bash
:copen        Open the quickfix window
:cclose       Close the quickfix window
:cnext        Go to the next error
:cprevious    Go to the previous error
:colder       Go to the older error list
:cnewer       Go to the newer error list

```

#### Using `:vimgrep` for internal files

`:vimgrep <pattern> <filename>`

We can also use wildcards to search inside of directories.

`:vim /breakfast/ app/controllers/**/*.rb` for example will search for all occurrences
of `breakfast` in all files in subdirectories.

#### Using `:grep` for external files

`:grep -R "lunch" app/controllers/` will search for all occurrences of `lunch`
in all files in `app/controllers/`

## netrw

Netrw is a file explorer built into Vim. We don't need to use it in Nvim because
we use neotree instead.

To use netrw, we can open vim inside a directory with `vim .`

To open netrw inside a directory, we can use `:Vex`

### Other Commands for Netrw

```bash
:Explore     Starts netrw on current file
:Sexplore    No kidding. Starts netrw on split top half of the screen
:Vexplore    Starts netrw on split left half of the screen
```

### Netrw commands

```bash
%  // Create a new file
d  // Create a new directory
R  // Rename a file or directory
D  // Delete a file or directory
```

## LazyVim Finding Files

### Finding by open buffers

`<leader>fb`

### Switch Buffers

`<leader>,`

### Finding by filenames in the current directory or Root Directory

`<leader>ff`
`<leader>fF`

### Find Recent Files

`<leader>fR`

### Finding Config files

`<leader>fc`

### Finding files in root Directory

`<leader><leader>`

### Command History

`<leader>:`

### Find within buffer

`<leader>sb`

### Search Diagnostics

`<leader>sd`

### Search Grep

`<leader>sg`

### Search Help

`<leader>sh`

### Search Keymaps

`<leader>sk`
