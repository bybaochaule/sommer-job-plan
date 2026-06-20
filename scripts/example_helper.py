#!/usr/bin/env python3
"""Deterministischer Helper fuer den Skill sommer-job-plan.

Gibt ein leeres 6-Wochen-Plan-Geruest in Markdown aus. Das Skript macht keine
Netzwerkaufrufe, nutzt keine Geheimnisse und schaetzt oder verspricht keine Einnahmen.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class WeekTemplate:
    week: int
    goal: str
    default_actions: str
    deliverable: str
    metric: str
    quality_gate: str


WEEKS = [
    WeekTemplate(1, "Setup", "1-2 Angebote waehlen; einfachen Proof erstellen; Outreach-Liste bauen", "Angebotsentwurf und Kontaktliste", "Angebote entworfen; Kontakte gelistet", "Angebot hat klaren Scope und keine Garantien"),
    WeekTemplate(2, "Test", "Outreach senden; Feedback erfragen; kleinen Pilot durchfuehren", "Feedback-Notizen und erster Test", "Outreach gesendet; Gespraeche gestartet", "Outreach ist ehrlich und nicht spamartig"),
    WeekTemplate(3, "Liefern", "Erste Arbeit abschliessen; Zeit tracken; Feedback erbitten", "Gelieferter Pilot oder Portfolio-Beispiel", "Lieferobjekte erstellt; Feedback erfasst", "Scope und Qualitaetskriterien erfuellt"),
    WeekTemplate(4, "Verbessern", "Engpaesse pruefen; Angebot schaerfen; wiederverwendbare Templates erstellen", "Aktualisiertes Angebot und Prozess", "Engpass behoben; Template erstellt", "Aenderungen basieren auf Feedback"),
    WeekTemplate(5, "Wiederholen", "Besten Kanal fokussieren; Lieferung wiederholen; Referral-Anfrage testen", "Wiederholbare Wochenroutine", "Follow-ups; wiederholbare Schritte", "Arbeitslast passt zu verfuegbaren Stunden"),
    WeekTemplate(6, "Review", "Portfolio aktualisieren; Lernen zusammenfassen; naechsten Schritt waehlen", "Portfolio-Update und naechste Entscheidung", "Review abgeschlossen", "Erfolgsaussagen nicht uebertrieben"),
]


def markdown_scaffold(title: str) -> str:
    rows = [
        "| Woche | Ziel | Aktionen | Lieferobjekt | Tracker-Metrik | Qualitaets-Gate |",
        "|---|---|---|---|---|---|",
    ]
    for item in WEEKS:
        rows.append(
            f"| {item.week} | {item.goal} | {item.default_actions} | {item.deliverable} | {item.metric} | {item.quality_gate} |"
        )
    return "\n".join([
        f"# {title}",
        "",
        "Nutze dies als Aktivitaetsplan, nicht als Einkommensversprechen.",
        "",
        *rows,
        "",
        "## Woechentliche Review-Fragen",
        "",
        "- Was habe ich getestet?",
        "- Welches Feedback habe ich erfasst?",
        "- Welcher Engpass ist aufgetreten?",
        "- Was aendere ich naechste Woche?",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description="Gibt ein leeres 6-Wochen-Sommerjob-Plan-Geruest aus.")
    parser.add_argument("--title", default="6-Wochen-Sommerjob-Plan-Geruest")
    args = parser.parse_args()
    print(markdown_scaffold(args.title))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
