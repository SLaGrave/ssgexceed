from src import header, title, characters_intro, players_intro, table_item, calc_scores, image_inline, point_calculation, footer

import argparse
import datetime
import json


NOTE = ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("datafile", type=argparse.FileType("r"))
    args = parser.parse_args()

    data = json.load(args.datafile)
    characters, players = calc_scores(data)

    with open("./index.html", "w") as f:
        # Header
        f.write(header)

        # Title
        f.write(title)
        # f.write(f"<p>{NOTE}</p>")
        f.write(f"<p><b>Last Updated:</b> {datetime.datetime.now().strftime('%m/%d/%Y')}</p>")

        # Characters
        f.write(characters_intro)
        f.write("<table>")
        c = [(k, v) for k,v in characters.items()]
        c.sort(key=lambda a: a[1], reverse=True)
        for pair in c:
            f.write(table_item.format(image_inline.format("characters", pair[0], 50, 50), pair[0], pair[1]))
        f.write("</table>")

        # Players
        f.write(players_intro)
        f.write("<table>")
        p = [(k, v) for k,v in players.items()]
        p.sort(key=lambda a: a[1], reverse=True)
        for pair in p:
            f.write(table_item.format(image_inline.format("players", pair[0], 50, 50), pair[0], pair[1]))
        f.write("</table>")

        # Points
        f.write(point_calculation)

        # Footer
        f.write(footer)
