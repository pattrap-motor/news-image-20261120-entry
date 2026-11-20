"""Draw 'The World in One Day - 20 November 2026' as a 1024x1024 newspaper
front page with Pillow. All artwork is flat vector-style shapes and all text
is drawn with DejaVu fonts, so the image is crisp at the ~300 px judging
scale and byte-identical on every run. No network, no external assets."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
RED = (176, 30, 36)
TEAL = (15, 94, 110)
NAVY = (22, 50, 79)
GOLD = (217, 164, 65)
GREEN = (30, 125, 70)
SKY = (214, 232, 238)
GREY = (90, 90, 90)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill=INK, leading=None):
    if leading is None:
        leading = fnt.size + 6
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def cyclone(draw, x, y, w, h):
    """Spiral storm over a coastline."""
    draw.rectangle([x, y, x + w, y + h], fill=SKY)
    cx, cy = x + w // 2, y + h // 2 - 10
    # spiral arms: concentric arcs, alternating teal/navy
    for r in range(150, 20, -18):
        col = TEAL if (r // 18) % 2 == 0 else NAVY
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=300,
                 fill=col, width=9)
    draw.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(247, 243, 234),
                 outline=NAVY, width=3)
    # coastline strip at the bottom
    coast = [(x, y + h), (x, y + h - 52), (x + 90, y + h - 70),
             (x + 210, y + h - 46), (x + 330, y + h - 66),
             (x + w, y + h - 40), (x + w, y + h)]
    draw.polygon(coast, fill=(222, 196, 138))
    draw.ellipse([x + w - 118, y + h - 62, x + w - 104, y + h - 48],
                 fill=RED)
    draw.text((x + w - 196, y + h - 36), "GOPALPUR", font=font(SANS_B, 17),
              fill=RED)
    # rain streaks
    for i in range(14):
        rx = x + 18 + i * 32
        ry = y + 14 + (i % 3) * 26
        draw.line([rx, ry, rx - 10, ry + 22], fill=(120, 160, 175), width=3)


def marchers(draw, x, y, w, h):
    """Row of student silhouettes with placards."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 238, 240))
    ground = y + h - 26
    draw.rectangle([x, ground, x + w, y + h], fill=(196, 205, 208))
    xs = [x + 18, x + 62, x + 106, x + 150, x + 194]
    cols = [NAVY, RED, TEAL, (90, 60, 110), GREEN]
    for i, px in enumerate(xs):
        # body
        draw.ellipse([px, y + 52, px + 26, y + 78], fill=cols[i])
        draw.rounded_rectangle([px + 1, y + 80, px + 25, ground],
                               radius=8, fill=cols[i])
        # placards only on the first three marchers, kept inside the art
        if i < 3:
            draw.line([px + 26, y + 40, px + 26, y + 78], fill=INK, width=3)
            draw.rectangle([px + 28, y + 22, px + 76, y + 52],
                           fill=(255, 255, 255), outline=INK, width=2)
    draw.text((x + 48, y + 31), "FUTURE", font=font(SANS_B, 11), fill=INK)
    draw.text((x + 136, y + 31), "STRIKE", font=font(SANS_B, 11), fill=INK)


def chart(draw, x, y, w, h):
    """Rising stock chart."""
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    base = y + h - 34
    pts = [(x + 16, base - 8), (x + 62, base - 26), (x + 108, base - 18),
           (x + 154, base - 52), (x + 200, base - 78), (x + 228, base - 96)]
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=GREEN, width=6)
    draw.polygon([(pts[-1][0] - 2, pts[-1][1] + 14), (pts[-1][0] + 16, pts[-1][1] - 4),
                  (pts[-1][0] - 2, pts[-1][1] - 6)], fill=GREEN)
    draw.line([x + 12, base, x + w - 10, base], fill=GREY, width=2)
    draw.text((x + 16, y + 8), "$97.17  +17%", font=font(SANS_B, 24),
              fill=GREEN)


def cricket(draw, x, y, w, h):
    """Cricket ball and stumps on a green strip."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 238, 220))
    gy = y + h - 30
    draw.rectangle([x, gy, x + w, y + h], fill=(120, 170, 90))
    # stumps
    for sx in (x + 30, x + 44, x + 58):
        draw.rectangle([sx, y + 46, sx + 9, gy], fill=(232, 196, 90),
                       outline=INK, width=1)
    draw.rectangle([x + 30, y + 40, x + 67, y + 47], fill=(232, 196, 90),
                   outline=INK, width=1)
    # ball with seam
    bx, by = x + 165, y + 78
    draw.ellipse([bx - 34, by - 34, bx + 34, by + 34], fill=(178, 34, 34))
    draw.arc([bx - 34, by - 34, bx + 34, by + 34], start=250, end=110,
             fill=(255, 255, 255), width=4)
    draw.text((x + 118, y + 118), "243/5", font=font(SANS_B, 30), fill=INK)


def globe(draw, x, y, w, h):
    """Blue globe with balloons for World Children's Day."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 236, 247))
    cx, cy, r = x + 78, y + 82, 58
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(64, 130, 200))
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=(255, 255, 255),
                 width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=3)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], start=0, end=180,
             fill=(255, 255, 255), width=3)
    for bx, by, col in ((x + 185, y + 30, RED), (x + 215, y + 62, GOLD),
                        (x + 170, y + 78, GREEN)):
        draw.ellipse([bx - 13, by - 16, bx + 13, by + 16], fill=col)
        draw.polygon([(bx - 4, by + 16), (bx + 4, by + 16), (bx, by + 24)],
                     fill=col)
        draw.line([bx, by + 24, bx + 8, by + 52], fill=GREY, width=2)


def panel(draw, x, y, w, h, kicker, headline, sub, art, art_w=240):
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    art(draw, x + 2, y + 2, art_w, h - 4)
    tx = x + art_w + 16
    tw = x + w - 14 - tx
    draw.text((tx, y + 12), kicker, font=font(SANS_B, 15), fill=RED)
    y2 = text_block(draw, tx, y + 36,
                    wrap(draw, headline, font(SANS_B, 25), tw),
                    font(SANS_B, 25), leading=30)
    text_block(draw, tx, y2 + 4,
               wrap(draw, sub, font(SANS, 18), tw), font(SANS, 18), leading=23)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.text((W // 2, 16), "THE WORLD IN ONE DAY", font=font(SERIF_B, 62),
           fill=INK, anchor="ma")
    d.line([24, 96, W - 24, 96], fill=INK, width=3)
    d.text((W // 2, 106), "FRIDAY  ·  20 NOVEMBER 2026", font=font(SANS_B, 26),
           fill=RED, anchor="ma")

    # lead panel: cyclone
    ly, lh = 152, 348
    d.rectangle([24, ly, W - 24, ly + lh], outline=INK, width=2)
    cyclone(d, 26, ly + 2, 470, lh - 4)
    tx = 520
    d.text((tx, ly + 16), "LEAD  ·  BAY OF BENGAL", font=font(SANS_B, 17), fill=RED)
    y = text_block(d, tx, ly + 44,
                   wrap(d, "AKVAN HITS ODISHA", font(SERIF_B, 52), W - 24 - tx),
                   font(SERIF_B, 52), leading=58)
    y = text_block(d, tx, y + 8,
                   wrap(d, "Cyclone makes landfall near Gopalpur at noon — "
                           "105,304 people moved to shelters as winds hit "
                           "100 km/h.", font(SANS, 25), W - 24 - tx),
                   font(SANS, 25), leading=32)
    d.text((tx, ly + lh - 40), "Red alerts in 11 districts.",
           font=font(SANS_B, 20), fill=TEAL)

    # grid 2x2
    gy, gh, gap = 520, 172, 16
    panel(d, 24, gy, 488, gh, "EUROPE", "Students walk out",
          "Walkouts in a dozen countries — Italy on general strike.",
          marchers)
    panel(d, 520, gy, 480, gh, "NEW YORK", "Record IPO closes today",
          "ANT ended its debut +17% at $97.17; the $81bn offering "
          "closes.", chart)
    panel(d, 24, gy + gh + gap, 488, gh, "WELLINGTON", "Day 2 in Wellington",
          "New Zealand resume at 243/5; Nicholls unbeaten on 113.",
          cricket)
    panel(d, 520, gy + gh + gap, 480, gh, "EVERYWHERE", "World Children's Day",
          "The UN marks 20 November for children everywhere.", globe)

    # ticker (auto-fit so the line never clips at the edges)
    ty = 900
    d.rectangle([24, ty, W - 24, ty + 44], fill=INK)
    ticker = ("ALSO TODAY  ·  World Children's Day  ·  India v New "
              "Zealand, Day 2  ·  Anthropic's $81bn IPO closes")
    tsize = 19
    while d.textlength(ticker, font=font(SANS_B, tsize)) > W - 72 and tsize > 10:
        tsize -= 1
    d.text((W // 2, ty + (44 - tsize) // 2 - 2), ticker,
           font=font(SANS_B, tsize), fill=(247, 243, 234), anchor="ma")

    # footer
    d.text((W // 2, 958), "Sources: India Meteorological Department  ·  "
           "Nasdaq  ·  ZeroFox  ·  Reuters — All events of Friday 20 November 2026",
           font=font(SANS, 16), fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
