# Integration Guide: Adding the Life Cycle Dashboard to `shannonrankin/ethnobotany`

## What changed from the standalone version

| | Standalone | Integrated |
|---|---|---|
| **Navigation** | Custom fixed sidebar (left) | Removed — Quarto's sidebar handles this |
| **Dropdowns** | Inside that fixed sidebar | Horizontal control bar at top of page |
| **CSS variable names** | `--parchment`, `--bark`, etc. | `--eb-parchment`, `--eb-bark`, etc. (prefixed to avoid cosmo conflicts) |
| **Slideout z-index** | 200 | 1050 (clears Quarto navbar + docked sidebar) |
| **Page layout** | `custom` | `full` (fills content area, suppresses Quarto TOC column) |
| **TOC** | off | overridden off per-page (site default is `toc: true`) |
| **CSS location** | `content/dashboard.css` | `content/dashboard.css` (same — co-located with `.qmd`) |
| **FileAttachment path** | `../data/ethnobotany_utilitarian.csv` | `../data/ethnobotany_utilitarian.csv` (same — relative to `content/`) |

---

## Files to add / change in your repo

### 1. Add these new files

```
content/
├── utility_dashboard.qmd   ← new (provided)
└── dashboard.css           ← new (provided)

data/
└── ethnobotany_utilitarian.csv   ← already exists / replace with updated
```

### 2. Replace `_quarto.yml` in repo root

Add one entry to the sidebar `contents:` list (or replace the whole file with the provided `_quarto.yml`):

```yaml
    contents:
      - href: index.qmd
        text: Home
      - href: content/folderStructure.qmd
        text: "Folder Structure & Content"
      - href: content/qmd_withCode.qmd
        text: "Adding Executable Code"
      # ── ADD THIS ──
      - href: content/utility_dashboard.qmd
        text: "Life Cycle Dashboard"
```

### 3. Add icon images to `content/images/`

Place the 6 SVG icon files there (included in the original project zip, or swap for your own PNGs):

```
content/images/
├── seeds_icon.svg
├── plant_icon.svg
├── harvest_icon.svg
├── create_icon.svg
├── culture_icon.svg
└── connection_icon.svg
```

To use PNGs instead, rename to `seeds_icon.png` etc. and update the `icon:` references in `utility_dashboard.qmd` to match.

---

## Render and deploy

```bash
# From repo root
quarto render

# Then push — GitHub Pages auto-deploys from docs/ on main
git add .
git commit -m "Add ethnobotany life cycle dashboard"
git push
```

The dashboard will be live at:
`https://shannonrankin.github.io/ethnobotany/content/utility_dashboard.html`

And it will appear as **"Life Cycle Dashboard"** in the left sidebar navigation.

---

## Adding plant photos

Name photos using this pattern and place in `content/images/`:

```
[name_kumeyaay]_[stage]_anydescription.jpg
```

Examples:
- `kupall_seeds_berries.jpg`
- `kupall_flowers_spring.jpg`  
- `kupall_plant_shrub.jpg`
- `kupall_harvest_branches.jpg`

The dashboard auto-detects images by matching the plant's Kumeyaay name and the stage keyword in the filename.

---

## Notes on the cosmo theme

The dashboard CSS uses `!important` on a small number of heading rules (`h1`, `h2`, `h3` inside dashboard components) because cosmo's SCSS applies its own heading styles at high specificity. This is intentional and scoped only to `.dash-header`, `.panel-heading`, and `.panel-subheading` — it won't affect any other pages on the site.

If you ever update `theme.scss` or `theme-dark.scss` and notice dashboard headings look off, check those three selectors in `dashboard.css`.
