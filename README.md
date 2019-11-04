# BrachioGraph Utils

This is a random collection of scripts that allow creating nice plots for the amazing [BrachioGraph](https://github.com/evildmp/BrachioGraph) pen plotter.

It allows importing simple SVGs and G-code, minimizing travel distance and previewing the plot.

## Installation

or 

### Usage

```bash
# convert SVG
brachiograph-utils convert svg example.svg out.json

# combine two scripts by piping the stdout to the stdin
brachiograph-utils convert svg example.svg - | brachiograph-utils optimizers order - out.json

# show turtle preview
brachiograph-utils display out.json -s 3 

# every command and category has a help text
brachiograph-utils --help
```

### SVG tips


As the importer is pretty simple, there are some limitations:
- only paths are supported
    - so use Inkscape to convert everything else (e.g. Text, Circles, etc.) to paths
- only straight lines between nodes are allowed (so no Bezier Curves)
    - use `Extensions -> Modify Path -> Flatten Beziers` to make curves cornered
- paths inside of `<defs></defs>` are not ignored
    - if your plot contains squares that are not visible in the SVG, you might have them defined in the `<defs></defs>` section of the SVG. Simply remove them in a text editor if they are not needed.
