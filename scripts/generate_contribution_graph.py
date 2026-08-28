#!/usr/bin/env python3
"""Generate a GitHub activity line graph SVG from the GraphQL API."""

import json
import os
import urllib.request
from html import escape
from pathlib import Path

USERNAME = os.environ.get("PROFILE_USERNAME", "fizzahussain")
TOKEN = os.environ["GITHUB_TOKEN"]
OUTPUT = Path(os.environ.get("GRAPH_OUTPUT", "assets/github-contribution-graph.svg"))

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
            "User-Agent": "github-activity-line-graph",
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
    return [
        day
        for week in user["contributionsCollection"]["contributionCalendar"]["weeks"]
        for day in week["contributionDays"]
    ][-31:]


def render(days):
    width, height = 1100, 330
    left, right, top, bottom = 58, 28, 52, 58
    plot_w = width - left - right
    plot_h = height - top - bottom
    max_count = max((day["contributionCount"] for day in days), default=1)
    y_max = max(5, max_count)

    points = []
    for index, day in enumerate(days):
        x = left + (index / max(1, len(days) - 1)) * plot_w
        y = top + plot_h - (day["contributionCount"] / y_max) * plot_h
        points.append((x, y, day))

    line = " ".join(f"{x:.1f},{y:.1f}" for x, y, _ in points)
    area = f"{left},{top + plot_h} " + line + f" {left + plot_w},{top + plot_h}"

    grid = []
    for step in range(0, 4):
        value = round(y_max * step / 3)
        y = top + plot_h - (value / y_max) * plot_h
        grid.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" stroke="#21262d"/>'
            f'<text x="{left - 12}" y="{y + 4:.1f}" text-anchor="end" class="axis">{value}</text>'
        )

    labels = []
    for index in [0, 7, 14, 21, 30]:
        if index >= len(days):
            continue
        day = days[index]
        x = left + (index / max(1, len(days) - 1)) * plot_w
        label = day["date"][5:]
        labels.append(f'<text x="{x:.1f}" y="{height - 24}" text-anchor="middle" class="axis">{label}</text>')

    circles = []
    for x, y, day in points:
        count = day["contributionCount"]
        title = f'{day["date"]}: {count} contribution' + ("s" if count != 1 else "")
        circles.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#a78bfa">'
            f'<title>{escape(title)}</title></circle>'
        )

    total = sum(day["contributionCount"] for day in days)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(USERNAME)} GitHub activity line graph</title>
<desc id="desc">Daily GitHub contributions over the last 31 days.</desc>
<defs>
  <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.28"/>
    <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.02"/>
  </linearGradient>
</defs>
<style>
  .title {{ font: 700 20px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; fill: #f0f6fc; }}
  .subtitle {{ font: 500 11px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; fill: #8b949e; }}
  .axis {{ font: 500 10px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; fill: #6e7681; }}
</style>
<rect width="100%" height="100%" rx="16" fill="#0d1117"/>
<text x="{left}" y="27" class="title">GitHub Activity</text>
<text x="{left + 176}" y="27" class="subtitle">{total} contributions in the last 31 days</text>
{"".join(grid)}
<polygon points="{area}" fill="url(#area)"/>
<polyline points="{line}" fill="none" stroke="#a78bfa" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
{"".join(circles)}
{"".join(labels)}
</svg>'''


def main():
    days = fetch_days()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render(days), encoding="utf-8")
    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
