header = """
<head>
<link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-dark.css" type="text/css">
<link rel="icon" type="image/x-icon" href="./imgs/icons8-punch-16.png">
</head>
"""

title = """
<h1>SSG <img src="./imgs/exceed_logo.webp" alt="Exceed" style="vertical-align:middle;" width="100" height="100"> Rankings</h1>
"""

characters_intro = """
<h3>Character Ranking</h3>
"""

players_intro = """
<h3>Player Ranking</h3>
"""

point_calculation = """
<h3>Point Calculation</h3>
<p>Points are calculated as follows: A single game is worth one point to the winner.
A tournament of <i>n</i> players awards <i>n</i> points to first place, <i>n-1</i> points to second place...
and 1 point to <i>nth</i> place.</p>
"""

table_item = """
<tr>
    <td>{}</td>
    <td><b>{}</b></td>
    <td>{} points</td>
</tr>
"""

image_inline = """
<img src="./imgs/{}/{}.png" style="vertical-align:middle; border-radius: 50%;" width="{}" height="{}">
"""

footer = """
<a href="https://github.com/slagrave"><img src="https://img.shields.io/badge/This_&#128169_by-Sam_LaGrave-purple"></a>
"""