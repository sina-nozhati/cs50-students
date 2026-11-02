# Kb Doc Page Overrides

> **PROJECT:** CS50x Anzali  
> **Page Type:** Knowledge-base document reader  
> **Brand:** Locked to Harvard Crimson — see `BRAND_OVERRIDE.md`

> ⚠️ **IMPORTANT:** Rules in this file **override** the Master file (`design-system/MASTER.md`).  
> Only deviations from the Master are documented here.

---

## Brand lock (non-negotiable)

| نقش | مقدار |
|-----|--------|
| Primary / CTA / badges OFFICIAL | `#A51C30` (Crimson) |
| Primary dark / GENERATED badge | `#771020` |
| Tint / GENERATED wash | `#FBEAEE` |
| Page background | `#FAFAF7` |
| Text | `#1E1E1E` |
| Muted | `#334155` |
| Font | Vazirmatn |

**ممنوع:** بنفش/ایندیگو، کرم گرم `#F4F1EA`، گلو، ایموجی، پیل‌های رنگی غیربرند.

---

## Page-Specific Rules

### Layout

- Single reading column (max-width ~48–56rem for prose); hub week page may use 2-col child cards.
- Sections order on **doc**: breadcrumb → title + badges → child links → TOC → OFFICIAL → GENERATED → CC footer.
- Sections order on **week hub**: breadcrumb → hero → topics → official links → children cards → GENERATED checklist → OFFICIAL summary → mark-read → downloads → footer.

### Typography

- Body: Vazirmatn, ~0.95rem, line-height 1.75 (`.kb-prose`).
- Code / pre: monospace, **`direction: ltr`**, `unicode-bidi: isolate`.
- Headings in prose: crimson-dark accent on h3; h2 with hairline border.

### Color

- Links and focus rings: Crimson only.
- `.kb-official`: crimson left/right border (RTL-aware `border-inline-start`).
- `.kb-generated`: crimson-tint wash + crimson-dark edge — not amber/cream.
- Badges: solid Crimson / crimson-dark text on white — no purple chips.

### Components

- Cards only for interactive containers (child nav, TOC, prose shell).
- Mark-read via HTMX fragment; SVG icons, `cursor-pointer`, 150–300ms transitions.
- Footer must credit **CS50x / Harvard / David J. Malan** and **CC BY-NC-SA 4.0**.

### UX

- TOC shown when ≥2 headings; anchors match heading `id`s from renderer.
- Mobile-first RTL; official external links open in new tab with `rel="noopener"`.
