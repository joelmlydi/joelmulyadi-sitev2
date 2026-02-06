# Joel Mulyadi - Personal Website

Lightning-fast personal website inspired by Patrick Collison's minimalist design.

## Features

- ⚡ **Ultra-fast loading** - Pure HTML/CSS, no JavaScript bloat
- 📱 **Mobile-friendly CMS** - Write and update from anywhere
- 🚀 **Auto-deployment** - Changes go live instantly
- 💰 **100% Free** - No ongoing costs beyond domain

## Structure

```
.
├── index.html          # Homepage
├── about.html          # About page
├── thoughts.html       # Blog listing (auto-generated)
├── questions.html      # Big questions (auto-generated)
├── readings.html       # Curated articles (auto-generated)
├── css/
│   └── style.css      # Minimal styling
├── admin/
│   ├── index.html     # CMS interface
│   └── config.yml     # CMS configuration
├── _thoughts/         # Markdown files for blog posts
├── _questions/        # Markdown files for questions
├── _readings/         # Markdown files for reading notes
└── build.py          # Converts markdown to HTML
```

## Setup Instructions

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. Name it `joelmulyadi-site` (or whatever you prefer)
3. Make it **public** (required for free Netlify)
4. Don't initialize with README (we already have files)

### 2. Push Code to GitHub

```bash
cd joelmulyadi-site
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/joelmulyadi-site.git
git push -u origin main
```

### 3. Deploy to Netlify

1. Go to https://app.netlify.com/signup (sign up with GitHub)
2. Click "Add new site" → "Import an existing project"
3. Choose GitHub and authorize
4. Select your `joelmulyadi-site` repository
5. Build settings should auto-detect:
   - Build command: `python build.py`
   - Publish directory: `.`
6. Click "Deploy site"

### 4. Enable CMS (Identity & Git Gateway)

1. In Netlify dashboard, go to "Site settings" → "Identity"
2. Click "Enable Identity"
3. Under "Registration preferences", select "Invite only"
4. Under "External providers", enable GitHub
5. Go to "Services" → "Git Gateway" and click "Enable Git Gateway"

### 5. Invite Yourself to CMS

1. Go to "Identity" tab in Netlify dashboard
2. Click "Invite users"
3. Enter your email address
4. Check your email and accept the invitation

### 6. Set Up Custom Domain

Your Netlify site will have a URL like `random-name-123.netlify.app`

1. In Netlify dashboard, go to "Domain settings"
2. Click "Add custom domain"
3. Enter `joelmulyadi.com`
4. Netlify will give you DNS records

Go back to Spaceship:
1. Click "Custom DNS Records" 
2. Add an **A Record**:
   - Name: `@`
   - Value: `75.2.60.5` (Netlify's IP)
3. Add a **CNAME Record**:
   - Name: `www`
   - Value: `your-site-name.netlify.app`

Wait 5-30 minutes for DNS to propagate.

### 7. Access the CMS

Once deployed, you can access the CMS at:
`https://joelmulyadi.com/admin/`

Login with the email you invited, and you can start writing!

## How to Update Content

### From Computer or Phone:

1. Go to `https://joelmulyadi.com/admin/`
2. Login
3. Click on "Thoughts", "Questions", or "Readings"
4. Click "New Thought" (or question/reading)
5. Write your content
6. Click "Publish"
7. Site updates automatically in 1-2 minutes!

### Directly from GitHub (advanced):

1. Go to your GitHub repo
2. Navigate to `_thoughts/`, `_questions/`, or `_readings/`
3. Create a new `.md` file with frontmatter:

```markdown
---
title: "My First Post"
date: "2026-02-06"
---

Your content here...
```

4. Commit the file
5. Site rebuilds automatically

## Customization

### Change About Page Content
Edit `index.html` and `about.html` directly in GitHub or locally.

### Add Your Photo
1. Upload a photo named `photo.jpg` to the root directory
2. Optimal size: 400x400px

### Modify Styles
Edit `css/style.css` to change colors, fonts, spacing, etc.

## Troubleshooting

**CMS won't load:**
- Make sure Git Gateway is enabled in Netlify
- Make sure you've accepted the Identity invitation
- Check browser console for errors

**Changes not appearing:**
- Check Netlify deploy logs
- Make sure `build.py` ran successfully
- DNS changes take 5-30 minutes

**Site not accessible:**
- Verify DNS records in Spaceship
- Wait for DNS propagation (up to 48 hours, usually 30 minutes)
- Try accessing directly via Netlify URL first

## Support

For questions or issues:
- Netlify Docs: https://docs.netlify.com
- Decap CMS Docs: https://decapcms.org/docs/
- GitHub Issues: Create an issue in your repo
