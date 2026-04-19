# MLB Batting Lineup Optimization

**Independent Study Project** | Spring 2026 | [Back to Portfolio](../)

This project uses linear programming to construct an optimized baseball batting lineup under realistic roster and defensive constraints. Player offensive value is approximated using wRC+, and the model assigns hitters to lineup spots to maximize projected offensive output.

## Key Findings

- The constrained optimal lineup produces lower projected offensive output than the unconstrained benchmark.
- Defensive position requirements create a measurable opportunity cost.
- Optimization helps identify where roster limitations reduce lineup flexibility.

## Files

- `main.tex` — LaTeX source for the written report
- `batting_lineup_optimization_report.pdf` — compiled report
- `analysis.py` — Python optimization script
- `README.md` — project overview

## How to Rebuild

```bash
python analysis.py
pdflatex main.tex
pdflatex main.tex
```

## Tools Used

- Python
- pandas
- PuLP
- LaTeX
- linear programming

---

*Part of my Independent Study: Sports Analytics portfolio.*
