#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime

# Simple markdown to HTML converter
def md_to_html(text):
    # Convert headers
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Convert bold and italic
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Convert links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    
    # Convert paragraphs
    paragraphs = text.split('\n\n')
    html_paragraphs = []
    for p in paragraphs:
        if not p.strip().startswith('<'):
            html_paragraphs.append(f'<p>{p.strip()}</p>')
        else:
            html_paragraphs.append(p)
    
    return '\n'.join(html_paragraphs)

# Parse front matter
def parse_frontmatter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = {}
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"')
            body = parts[2].strip()
            return frontmatter, body
    return {}, content

# Template for individual thought posts
def thought_template(title, date, content):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Joel Mulyadi</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container">
        <div class="content">
            <h2 class="page-title">{title}</h2>
            <div class="thought-date">{date}</div>
            <div class="thought-content">
                {content}
            </div>
        </div>
        
        <nav class="sidebar">
            <h1>Joel Mulyadi</h1>
            <ul>
                <li><a href="/about.html">About</a></li>
                <li><a href="/thoughts.html">Thoughts</a></li>
                <li><a href="/questions.html">Questions</a></li>
                <li><a href="/readings.html">Readings</a></li>
            </ul>
        </nav>
    </div>
</body>
</html>'''

# Build thoughts
def build_thoughts():
    thoughts_dir = Path('_thoughts')
    if not thoughts_dir.exists():
        return []
    
    thoughts = []
    Path('thoughts').mkdir(exist_ok=True)
    
    for md_file in thoughts_dir.glob('*.md'):
        content = md_file.read_text()
        frontmatter, body = parse_frontmatter(content)
        
        title = frontmatter.get('title', md_file.stem)
        date = frontmatter.get('date', '')
        html_content = md_to_html(body)
        
        # Create individual post HTML
        post_html = thought_template(title, date, html_content)
        post_file = Path('thoughts') / f'{md_file.stem}.html'
        post_file.write_text(post_html)
        
        thoughts.append({
            'title': title,
            'date': date,
            'slug': md_file.stem,
            'excerpt': body[:200] + '...' if len(body) > 200 else body
        })
    
    return sorted(thoughts, key=lambda x: x['date'], reverse=True)

# Build thoughts listing page
def build_thoughts_listing(thoughts):
    items_html = ''
    for thought in thoughts:
        items_html += f'''
            <div class="thought-item">
                <h3 class="thought-title"><a href="/thoughts/{thought['slug']}.html">{thought['title']}</a></h3>
                <div class="thought-date">{thought['date']}</div>
                <p>{thought['excerpt']}</p>
            </div>
        '''
    
    if not items_html:
        items_html = '<p>Coming soon...</p>'
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thoughts - Joel Mulyadi</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container">
        <div class="content">
            <h2 class="page-title">Thoughts</h2>
            {items_html}
        </div>
        
        <nav class="sidebar">
            <h1>Joel Mulyadi</h1>
            <ul>
                <li><a href="/about.html">About</a></li>
                <li><a href="/thoughts.html">Thoughts</a></li>
                <li><a href="/questions.html">Questions</a></li>
                <li><a href="/readings.html">Readings</a></li>
            </ul>
        </nav>
    </div>
</body>
</html>'''
    
    Path('thoughts.html').write_text(html)

# Build questions listing
def build_questions():
    questions_dir = Path('_questions')
    if not questions_dir.exists():
        questions_dir.mkdir()
        return []
    
    questions = []
    for md_file in questions_dir.glob('*.md'):
        content = md_file.read_text()
        frontmatter, _ = parse_frontmatter(content)
        
        questions.append({
            'question': frontmatter.get('question', ''),
            'note': frontmatter.get('note', ''),
            'order': int(frontmatter.get('order', 0))
        })
    
    return sorted(questions, key=lambda x: x['order'])

def build_questions_page(questions):
    items_html = ''
    for q in questions:
        note_html = f'<div class="question-note">{q["note"]}</div>' if q['note'] else ''
        items_html += f'''
            <div class="question-item">
                <div class="question-text">{q['question']}</div>
                {note_html}
            </div>
        '''
    
    if not items_html:
        items_html = '''
            <div class="question-item">
                <div class="question-text">What business vehicles will dominate wealth creation in 2025-2045?</div>
                <div class="question-note">Exploring why certain organizational structures emerge as dominant in different eras.</div>
            </div>
        '''
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Questions - Joel Mulyadi</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container">
        <div class="content">
            <h2 class="page-title">Questions</h2>
            <p style="margin-bottom: 30px; color: #666;">Big questions I'm working on over time.</p>
            {items_html}
        </div>
        
        <nav class="sidebar">
            <h1>Joel Mulyadi</h1>
            <ul>
                <li><a href="/about.html">About</a></li>
                <li><a href="/thoughts.html">Thoughts</a></li>
                <li><a href="/questions.html">Questions</a></li>
                <li><a href="/readings.html">Readings</a></li>
            </ul>
        </nav>
    </div>
</body>
</html>'''
    
    Path('questions.html').write_text(html)

# Build readings
def build_readings():
    readings_dir = Path('_readings')
    if not readings_dir.exists():
        readings_dir.mkdir()
        return []
    
    readings = []
    for md_file in readings_dir.glob('*.md'):
        content = md_file.read_text()
        frontmatter, _ = parse_frontmatter(content)
        
        readings.append({
            'title': frontmatter.get('title', ''),
            'url': frontmatter.get('url', ''),
            'quote': frontmatter.get('quote', ''),
            'date': frontmatter.get('date', '')
        })
    
    return sorted(readings, key=lambda x: x['date'], reverse=True)

def build_readings_page(readings):
    items_html = ''
    for r in readings:
        items_html += f'''
            <div class="reading-item">
                <h3 class="reading-title"><a href="{r['url']}" target="_blank">{r['title']}</a></h3>
                <div class="reading-quote">"{r['quote']}"</div>
            </div>
        '''
    
    if not items_html:
        items_html = '<p>Coming soon...</p>'
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Readings - Joel Mulyadi</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container">
        <div class="content">
            <h2 class="page-title">Readings</h2>
            <p style="margin-bottom: 30px; color: #666;">Articles and pieces I've found interesting.</p>
            {items_html}
        </div>
        
        <nav class="sidebar">
            <h1>Joel Mulyadi</h1>
            <ul>
                <li><a href="/about.html">About</a></li>
                <li><a href="/thoughts.html">Thoughts</a></li>
                <li><a href="/questions.html">Questions</a></li>
                <li><a href="/readings.html">Readings</a></li>
            </ul>
        </nav>
    </div>
</body>
</html>'''
    
    Path('readings.html').write_text(html)

# Main build function
def main():
    print("Building site...")
    
    # Build all sections
    thoughts = build_thoughts()
    build_thoughts_listing(thoughts)
    print(f"Built {len(thoughts)} thoughts")
    
    questions = build_questions()
    build_questions_page(questions)
    print(f"Built {len(questions)} questions")
    
    readings = build_readings()
    build_readings_page(readings)
    print(f"Built {len(readings)} readings")
    
    print("Build complete!")

if __name__ == '__main__':
    main()
