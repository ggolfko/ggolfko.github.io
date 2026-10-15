# Portfolio VPS deployment

Target: `portfolio.galaclab.com` -> `/srv/portfolio/current`.

Use the same DigitalOcean VPS and deploy user as Galaclab.

GitHub environment `production` secrets:
- `VPS_HOST`
- `VPS_USER`
- `VPS_PORT` (optional)
- `VPS_SSH_KEY`
- `PORTFOLIO_HEALTHCHECK_URL` = `https://portfolio.galaclab.com/`

Install `infra/nginx/portfolio.galaclab.com.conf` on the VPS, then after DNS resolves:
```bash
sudo certbot --nginx -d portfolio.galaclab.com
```
