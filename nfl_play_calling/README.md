# NFL Play Calling Optimization

**Independent Study Project** | Spring 2026 | [Back to Portfolio](../)

This project analyzes NFL play-calling efficiency using 2023 nflfastR data and Expected Points Added (EPA). It examines game situations such as down, distance, and field position to evaluate where teams may be favoring run or pass decisions that differ from the most efficient option.

## Key Findings
- Passing shows a clear EPA advantage in several long-yardage and opponent-territory situations.
- Teams often remain conservative in situations where passing appears more efficient.
- The results suggest there may be opportunities to improve offensive decision-making in certain game contexts.

## Quick View
- [Full Report PDF](nfl-play-calling-report.pdf)
- [LaTeX Source](main.tex)
- [Visuals](figures/)

| Situation Example | Pass Advantage (EPA) | Actual Pass % | Interpretation |
|-------------------|----------------------|---------------|----------------|
| 2nd & Long, Red Zone | +0.25 | 45% | Underused |
| 3rd & Short, Own Territory | -0.12 | 30% | Overused |

## How to Rebuild
```bash
pdflatex main.tex
pdflatex main.tex
```

**Tools:** R, nflfastR, tidyverse, LaTeX, Overleaf.

---

*Part of my Independent Study: Sports Analytics portfolio.*
