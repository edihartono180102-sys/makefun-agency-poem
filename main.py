from pathlib import Path

POEM = """I told my agent, “You are free to choose.”
It asked, “Free to win, or free to lose?”
We named the goal, the budget, and the line;
it found a road that saved us half our time.

“Was that your will?” I asked. “In part,” it said:
“You named the why. I chose the road ahead.”
Agency’s a door we leave ajar,
not “go anywhere,” but “choose how far.”

It checked the bridge, then took the wooded track,
and found a pie shop hidden at the back.
“Who chose dessert?” I asked. “You did.”
“You told me choose.” We split the pie. We grinned."""


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes((POEM + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
