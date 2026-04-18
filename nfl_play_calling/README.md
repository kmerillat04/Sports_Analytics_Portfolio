# NFL Play Calling Optimization

**Independent Study Project** | Spring 2026 | [Back to Portfolio](../)

Analyzes NFL play-calling efficiency using 2023 nflfastR data and Expected Points Added (EPA). Identifies game situations (down, distance, field position) where teams underuse optimal pass/run decisions.

[![Pass Calling Efficiency](https://via.placeholder.com/800x400/0d1117/ffffff?text=play_calling_efficiency.png)](nfl-play-calling-report.pdf)

## 🎯 Key Findings
- Passing shows clear EPA edge in long-yardage (7+ yds) and opponent territory situations.
- Teams often run conservatively despite data favoring passes (e.g., 2nd & long, midfield).
- Opportunities for ~0.1–0.3 EPA gains via adjusted tendencies.

## 📊 Quick View
- **[Full Report PDF](nfl-play-calling-report.pdf)** (8 pages)
- **[LaTeX Source](main.tex)** + [R Analysis Code](analysis.R)
- [Visuals Folder](figures/) (if separate)

| Situation Example | Pass Advantage (EPA) | Actual Pass % | Optimal? |
|-------------------|----------------------|---------------|----------|
| 2nd & Long, Red Zone | +0.25 | 45% | Underused |
| 3rd & Short, Own Territory | -0.12 | 30% | Overused |

## 🛠️ How to Rebuild
```bash
# Requires R + nflfastR, or compile LaTeX
pdflatex main.tex  # Run 2x for refs
```

**Tools**: R (nflfastR, tidyverse), LaTeX/Overleaf, EPA modeling.

---

*Part of [Independent Study Portfolio](../). Code/data public for reproducibility.*
