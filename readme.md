
https://github.com/Yarden-zamir/homebrew-tap
# Concept 

```
 Usage: wrap [OPTIONS] COMMAND [ARGS]...
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell.           │
│                                                              [default: None]                                       │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it   │
│                                                              or customize the installation.                        │
│                                                              [default: None]                                       │
│ --help                                                       Show this message and exit.                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ gen      The main function of wrap, this will process all files in the input path using the processors in the      │
│          processor path and output the results to the output path                                                  │
│ github   open the wrap Github page                                                                                 │
│ install  Installs a default configuration for wrap using the base processors and some sensible defaults (wrap can  │
│          be used without this) also imports examples :param install_to_shell: the shell to install to              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## Terminology

- inputs
- wraps
- processors

# Installation
```bash
brew install yarden-zamir/tap/wrap
wrap install
```
