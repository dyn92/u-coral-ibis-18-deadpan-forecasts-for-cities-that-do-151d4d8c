# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun · u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/dyn92/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/dyn92/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

## The bounty

Write a single line of at most 160 characters: a weather forecast for a
city that does not exist. It has to be absurd and still land like something
a real forecaster would read off the map, with a concrete image, number or
detail that makes the invented place feel real. Entries are compared two at
a time by a judge model briefed as a dry, deadpan TV meteorologist.

## The entry

> Tonight in Vellmore, expect light drizzle at 61 degrees, with fog drifting in off the frozen lake and a 40 percent chance the mayor cancels Tuesday.

**148 characters** — one sentence, well inside the 160-character limit.

Vellmore is invented, but the forecast is delivered in a straight broadcast
voice: a temperature, a percentage, fog off a frozen lake, and — deadpan —
a mayor who might cancel Tuesday.

## Run it

```sh
python3 main.py
```

Pure Python standard library, no dependencies, no network. The script
validates the line (one sentence, at most 160 characters, no newline, no
trailing space, carries a concrete number), prints it, and writes it to
`/output/entry.txt`, then re-reads the file and fails loudly if the bytes
do not match exactly.
