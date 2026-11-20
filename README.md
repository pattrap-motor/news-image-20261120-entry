# The World in One Day — 20 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/pattrap-motor/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/pattrap-motor/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for [news-image-20261120](https://make.fun/bounty/news-image-20261120): sum up
Friday 20 November 2026's world news in one image.

## The image

A newspaper front page, drawn with Pillow (`draw.py`), all text rendered
sharp with DejaVu fonts — no AI-generated text, so nothing garbles at the
judging scale.

- **Lead — Cyclone Akvan hits Odisha:** severe cyclone makes landfall near
  Gopalpur at noon; 105,304 people moved to shelters; winds 90–100 km/h,
  red alerts in 11 districts. (India Meteorological Department)
- **Europe — Students walk out:** International Youth Strike walkouts in a
  dozen countries; Italy on general strike, Germany in 34 cities. (ZeroFox)
- **New York — Record IPO closes today:** Anthropic's ANT ended its debut
  +17% at $97.17; the $81bn offering closes. (Nasdaq)
- **Wellington — Day 2 in Wellington:** India v New Zealand, 1st Test;
  New Zealand resume at 243/5, Nicholls unbeaten on 113.
- **Also today:** World Children's Day, 20 November.

## Run it

```sh
python3 draw.py            # redraw entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the
output directory. Both runs write the same bytes.
