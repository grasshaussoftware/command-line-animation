from itertools import cycle
from time import sleep


def sleep_with_spinner(seconds: float = 400.0, message: str = "Sleeping"):
    """
    Show a nice spinner animation while sleeping for a given number of seconds.
    Much cleaner and reusable than the original snippet.
    """
    print(f'{message} ', end='', flush=True)

    # Standard spinner frames (cycles forever)
    spinner = cycle(r'-\|/')

    # Calculate exact number of animation frames needed
    frames_needed = int(seconds / 0.2)

    for _ in range(frames_needed):
        # Overwrite the previous spinner character in place
        print('\b', next(spinner), sep='', end='', flush=True)
        sleep(0.2)

    # Erase the spinner character and move to the next line
    print('\b ', flush=True)
