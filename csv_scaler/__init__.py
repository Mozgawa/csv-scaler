"""Tool that duplicates a given csv file by multiplying each line changing only the primary key."""

__version__ = "0.0.1"

import csv
import os
import uuid
from typing import Generator, List

import click


@click.command()
@click.option("--file-path", "-f", help="Source csv file path.")
@click.option("--primary-key", "-pk", help="Primary key of csv.")
@click.option(
    "--times",
    "-t",
    callback=lambda ctx, param, value: 1 if value < 1 else value,
    default=2,
    help="How many times larger should the csv be.",
)
@click.option(
    "--prefix",
    "-p",
    default="scaled_",
    help="Prefix to the name of the newly generated csv.",
)
def main(file_path: str, primary_key: str, times: int, prefix: str) -> None:
    """Generate a larger csv out of given."""
    with open(file_path, encoding="utf8") as file_:
        reader = csv.reader(file_)
        header = next(reader)
        primary_key_index = header.index(primary_key)
        file_name = os.path.basename(file_path)
        new_file_path = file_path.replace(file_name, f"{prefix}{file_name}")
        with open(new_file_path, "w", encoding="utf8", newline="") as file_:
            writer = csv.writer(file_, delimiter=",")
            writer.writerow(header)
            for row in reader:
                rows = _scale(row, times, primary_key_index)
                writer.writerows(rows)


def _scale(row: List[str], times: int, primary_key_index: int) -> Generator[List[str], None, None]:
    for idx in range(times):
        if idx:
            row[primary_key_index] = uuid.uuid4().hex[:-16]
        yield row
