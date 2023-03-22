# Brain games
---
### Hexlet tests and linter status:
[![Actions Status](https://github.com/marinavasyukova/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/marinavasyukova/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c4a10d1b77687e60284/maintainability)](https://codeclimate.com/github/marinavasyukova/python-project-49/maintainability)

---

## Description
**Brain games** is a simple brain training Cli-utility, which consists of 5 games:

1. Calculator
2. Guess if number is even
3. Find the greatest common divisor
4. Guess if number is prime
5. Complete progression

Each game asks questions and waits for answer from user. After 3 correct answers game is passed. After first incorrect answer game is over.

It's the first training project on Hexlet 'Python developer' course.

---

## Installation

1. ### Using pip

    ```bash
    python3 -m pip install --user git+https://github.com/marinavasyukova/python-project-49.git
    ```
or

2. ### Download from git repository

    ```bash
    git clone https://github.com/marinavasyukova/python-project-49.git
    make install          # install poetry for dependency management and packaging
    make build            # create package in dist/
    make package-install  # install package
    ```
---

## Usage and demo

1. **Calculator**
    ```
    brain-calc
    ```
    Program shows to the user random mathematical expression and user should calculate and write the result.

    <details>
    <summary>Brain-calc game demonstration</summary>

    [![asciicast](https://asciinema.org/a/SdNAnHAgMrpn9ZLm9GeU8aR3d.svg)](https://asciinema.org/a/SdNAnHAgMrpn9ZLm9GeU8aR3d)

    </details>


2. **Guess if number is even**
    ```
    brain-even
    ```
    Program shows to the user a random number and user should answer 'yes' if the number is even, or 'no' if the number is odd.

    <details>
    <summary>Brain-even game demonstration</summary>
    
    [![asciicast](https://asciinema.org/a/oU96SVjCjfGdo3OSiGhsui2rC.svg)](https://asciinema.org/a/oU96SVjCjfGdo3OSiGhsui2rC)

    </details>

3. **Find the greatest common divisor**
    ```
    brain-gcd
    ```
    Program shows to the user two random numbers and user should calculate and write the greatest common divisor of these numbers.
    <details>
    <summary>Brain-gcd game demonstration</summary>

    [![asciicast](https://asciinema.org/a/cJZGVkI0KgDjvFjfqgTm4a259.svg)](https://asciinema.org/a/cJZGVkI0KgDjvFjfqgTm4a259)

    </details>

4. **Guess if number is prime**
    ```
    brain-prime
    ```
    Program shows to the user a random number and user should answer 'yes' if the number is prime, or 'no' otherwise.
    <details>
    <summary>Brain-prime game demonstration</summary>

    [![asciicast](https://asciinema.org/a/zdIk5MAa7K3mlwE1zmmJCj1mp.svg)](https://asciinema.org/a/zdIk5MAa7K3mlwE1zmmJCj1mp)

    </details>

5. **Complete progression**
    ```
    brain-progression
    ```
    Program shows to the user an arithmetic progression with missing number and user should determine and write this missing number.

    <details>
    <summary>Brain-progression game demonstration</summary>

    [![asciicast](https://asciinema.org/a/UjPyvXYgqG6kP0AoLSW55g9jG.svg)](https://asciinema.org/a/UjPyvXYgqG6kP0AoLSW55g9jG)

    </details>
