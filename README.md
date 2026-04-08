# Priyanka Mangrulkar — Portfolio

Personal portfolio website for Priyanka Mangrulkar — Data Analyst, Data Scientist & BI Developer based in Boston.

Built as a single-file static site (HTML + Tailwind CSS via CDN + vanilla JS) — dark minimalist theme, single-page scroll, smooth animations, project cards. No build step required.

## Quick Preview

Just open `index.html` in a browser.

## Deploy

### Option 1 — Vercel (recommended, 1 minute)
1. Push this folder to a new GitHub repo.
2. Go to https://vercel.com/new, import the repo.
3. Framework preset: **Other**. Click **Deploy**. Done.

### Option 2 — GitHub Pages
1. Create a new GitHub repo named `priyanka-portfolio` (or `<username>.github.io` for a root domain).
2. Push the files:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio"
   git branch -M main
   git remote add origin https://github.com/<username>/priyanka-portfolio.git
   git push -u origin main
   ```
3. In the repo: **Settings → Pages → Source: Deploy from branch → main / (root)**.
4. Site will be live at `https://<username>.github.io/priyanka-portfolio/`.

### Option 3 — Custom domain
After deploying to Vercel or GitHub Pages, add your domain in the project settings and update your DNS A/CNAME records as instructed.

## Customization

All content lives in `index.html`:
- **Hero / About**: top `<section>` blocks — edit text directly.
- **Experience**: the `#experience` section.
- **Projects**: edit the `projects` array in the `<script>` block at the bottom. Add `image`, `live`, `github` as needed.
- **Skills**: edit the `skills` object in the same script.
- **Colors**: tweak the `accent` color in the `tailwind.config` block (currently lime `#a3e635`).

## Structure

```
priyanka-portfolio/
├── index.html    # Entire site (content, styles, scripts)
└── README.md     # This file
```

## Suggested next steps
- Add a profile photo in the Hero section.
- Add project screenshots (drop images in an `/images` folder and reference them in the `projects` array).
- Add a `resume.pdf` link in the Contact section.
