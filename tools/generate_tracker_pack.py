"""Generates the Universal Tracker map pack (tracker/ folder, issue #55).

Run from an Archipelago source checkout root with this world present as
worlds/mario_kart_double_dash (needs Pillow). Regenerate whenever locations
are added or renamed.
"""
import json, os, sys, types
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.getcwd())
# Fake the worlds package so importing our world doesn't trigger the
# AutoWorld loader (which imports every world and can prompt for packages).
worlds_pkg = types.ModuleType("worlds")
worlds_pkg.__path__ = [os.path.join(os.getcwd(), "worlds")]
sys.modules["worlds"] = worlds_pkg
from worlds.mario_kart_double_dash import game_data, locations

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tracker")

CELL_W, CELL_H = 310, 150
MARGIN = 16
COLS = 4
COURSE_ROWS = 4
DOT_SIZE = 20

BG = (24, 26, 33)
CELL_BG = (41, 44, 57)
CELL_BG_CUP = (52, 44, 41)
BORDER = (90, 95, 115)
TEXT = (235, 235, 235)
LABEL = (150, 155, 175)

def cell_pos(col, row):
    x = MARGIN + col * (CELL_W + MARGIN)
    y = MARGIN + row * (CELL_H + MARGIN)
    return x, y

def main():
    try:
        font_big = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 22)
        font_small = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 15)
    except OSError:
        font_big = font_small = ImageFont.load_default()

    width = MARGIN + COLS * (CELL_W + MARGIN)
    # 4 course rows + 2 cup/misc rows
    rows = COURSE_ROWS + 2
    height = MARGIN + rows * (CELL_H + MARGIN)
    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    # Collect locations by category.
    course_locs = {c.name: {"Race": [], "Boxes": [], "TT": [], "Routes": []}
                   for c in game_data.RACE_COURSES}
    cup_locs = {cup: [] for cup in game_data.CUPS}
    misc_locs = []

    for id, data in enumerate(locations.data_table):
        if id == 0:
            continue
        course = next((c for c in game_data.RACE_COURSES if c.name in data.tags), None)
        cup = next((c for c in game_data.CUPS if c in data.tags or data.region == c), None)
        if course is not None:
            if locations.TAG_ITEM_BOX in data.tags:
                course_locs[course.name]["Boxes"].append(data.name)
            elif locations.TAG_TT in data.tags:
                course_locs[course.name]["TT"].append(data.name)
            elif locations.TAG_SHORTCUT in data.tags:
                course_locs[course.name]["Routes"].append(data.name)
            else:
                course_locs[course.name]["Race"].append(data.name)
        elif cup is not None:
            cup_locs[cup].append(data.name)
        else:
            misc_locs.append(data.name)

    pop_locations = []

    def draw_cell(x, y, title, bg):
        draw.rounded_rectangle([x, y, x + CELL_W, y + CELL_H], radius=10, fill=bg, outline=BORDER, width=2)
        draw.text((x + 12, y + 8), title, fill=TEXT, font=font_big)

    def add_dots(x, y, name, groups):
        """groups: list of (label, [location names]). Returns poptracker children."""
        children = []
        used = [g for g in groups if g[1]]
        n = len(used)
        if n == 0:
            return children
        for i, (label, locs) in enumerate(used):
            dot_x = x + int(CELL_W * (i + 1) / (n + 1))
            dot_y = y + CELL_H - 40
            draw.text((dot_x, dot_y - 18), label, fill=LABEL, font=font_small, anchor="mm")
            children.append({
                "name": label,
                "map_locations": [{"map": "Courses", "x": dot_x, "y": dot_y}],
                "sections": [{"name": loc} for loc in locs],
            })
        return children

    # Course cells.
    for i, course in enumerate(game_data.RACE_COURSES):
        col, row = i % COLS, i // COLS
        x, y = cell_pos(col, row)
        draw_cell(x, y, course.name, CELL_BG)
        groups = [(label, locs) for label, locs in course_locs[course.name].items()]
        children = add_dots(x, y, course.name, groups)
        pop_locations.append({"name": course.name, "children": children})

    # Cup cells (2 rows of 3: 4 normal cups + all cup tour + misc).
    cup_titles = list(game_data.NORMAL_CUPS) + [game_data.CUPS[game_data.CUP_ALL_CUP_TOUR], "Everything Else"]
    for i, title in enumerate(cup_titles):
        col = (i % 3) * 4 // 3  # spread 3 cells over 4 columns: 0, 1, 2 -> wider cells
        # simpler: 3 cells per row, each 4/3 cell wide
        row = COURSE_ROWS + i // 3
        x = MARGIN + (i % 3) * (int(CELL_W * 4 / 3) + MARGIN + 5)
        y = MARGIN + row * (CELL_H + MARGIN)
        w = int(CELL_W * 4 / 3) + 20
        draw.rounded_rectangle([x, y, x + w, y + CELL_H], radius=10, fill=CELL_BG_CUP, outline=BORDER, width=2)
        draw.text((x + 12, y + 8), title, fill=TEXT, font=font_big)
        locs = misc_locs if title == "Everything Else" else cup_locs[title]
        if not locs:
            continue
        dot_x, dot_y = x + w // 2, y + CELL_H - 40
        draw.text((dot_x, dot_y - 18), "Checks", fill=LABEL, font=font_small, anchor="mm")
        pop_locations.append({"name": title, "children": [{
            "name": "Checks",
            "map_locations": [{"map": "Courses", "x": dot_x, "y": dot_y}],
            "sections": [{"name": loc} for loc in locs],
        }]})

    os.makedirs(os.path.join(OUT, "maps"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "locations"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
    img.save(os.path.join(OUT, "images", "courses.png"), optimize=True)
    with open(os.path.join(OUT, "maps", "maps.json"), "w") as f:
        json.dump([{
            "name": "Courses",
            "location_size": DOT_SIZE,
            "location_border_thickness": 2,
            "img": "images/courses.png",
        }], f, indent=2)
    with open(os.path.join(OUT, "locations", "locations.json"), "w") as f:
        json.dump(pop_locations, f, indent=2)
    total = sum(len(ch["sections"]) for loc in pop_locations for ch in loc["children"])
    print(f"tracker pack written: {len(pop_locations)} nodes, {total} sections, image {width}x{height}")

main()
