import json
import random

import click

from .converters import fromgcode, fromsvg
from .display import plot

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    a collection of utilities for creating great BrachioGraph plots
    """
    pass


@cli.group()
def convert():
    """
    import various file formats
    """
    pass


@convert.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def gcode(input, output):
    """
    convert really simple gcode (mostly working on export from Slic3r)
    """
    data = fromgcode.convert(input)
    json.dump(data, output)


@convert.command()
@click.argument('input', type=click.Path())
@click.argument('output', type=click.File('w'))
def svg(input, output):
    """
    convert from paths in SVGs (only supports simple <path> without curves)
    """
    data = fromsvg.convert(input)
    json.dump(data, output)


@cli.group()
def optimizers():
    """
    some scripts that minimize the amount of movement between lines
    """
    pass


@optimizers.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def shuffle(input, output):
    """
    a trivial "optimizer" that shuffles all lines
    """
    data = json.load(input)
    random.shuffle(data)
    json.dump(data, output)


@optimizers.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def order(input, output):
    """
    takes the first line, then searches for the closest end- or startpoint, follows it and continues until all lines are drawn.

    not the shortest route, but very quick and most of the time pretty reasonable
    """
    data = json.load(input)
    from .optimizers.order import optimize as order_optimize
    data = order_optimize(data)
    json.dump(data, output)


@optimizers.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@click.option('-i', "--iterations", type=int, default=500_000)
def randomized_optimizer(input, output, iterations):
    """
    inspired by a traveling saleseman solver this script randomly swaps or reverses lines in the whole drawing
    and always takes the variation with the shortest route

    sometimes able to dramatically reduce travel times, sometimes just stuck on a local minimum

    requires numba as it would take ages to calculate without it
    """
    data = json.load(input)
    from .optimizers.randomized import optimize as randomized_optimize
    data = randomized_optimize(data, iterations)
    json.dump(data, output)


@cli.command()
@click.argument('input', type=click.File('r'))
@click.option('-s', "--scale", type=float, default=1)
@click.option('-x', "--xoffset", type=float, default=0)
@click.option('-y', "--yoffset", type=float, default=0)
def display(input, scale, xoffset, yoffset):
    """
    draws a preview of the plot in a window
    """
    data = json.load(input)
    plot(data, scale, xoffset, yoffset)


if __name__ == '__main__':
    cli()
