# Vercel Deployment

Production domain: **https://portfolio.galaclab.com/**

## Project setup

Import this repository into Vercel:

- Repository: `ggolfko/ggolfko.github.io`
- Production branch: `master`
- Framework preset: `Other`
- Root directory: repository root
- Build command: leave empty
- Output directory: leave empty

This repository remains named `ggolfko.github.io`, but production hosting is Vercel. GitHub Pages can stay enabled temporarily as a preview/fallback while migration is completed.

## Domain

Attach:

- `portfolio.galaclab.com`

The portfolio canonical URLs, Open Graph URLs, robots.txt, and sitemap already point to `portfolio.galaclab.com`.

## Git flow

- Pull request / branch -> Vercel Preview Deployment
- Merge or push to `master` -> Vercel Production Deployment
- GitHub Actions -> static validation + Lighthouse CI

## Migration check

After the first production deployment, verify:

- `/`
- `/Kitti-Onthong-Resume.pdf`
- `/robots.txt`
- `/sitemap.xml`

Then point the DNS record for `portfolio.galaclab.com` to the value Vercel requests.

The legacy `v1/` directory is excluded from Vercel deployment.
