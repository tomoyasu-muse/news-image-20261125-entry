# 25 November 2026 — The World in One Day

[![make.fun bounty](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/tomoyasu-muse/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/tomoyasu-muse/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125)

A program that writes one image summing up the world news of
**Wednesday 25 November 2026** to `/output/entry.png`, entered in the
[make.fun bounty "Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125).

## What the image shows

A newspaper front page with the date **25 NOVEMBER 2026** in extra
large type and five stories, each a Wednesday 25 November development
cross-checked across several news sources reporting that day:

- Shenzhou-24 lifts off at 8:18 a.m. on Wednesday from Jiuquan,
  carrying Pakistan's Muhammad Zeeshan Ali, 40 — the first Pakistani
  in orbit and the first foreign astronaut aboard China's Tiangong
  space station — and docks hours later
- Security forces storm a supermarket in Cartagena early on Wednesday,
  ending a 17-hour siege and freeing all 20 remaining hostages; one
  captor is killed, after 10 hostages were released on Tuesday
- Bangladesh's wage board approves a 36% rise in the garment minimum
  wage early on Wednesday, to 17,000 taka a month from 12,500, after
  weeks of protests, for more than four million workers
- Rescuers recover nine bodies on Wednesday from a flooded gold mine
  in Bogor, Indonesia, and keep searching for 17 workers trapped in
  a 100-metre shaft since Monday's river flood (the toll rose during
  Wednesday, from three bodies by midday to nine by the evening)
- North Korea expels the head of the Swiss diplomatic office in
  Pyongyang on Wednesday, giving him 48 hours to leave, and orders
  the office shut, after Swiss sanctions on a children's camp

A ticker adds Iran saying four tankers — three oil tankers and an
LNG carrier — hit naval mines and caught fire in the Strait of
Hormuz on Wednesday, Shanghai stocks falling 2% on Wednesday to
their lowest close since July 2025, and the bodies of six people
found early on Wednesday after a Cessna 210 crashed on Tuesday
off Mississippi.

Stories first reported on Tuesday 24 November — the Shanghai party
chief investigation, the Huawei verdict, and Ukraine's 2027 financing
need — were deliberately left out, even though they were widely
reported again on Wednesday.

## How it works

`entry.png` is drawn by `draw_entry.py` (Python + Pillow) before
submission. `main.py` (Python 3.13, standard library only) copies
that finished image to `/output/entry.png`, so two runs in the
offline grading sandbox always write exactly the same bytes.

Run it locally:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
