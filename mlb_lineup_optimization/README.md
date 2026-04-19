# Batting Lineup Optimization Using Linear Programming

**Independent Study Project** | Spring 2026 | [Back to Portfolio](../)

This project uses linear programming to construct an optimized baseball batting lineup under realistic roster and defensive constraints. Player offensive value is approximated using wRC+, and the model assigns hitters to lineup spots in a way that maximizes projected offensive output.

## Key Findings
- The constrained optimal lineup produces a lower projected offensive output than the unconstrained version.
- Defensive position requirements create a measurable opportunity cost.
- Optimization helps identify where roster limitations reduce lineup flexibility.

## Quick View
- [Full Report PDF](batting-lineup-optimization-report.pdf)
- [LaTeX Source](main.tex)
- [Python Code](analysis.py)
- [Figures](figures/)

| Lineup Type | Projected wRC+ | Notes |
|-------------|----------------|-------|
| Constrained Optimal | 963 | Includes defensive requirements |
| Unconstrained Optimal | 979 | Best possible offensive arrangement |

## How to Rebuild
```bash
pdflatex main.tex
pdflatex main.tex
```

**Tools:** Python, PuLP, pandas, LaTeX, linear optimization.

---

*Part of my Independent Study: Sports Analytics portfolio.*
