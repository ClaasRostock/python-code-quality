from .somewhere_deep_in_an_external_package import Line, Plot


def draw_plot(plot: Plot) -> None:
    plot.draw()
    return


def get_first_line_from_plot(plot: Plot) -> Line:
    first_line: Line = plot.L[0]  # pyright: ignore[reportUnknownMemberType]
    return first_line
