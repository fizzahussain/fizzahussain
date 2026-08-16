#!/usr/bin/env python3
"""Generate a self-updating GitHub profile activity SVG"""

import json
import os
import urllib.request
from datetime import datetime, timezone
from html import escape
from pathlib import Path


USERNAME = os.environ.get("PROFILE_USERNAME", "fizzahussain")
TOKEN = os.environ["GITHUB_TOKEN"]
OUTPUT = Path(os.environ.get("PULSE_OUTPUT", "assets/github-pulse.svg"))

QUERY = """
query($login: String!) {
  user(login: $login) {
    repositories(
      first: 1
      privacy: PUBLIC
      ownerAffiliations: OWNER
    ) {
      totalCount
    }
    contributionsCollection {
      totalCommitContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
      commitContributionsByRepository(maxRepositories: 100) {
        repository {
          name
        }
      }
    }
  }
}
"""


def graphql(query, variables):
    payload = json.dumps({
        "query": query,
        "variables": variables,
    }).encode("utf-8")

    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "github-profile-pulse",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)

    if result.get("errors"):
        raise RuntimeError(json.dumps(result["errors"], indent=2))

    return result["data"]


def sparkline(days, x, y, width, height):
    recent = days[-35:]
    counts = [day["contributionCount"] for day in recent]
    max_count = max(counts) if counts else 1
    max_count = max(max_count, 1)

    gap = 4
    bar_width = (width - gap * (len(recent) - 1)) / max(len(recent), 1)
    bars = []

    for index, count in enumerate(counts):
        bar_height = 3 if count == 0 else max(7, (count / max_count) * height)
        bx = x + index * (bar_width + gap)
        by = y + height - bar_height
        opacity = 0.18 if count == 0 else 0.45 + (count / max_count) * 0.55

        bars.append(
            f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_width:.1f}" '
            f'height="{bar_height:.1f}" rx="2.5" fill="url(#bar)" '
            f'opacity="{opacity:.2f}"/>'
        )

    return "\n".join(bars)


def metric(x, value, label, detail):
    return f"""
    <g transform="translate({x}, 148)">
      <text class="metric" x="0" y="0" text-anchor="middle">{escape(str(value))}</text>
      <text class="label" x="0" y="29" text-anchor="middle">{escape(label)}</text>
      <text class="detail" x="0" y="50" text-anchor="middle">{escape(detail)}</text>
    </g>
    """


def main():
    data = graphql(QUERY, {"login": USERNAME})["user"]
    if not data:
        raise RuntimeError(f"GitHub user not found: {USERNAME}")

    contributions = data["contributionsCollection"]
    calendar = contributions["contributionCalendar"]

    public_repos = data["repositories"]["totalCount"]
    total_contributions = calendar["totalContributions"]
    commit_contributions = contributions["totalCommitContributions"]
    active_repos = len(contributions["commitContributionsByRepository"])

    days = [
        day
        for week in calendar["weeks"]
        for day in week["contributionDays"]
    ]

    last_30 = sum(day["contributionCount"] for day in days[-30:])
    updated = datetime.now(timezone.utc).strftime("%d %b %Y · %H:%M UTC")

    svg = f"""<svg
      xmlns="http://www.w3.org/2000/svg"
      width="1100"
      height="410"
      viewBox="0 0 1100 410"
      role="img"
      aria-labelledby="title desc"
    >
      <title id="title">Fizza Hussain GitHub Pulse</title>
      <desc id="desc">
        Automatically generated public GitHub activity statistics for {escape(USERNAME)}
      </desc>

      <defs>
        <linearGradient id="frame" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#7c3aed"/>
          <stop offset="50%" stop-color="#2563eb"/>
          <stop offset="100%" stop-color="#0f766e"/>
        </linearGradient>

        <linearGradient id="bar" x1="0" y1="1" x2="0" y2="0">
          <stop offset="0%" stop-color="#2563eb"/>
          <stop offset="55%" stop-color="#8b5cf6"/>
          <stop offset="100%" stop-color="#5eead4"/>
        </linearGradient>

        <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
          <feGaussianBlur stdDeviation="8" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>

        <style>
          .title {{
            font: 700 27px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            fill: #f8fafc;
          }}
          .subtitle {{
            font: 500 13px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            fill: #94a3b8;
          }}
          .metric {{
            font: 800 36px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            fill: #f8fafc;
          }}
          .label {{
            font: 700 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            fill: #c4b5fd;
            letter-spacing: .4px;
          }}
          .detail {{
            font: 500 10px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            fill: #64748b;
          }}
          .small {{
            font: 600 11px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            fill: #94a3b8;
          }}
          .updated {{
            font: 500 10px ui-monospace, SFMono-Regular, Menlo, monospace;
            fill: #64748b;
          }}
        </style>
      </defs>

      <rect width="1100" height="410" rx="26" fill="#0d1117"/>
      <rect
        x="1"
        y="1"
        width="1098"
        height="408"
        rx="25"
        fill="none"
        stroke="url(#frame)"
        stroke-width="2"
        opacity=".75"
      />

      <circle cx="70" cy="62" r="13" fill="#8b5cf6" opacity=".18" filter="url(#glow)"/>
      <circle cx="70" cy="62" r="6" fill="#a78bfa"/>

      <text class="title" x="98" y="58">GITHUB PULSE</text>
      <text class="subtitle" x="98" y="80">
        Public engineering activity · automatically regenerated
      </text>

      <line x1="55" y1="105" x2="1045" y2="105" stroke="#1f2937"/>

      {metric(160, public_repos, "PUBLIC REPOSITORIES", "owned repositories")}
      {metric(420, total_contributions, "CONTRIBUTIONS", "current GitHub year window")}
      {metric(680, commit_contributions, "COMMIT CONTRIBUTIONS", "current GitHub year window")}
      {metric(940, active_repos, "ACTIVE REPOSITORIES", "with commit contributions")}

      <line x1="55" y1="222" x2="1045" y2="222" stroke="#1f2937"/>

      <text class="small" x="62" y="255">LAST 35 DAYS</text>
      <text class="small" x="1038" y="255" text-anchor="end">{last_30} contributions in the last 30 days</text>

      {sparkline(days, 62, 273, 976, 78)}

      <text class="updated" x="62" y="384">
        Source: GitHub GraphQL API · public activity
      </text>
      <text class="updated" x="1038" y="384" text-anchor="end">
        Updated {escape(updated)}
      </text>
    </svg>
    """

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(
        f"Generated {OUTPUT}: "
        f"{public_repos} repos, "
        f"{total_contributions} contributions, "
        f"{commit_contributions} commit contributions, "
        f"{active_repos} active repos"
    )


if __name__ == "__main__":
    main()
