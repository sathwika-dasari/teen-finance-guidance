import os

files = ['home.html', 'lessons.html', 'dashboard.html', 'profile.html', 'parttime.html']
html_link = '''            <a href="/internships" class="nav-item">
                <i class="fas fa-briefcase nav-icon"></i>
                <span>Internships</span>
            </a>
            <button id="logout-btn"'''

for f in files:
    path = f'c:/Teen App/teen-finance-guidance/frontend/screens/{f}'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # We look for the logout button and insert before it
        if '<button id="logout-btn"' in content and '/internships' not in content:
            new_content = content.replace('            <button id="logout-btn"', html_link)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"Skipped {f}")
    except Exception as e:
        print(f"Error {f}: {e}")
