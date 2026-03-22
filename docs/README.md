# B3 SOC Brain – Documentation

This folder contains board-ready technical diagrams for the B3 SOC Brain platform.

## Diagrams

| File | Description |
|---|---|
| [`b3_soc_brain_architecture.svg`](b3_soc_brain_architecture.svg) | End-to-end system architecture: ingestion, API, AI, storage, dashboard, and CI/CD layers |
| [`soc_workflow_diagram.svg`](soc_workflow_diagram.svg) | SOC analyst and automation workflow from raw telemetry through containment and review |
| [`autonomous_ai_flowchart.svg`](autonomous_ai_flowchart.svg) | Autonomous AI engine internal pipeline: feature extraction, multi-model inference, rule generation, and adaptive feedback loop |

## How to View

Open any `.svg` file directly in a web browser, or view them rendered automatically on GitHub by clicking each file.

## How to Update

Edit the SVG files directly with any vector graphics editor (Inkscape, Figma, Adobe Illustrator) or update the XML source.
Export a high-resolution PNG if required for presentations:

```bash
inkscape --export-type=png --export-dpi=150 b3_soc_brain_architecture.svg
```
