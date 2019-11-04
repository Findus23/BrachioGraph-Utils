from io import TextIOWrapper

from svgpathtools import Path, svg2paths, Line


def convert(file: TextIOWrapper):
    paths, attributes = svg2paths(file)

    data = []

    path: Path
    for path in paths:
        outline = []
        endpoint = None
        line: Line
        for line in path:
            if not isinstance(line, Line):
                continue
            if line.start != endpoint:
                if outline:
                    data.append(outline)
                outline = [(line.start.real, -line.start.imag)]
            outline.append((line.end.real, -line.end.imag))
            endpoint = line.end
        if outline:
            data.append(outline)

    return data
