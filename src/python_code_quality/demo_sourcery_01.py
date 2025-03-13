import dataclasses


@dataclasses.dataclass
class Sample:
    id: str
    value: float


def get_samples() -> list[Sample]:
    # sourcery example: convert for loop into list comprehension
    samples: list[Sample] = _create_samples()
    samples_selected: list[Sample] = []
    for sample in samples:
        if sample.value > 3.0:
            samples_selected.append(sample)
    return samples_selected


def _create_samples() -> list[Sample]:
    samples: list[Sample]
    samples = [
        Sample("first", 1.0),
        Sample("second", 2.0),
        Sample("third", 3.0),
        Sample("fourth", 4.0),
        Sample("fifth", 5.0),
        Sample("sixth", 6.0),
    ]
    return samples
