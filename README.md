# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/irogayoh-png/deadpan-forecasts-cities-that-do-not-exist/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/irogayoh-png/deadpan-forecasts-cities-that-do-not-exist/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

One absurd but believable weather line for an invented city, read like a
straight-faced TV forecast. Entry for the
[make.fun bounty](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c).

## The forecast

> Tonight in Bumbershoot, rain falls only on people who forgot their umbrella, at a steady 2 inches per hour until 9pm.

117 characters, one line. The joke is a single deadpan twist — the rain is
selective — with concrete numbers (2 inches per hour, until 9pm) that make
Bumbershoot feel like a real place on the map.

## How it works

`main.py` writes that one line to `/output/entry.txt` (or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` for a local run). It checks the gate itself
first: exactly one line of 1 to 160 characters, no trailing newline.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/deadpan-test python3 main.py
cat /tmp/deadpan-test/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
