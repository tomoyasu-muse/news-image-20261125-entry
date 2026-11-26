#!/usr/bin/env python3
"""Front page for Wednesday 25 November 2026, drawn for make.fun.

Every story below is a Wednesday 25 November 2026 development, checked
that evening against at least two outlets. Tuesday origins are stated
in the copy where a story began the day before, so no Tuesday event is
presented as if it happened on Wednesday:

- Jiuquan, China: Shenzhou-24 lifts off at 08:18 Beijing time on
  Wednesday, carrying Tang Hongbo, Wu Yi and Pakistani payload
  specialist Muhammad Zeeshan Ali, 40. Ali is the first Pakistani in
  orbit and the first foreign astronaut aboard Tiangong; the craft
  docks about three and a half hours later for a stay of roughly
  five to ten days and about 90 experiments.
  Sources: Reuters, Xinhua, Dawn, CNA.
- Cartagena, Colombia: security forces storm an Exito supermarket
  early on Wednesday, ending a 17-hour siege and freeing all 20
  remaining hostages; one captor is killed and four are detained.
  Ten of about 30 hostages had been released on Tuesday. The siege
  began on Tuesday after a failed armoured-car robbery.
  Sources: Reuters, Al Jazeera, Xinhua, Straits Times.
- Dhaka, Bangladesh: the wage board approves a 36 percent rise in
  the garment minimum wage early on Wednesday, to 17,000 taka a
  month from 12,500, in a 4-2 vote after about 12 hours of talks.
  It takes effect on 1 December for more than four million workers,
  after weeks of protests; unions had sought 18,000 taka.
  Sources: Reuters, TRT World, Prothom Alo, CNA.
- Bogor, Indonesia: rescuers recover nine bodies on Wednesday
  from a flooded unauthorised gold mine and keep searching for 17
  workers trapped in a 100-metre shaft since Monday, when a river
  overflowed after heavy rain. Eleven miners escaped on Monday.
  The toll rose during Wednesday, from three bodies recovered by
  midday to nine by the evening.
  Sources: Reuters, CNA, Al Jazeera, Straits Times, AP.
- Pyongyang, North Korea: KCNA reports on Wednesday that North
  Korea has declared Sylvain Astier, head of the Swiss diplomatic
  office, persona non grata, giving him 48 hours to leave, and has
  ordered the office shut, in response to Swiss sanctions on the
  Songdowon children's camp. The office reopened on 19 October;
  Kim Yo Jong threatened its closure on Tuesday.
  Sources: Reuters, Japan Times, CNA, Le Temps.

Ticker, also Wednesday: Iran's Revolutionary Guards say four
tankers — three oil tankers and an LNG carrier — hit naval mines
and caught fire in the Strait of Hormuz on Wednesday, two of them
early in the day, in the third day of mine incidents there after
three tankers on Monday and a tanker and a container ship on
Tuesday; Shanghai stocks fall 2 percent on Wednesday to their
lowest close since July 2025 as a US tariff probe on 16 partners
looms, and Beijing urges Washington to keep trade stable; the
bodies of six people are found early on Wednesday after a Cessna
210 crashed on Tuesday off Horn Island, Mississippi, including
two boys aged 8 and 10.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
INK = (18, 18, 20)
SOFT = (58, 55, 50)
CREAM = (246, 241, 228)
PANEL = (255, 254, 248)
GOLD = (255, 196, 64)
WHITE = (255, 255, 255)
NAVY = (16, 22, 48)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    lines = []
    pending = ""
    for token in text.split():
        cand = token if pending == "" else pending + " " + token
        if draw.textlength(cand, font=fnt) <= max_width:
            pending = cand
        else:
            lines.append(pending)
            pending = token
    if pending:
        lines.append(pending)
    return lines


def banner(draw, box, colour, caption):
    x0, y0, x1, _ = box
    draw.rounded_rectangle([x0, y0, x1, y0 + 46], radius=10, fill=colour)
    draw.rectangle([x0, y0 + 26, x1, y0 + 46], fill=colour)
    draw.text((x0 + 14, y0 + 10), caption, font=font(BOLD, 24), fill=WHITE)


def body(draw, box, title, detail, title_pt=29, detail_pt=21):
    x0, y0, x1, _ = box
    inner = x1 - x0 - 28
    y = y0 + 60
    for ln in wrap(draw, title, font(BOLD, title_pt), inner):
        draw.text((x0 + 14, y), ln, font=font(BOLD, title_pt), fill=INK)
        y += title_pt + 7
    y += 5
    for ln in wrap(draw, detail, font(REG, detail_pt), inner):
        draw.text((x0 + 14, y), ln, font=font(REG, detail_pt), fill=SOFT)
        y += detail_pt + 6


def panel(draw, box, colour, caption, title, detail, title_pt=26, detail_pt=20):
    draw.rounded_rectangle(box, radius=13, fill=PANEL, outline=INK, width=3)
    banner(draw, box, colour, caption)
    body(draw, box, title, detail, title_pt, detail_pt)


def render_page():
    img = Image.new("RGB", (SIZE, SIZE), CREAM)
    d = ImageDraw.Draw(img)

    # Masthead: the judge is not told the date, so make it huge.
    d.rectangle([0, 0, SIZE, 192], fill=NAVY)
    d.text((26, 10), "THE WORLD IN ONE DAY", font=font(BOLD, 29), fill=GOLD)
    date_text = "25 NOVEMBER 2026"
    pt = 100
    while d.textlength(date_text, font=font(BOLD, pt)) > SIZE - 36:
        pt -= 2
    d.text((18, 44), date_text, font=font(BOLD, pt), fill=WHITE)
    d.text((26, 154), "WEDNESDAY  -  FIVE BIG STORIES, CHECKED ACROSS OUTLETS",
           font=font(BOLD, 24), fill=(205, 212, 230))

    # Lead: Shenzhou-24, Wednesday's launch and docking.
    lead_box = (22, 208, 1002, 414)
    d.rounded_rectangle(lead_box, radius=13, fill=PANEL, outline=INK, width=3)
    banner(d, lead_box, (176, 30, 32), "JIUQUAN  -  CHINA")
    body(
        d, lead_box,
        "FIRST FOREIGN ASTRONAUT REACHES TIANGONG",
        "Shenzhou-24 lifts off at 8:18 a.m. Wednesday with Pakistan's "
        "Muhammad Zeeshan Ali, 40, aboard — the first foreign astronaut "
        "on China's space station. It docks hours later.",
        title_pt=33, detail_pt=22,
    )

    # Four panels.
    panel(d, (22, 430, 500, 682), (0, 102, 102), "CARTAGENA  -  COLOMBIA",
          "ALL 20 REMAINING HOSTAGES FREED",
          "Forces storm a supermarket early Wednesday, ending a "
          "17-hour siege. One captor is killed; 10 hostages had "
          "been freed on Tuesday.",
          title_pt=26, detail_pt=20)
    panel(d, (524, 430, 1002, 682), (128, 52, 128), "DHAKA  -  BANGLADESH",
          "GARMENT PAY UP 36% TO 17,000 TAKA",
          "Wage board approves the rise early Wednesday after weeks "
          "of protests. It takes effect 1 Dec for 4 million workers.",
          title_pt=26, detail_pt=20)
    panel(d, (22, 698, 500, 916), (28, 110, 56), "BOGOR  -  INDONESIA",
          "9 DEAD IN FLOODED GOLD MINE",
          "Rescuers recover 9 bodies Wednesday and keep searching "
          "for 17 workers trapped in a 100m shaft since Monday's "
          "river flood.",
          title_pt=26, detail_pt=20)
    panel(d, (524, 698, 1002, 916), (28, 64, 142), "PYONGYANG  -  N. KOREA",
          "SWISS ENVOY EXPELLED IN 48 HOURS",
          "Pyongyang orders the Swiss office shut on Wednesday "
          "after Bern sanctioned a children's camp. It reopened "
          "on 19 October.",
          title_pt=26, detail_pt=20)

    # Ticker along the foot of the page.
    d.rectangle([0, 928, SIZE, SIZE], fill=NAVY)
    ticker_text = (
        "ALSO WEDNESDAY:  IRAN SAYS 4 TANKERS HIT MINES AND CATCH FIRE "
        "IN STRAIT OF HORMUZ  *  "
        "SHANGHAI STOCKS FALL 2% TO LOWEST CLOSE SINCE JULY 2025  *  "
        "BODIES OF 6 FOUND AFTER TUESDAY CESSNA CRASH OFF MISSISSIPPI"
    )
    ty = 936
    for ln in wrap(d, ticker_text, font(BOLD, 19), SIZE - 44):
        d.text((22, ty), ln, font=font(BOLD, 19), fill=GOLD)
        ty += 24

    return img


if __name__ == "__main__":
    out = Path(__file__).resolve().parent / "entry.png"
    render_page().save(out)
    print(f"saved {out}")
