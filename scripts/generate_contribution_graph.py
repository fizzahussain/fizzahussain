#!/usr/bin/env python3
"""Generate a GitHub contribution calendar SVG from the GraphQL API."""

import json
import os
import urllib.request
from datetime import datetime
from html import escape
from pathlib import Path

USERNAME = os.environ.get("PROFILE_USERNAME", "fizzahussain")
TOKEN = os.environ["GITHUB_TOKEN"]
OUTPUT = Path(os.environ.get("GRAPH_OUTPUT", "assets/github-contribution-graph.svg"))
README = Path("README.md")

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays { date contributionCount }
        }
      }
    }
  }
}
"""


def fetch_days():
    payload = json.dumps({"query": QUERY, "variables": {"login": USERNAME}}).encode()
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "github-contribution-graph",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get("errors"):
        raise RuntimeError(json.dumps(result["errors"], indent=2))
    user = result["data"].get("user")
    if not user:
        raise RuntimeError(f"GitHub user not found: {USERNAME}")
    return [day for week in user["contributionsCollection"]["contributionCalendar"]["weeks"] for day in week["contributionDays"]]


def render(days):
    weeks, current = [], []
    for day in days:
        current.append(day)
        if len(current) == 7:
            weeks.append(current)
            current = []
    if current:
        weeks.append(current)

    cell, gap, left, top = 12, 4, 42, 48
    width = left + len(weeks) * (cell + gap) + 18
    height = 48 + 7 * (cell + gap) + 32
    max_count = max((d["contributionCount"] for d in days), default=1)
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

    rects = []
    for wi, week in enumerate(weeks):
        for di, day in enumerate(week):
            count = day["contributionCount"]
            if count == 0:
                level = 0
            elif max_count <= 1 or count > max_count * 0.75:
                level = 4
            elif count > max_count * 0.5:
                level = 3
            elif count > max_count * 0.25:
                level = 2
            else:
                level = 1
            x = left + wi * (cell + gap)
            y = top + di * (cell + gap)
            title = f'{day["date"]}: {count} contribution' + ("s" if count != 1 else "")
            rects.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{colors[level]}">'
                f'<title>{escape(title)}</title></rect>'
            )

    months, last_month = [], None
    for wi, week in enumerate(weeks):
        month = week[0]["date"][:7]
        if month != last_month:
            label = datetime.strptime(month, "%Y-%m").strftime("%b")
            months.append(f'<text x="{left + wi * (cell + gap)}" y="30" class="month">{label}</text>')
            last_month = month

    weekdays = "".join(
        f'<text x="8" y="{top + (row - 1) * (cell + gap) + 10}" class="weekday">{label}</text>'
        for row, label in ((1, "Mon"), (3, "Wed"), (5, "Fri"))
    )
    legend_x = left + 31
    legend = "".join(
        f'<rect x="{legend_x + i * 16}" y="{height - 19}" width="12" height="12" rx="2" fill="{color}"/>'
        for i, color in enumerate(colors)
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(USERNAME)} GitHub contribution activity</title>
<desc id="desc">Contribution calendar generated from the GitHub GraphQL API.</desc>
<style>.month,.weekday{{font:11px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#8b949e}}.weekday{{font-size:10px}}</style>
<rect width="100%" height="100%" rx="14" fill="#0d1117"/>
{"".join(months)}{weekdays}{"".join(rects)}
<text x="{left}" y="{height - 10}" class="weekday">Less</text>{legend}<text x="{legend_x + 113}" y="{height - 10}" class="weekday">More</text>
</svg>'''


def patch_readme():
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    old_start = "https://github-readme-activity-graph.vercel.app/graph?username=fizzahussain"
    if old_start not in text:
        return
    start = text.index(old_start)
    tag_start = text.rfind("<img", 0, start)
    tag_end = text.find("/>", start)
    if tag_start == -1 or tag_end == -1:
        return
    replacement = '<img src="assets/github-contribution-graph.svg" width="100%" alt="Fizza Hussain GitHub contribution activity graph" />'
    README.write_text(text[:tag_start] + replacement + text[tag_end + 2 :], encoding="utf-8")


def main():
    days = fetch_days()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render(days), encoding="utf-8")
    patch_readme()
    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
