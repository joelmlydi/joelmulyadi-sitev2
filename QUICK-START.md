# Quick Start Guide

Follow these steps to get your site live in ~15 minutes:

## Prerequisites
- GitHub account (free)
- Netlify account (free - sign up with GitHub)

## Step-by-Step

### 1. Upload to GitHub (5 minutes)

```bash
# Navigate to the site folder
cd joelmulyadi-site

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Create repo on GitHub (go to https://github.com/new)
# Name: joelmulyadi-site
# Public repository
# Don't initialize with README

# Link to GitHub (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/joelmulyadi-site.git

# Push
git branch -M main
git push -u origin main
```

### 2. Deploy on Netlify (3 minutes)

1. Go to https://app.netlify.com (sign up with GitHub if needed)
2. Click "Add new site" → "Import an existing project"
3. Choose GitHub → Select `joelmulyadi-site` repo
4. Click "Deploy site" (settings auto-detect)
5. Wait ~1 minute for deployment

Your site is now live at `https://random-name.netlify.app`!

### 3. Set Up CMS Access (3 minutes)

In Netlify dashboard:

1. Go to "Site settings" → "Identity" → Click "Enable Identity"
2. Under "Registration", select "Invite only"
3. Under "Services" → "Git Gateway" → Click "Enable Git Gateway"
4. Go to "Identity" tab → "Invite users" → Enter your email
5. Check email → Accept invitation → Set password

Now go to `https://your-site.netlify.app/admin/` and login!

### 4. Point Your Domain (5 minutes)

In Netlify:
1. "Domain settings" → "Add custom domain" → Enter `joelmulyadi.com`
2. Netlify shows you the DNS records needed

In Spaceship:
1. Go to "Custom DNS Records"
2. Add **A Record**: Name = `@`, Value = `75.2.60.5`
3. Add **CNAME**: Name = `www`, Value = `your-site.netlify.app`

Wait 5-30 minutes, then visit `https://joelmulyadi.com` ✨

### 5. Start Writing!

Go to `https://joelmulyadi.com/admin/` and start creating:
- Thoughts (blog posts)
- Questions (big questions you're exploring)
- Readings (articles with quotes)

Changes go live automatically in 1-2 minutes!

## Customize

**Add your photo:**
- Upload a `photo.jpg` (400x400px works best)
- Replace the placeholder in the root directory

**Edit about page:**
- Open `index.html` and `about.html`
- Update the text to match your story

**Change styling:**
- Edit `css/style.css`
- Modify colors, fonts, spacing as desired

## Mobile Access

The CMS works great on mobile! Just visit:
`https://joelmulyadi.com/admin/`

Login and you can write/edit from anywhere.

---

Need help? Check the full README.md for detailed troubleshooting.
