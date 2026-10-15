# Kitti Onthong (Galacgolf) Portfolio

Personal engineering portfolio for **portfolio.galaclab.com**.

## Architecture

- Portfolio / Resume / Experience — this repository
- Commercial services — https://galaclab.com/
- Production hosting — Vercel
- Quality gates — GitHub Actions + Lighthouse CI

## Local preview

```bash
python3 -m http.server 8080
```

## Quality

```bash
python3 scripts/check-site.py
npx --yes @lhci/cli@0.15.x autorun --config=.lighthouserc.json
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for Vercel project/domain setup.
