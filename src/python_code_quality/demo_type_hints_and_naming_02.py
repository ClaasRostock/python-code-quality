from .somewhere_deep_in_an_external_package import Line, Plot


def draw(p: Plot) -> None:
    p.draw()
    return


def get_l_from_p(p: Plot) -> Line:
    result: Line = p.L[0]  # pyright: ignore[reportUnknownMemberType]
    return result
