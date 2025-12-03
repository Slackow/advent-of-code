# Info
This is my repo for 20xx Advent of Code!

I made a `day` bash script that lets me easily run code just by
putting my session token and the current year into a `.env` file

So I can just execute
```
./day 2
```
and it will automatically download the input and run my code in `2025/day2-1.py`

or
```
./day 2 2
# or
PART=2 ./day 2
# or
DAY=2 PART=2 ./day
```
to run part 2 (`2025/day2-2.py`)

text inputs are automatically cached in `.inputs`

Disclaimer: The code quality of my solutions may vary, I generally just
try to solve as quickly as possible so some variables names are
very short and the whole thing is generally uncommented.

I decided to push this on GitHub since I almost removed all my code when trying to move it to another folder by typing `rm` instead of `mv`, thankfully I caught it. :)

# Setup

- Clone the repo (`git clone https://github.com/Slackow/advent-of-code.git`)
- Install [uv](https://docs.astral.sh/uv/#installation)
- Run `cp .env.example .env`
- Fill out `.env` with your values
- Write your own code or use mine in format `"$YEAR/day$DAY-$PART.py"`
- Optionally edit the `.pylintrc` file to disable more or enable some warnings
- Execute the script (`./day $DAY ${PART:-}`)