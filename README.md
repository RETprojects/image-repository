# Winter 2022 Shopify Developer Intern Challenge Question

## TagSearch CLI

This is a commandline interface for keeping track of image tags in a folder.
It is a Bash script CLI implementing a Python backend.

## Installation

Install by cloning this repository and using the install target from the makefile.

```{bash}
git clone https://github.com/RETprojects/image-repository.git
make install
```

### Usage

### Loading a folder

Folders can be loaded with the `add` subcommand.

`./TagSearch add <folder_path>`

### Tagging an Image

Images can be tagged with the `tag` subcommand. 

`./TagSearch tag <image_name> <tag>`

### Searching for an Image

Searching images is done with the `search` subcommand.
There are two options: `-f` (search by filename) and `-t` (search by tag).

`./TagSearch search [-t|-f] <query>`
