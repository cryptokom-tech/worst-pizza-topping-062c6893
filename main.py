import os

ENTRY = (
    "Try our pizza topped with pocket lint — farm-to-table, "
    "if the farm is your coat pocket and the table is a mistake."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY:
        raise SystemExit("entry must be one line of 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != ENTRY:
            raise SystemExit("entry read-back mismatch")


if __name__ == "__main__":
    main()
