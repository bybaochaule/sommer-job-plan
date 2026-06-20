# Sommer Job Plan

## Überblick

Dieser Skill hilft Agenten, praktische 6-Wochen-Sommerjob-Pläne für Studierende, Freelancer und Side-Hustle-Einsteiger zu erstellen. Er verbindet Skills, Zeitbudget, Ziele und Grenzen zu einem umsetzbaren Kurzzeitplan mit Angebotsideen, Wochenaktionen, Trackern und Qualitätskontroll-Checklisten.

Der Skill macht keine Zusagen über Einnahmen, Nachfrage, Kundengewinnung oder Business-Erfolg.

## Wann verwenden

Nutze diesen Skill für Anfragen wie:

- "Erstelle einen Sommer Job Plan"
- "Ich möchte diesen Sommer Geld verdienen, aber brauche einen Plan"
- "Welche Angebote kann ich mit meinen Skills testen?"
- "Erstelle mir Wochenaktionen, Outreach-Schritte und Tracker"
- "Mach meinen Side-Hustle-Plan realistischer"

## Inhalt

- `SKILL.md`: Agent-Anweisungen, Trigger, Grenzen, Workflow, Ausgabeformat und Sicherheitsregeln.
- `agents/openai.yaml`: Anzeige-Metadaten, implizite Aufruf-Policy und Dateiabhängigkeiten.
- `references/style-guide.md`: Stilregeln, Angebotsmuster, Scoring-Kriterien und Beispielstruktur.
- `assets/tracker-template.csv`: kopierbare Tracker-Spalten für Wochenaktionen, Outreach und Lieferung.
- `assets/quality-checklist-template.md`: wiederverwendbare Qualitätskontroll-Checklisten.
- `scripts/example_helper.py`: deterministischer Helper zum Erzeugen eines leeren 6-Wochen-Plan-Scaffolds.

## Paket-Struktur

```text
sommer-job-plan/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- .gitkeep
|   |-- quality-checklist-template.md
|   `-- tracker-template.csv
|-- references/
|   `-- style-guide.md
`-- scripts/
    `-- example_helper.py
```

## Sicherheitsprinzip

Der Skill darf Ziele und Aktivitäten strukturieren, aber keine Ergebnisse versprechen. Finanzielle Ziele werden als nicht garantierte Zielwerte behandelt. Lokale Regeln, Plattformbedingungen, Arbeitsrecht, Steuern und Lizenzen müssen bei Bedarf aktuell geprüft werden.
