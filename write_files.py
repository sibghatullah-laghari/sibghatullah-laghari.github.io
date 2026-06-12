import os

BASE = r'c:\Users\sibla\Downloads\sibghatullah-laghari.github.io\src'

def w(rel, content):
    p = os.path.join(BASE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print('✔ written:', rel)

# ═══════════════════════════════════════════════════════════
# BaseLayout
# ═══════════════════════════════════════════════════════════
w('layouts/BaseLayout.astro', """\
---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';

export interface Props {
  title?: string;
  description?: string;
}

const {
  title = 'Sibghatullah Laghari | Backend Developer',
  description = 'Java Spring Boot Backend Developer — building secure, scalable APIs.',
} = Astro.props;
---
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content={description} />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style is:global>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-family: 'Inter', system-ui, sans-serif; }
    body { background-color: #0a0a0f; color: #e2e8f0; }
    ::selection { background: #4f46e5; color: #fff; }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #0f0f1a; }
    ::-webkit-scrollbar-thumb { background: #4f46e5; border-radius: 3px; }
    .gradient-text {
      background: linear-gradient(135deg, #818cf8, #c7d2fe, #a5b4fc);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    .card-hover { transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease; }
    .card-hover:hover { transform: translateY(-4px); box-shadow: 0 20px 40px rgba(99,102,241,0.15); border-color: #4f46e5 !important; }
    .section-divider { border: none; height: 1px; background: linear-gradient(to right, transparent, #2a2a4a, transparent); }
    .btn-primary {
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: #4f46e5; color: #fff; font-weight: 600; font-size: 0.875rem;
      padding: 0.625rem 1.5rem; border-radius: 0.5rem;
      transition: background 0.2s, transform 0.2s;
      text-decoration: none;
    }
    .btn-primary:hover { background: #4338ca; transform: translateY(-1px); }
    .btn-outline {
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: transparent; color: #94a3b8; font-weight: 600; font-size: 0.875rem;
      padding: 0.625rem 1.5rem; border-radius: 0.5rem;
      border: 1px solid rgba(255,255,255,0.1);
      transition: border-color 0.2s, color 0.2s, transform 0.2s;
      text-decoration: none;
    }
    .btn-outline:hover { border-color: #4f46e5; color: #fff; transform: translateY(-1px); }
    .tag {
      display: inline-block; padding: 0.2rem 0.65rem; border-radius: 9999px;
      font-size: 0.7rem; font-weight: 600; letter-spacing: 0.03em;
      background: rgba(99,102,241,0.15); color: #a5b4fc; border: 1px solid rgba(99,102,241,0.25);
    }
    section { padding: 5rem 1.5rem; }
    .container { max-width: 72rem; margin: 0 auto; }
  </style>
</head>
<body>
  <Navbar />
  <main>
    <slot />
  </main>
  <Footer />
</body>
</html>
""")

# ═══════════════════════════════════════════════════════════
# Navbar
# ═══════════════════════════════════════════════════════════
w('components/Navbar.astro', """\
---
const navLinks = [
  { href: '/', label: 'Home' },
  { href: '/experience', label: 'Experience' },
  { href: '/working', label: 'What I Do' },
  { href: '/projects', label: 'Projects' },
  { href: '/blog', label: 'Blog' },
  { href: '/contact', label: 'Contact' },
];
const current = Astro.url.pathname;
---
<header style="position:sticky;top:0;z-index:50;background:rgba(10,10,15,0.85);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,0.06);">
  <nav class="container" style="display:flex;align-items:center;justify-content:space-between;padding:1rem 1.5rem;">
    <a href="/" style="display:flex;align-items:center;gap:0.5rem;text-decoration:none;">
      <span style="width:2rem;height:2rem;border-radius:0.5rem;background:#4f46e5;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:0.75rem;flex-shrink:0;">SL</span>
      <span style="font-weight:600;color:#fff;font-size:1rem;">Sibghatullah</span>
    </a>
    <ul style="display:none;gap:0.25rem;list-style:none;" id="desktop-nav" class="desktop-nav-list">
      {navLinks.map(link => (
        <li>
          <a
            href={link.href}
            style={`text-decoration:none;padding:0.4rem 0.75rem;border-radius:0.5rem;font-size:0.875rem;font-weight:500;transition:background 0.2s,color 0.2s;${
              (current === link.href || (link.href !== '/' && current.startsWith(link.href)))
                ? 'background:rgba(79,70,229,0.2);color:#a5b4fc;'
                : 'color:#94a3b8;'
            }`}
          >{link.label}</a>
        </li>
      ))}
    </ul>
    <button id="mobile-menu-btn" aria-label="Toggle menu" style="background:none;border:none;cursor:pointer;color:#94a3b8;padding:0.5rem;display:none;" class="mobile-btn">
      <svg id="icon-open" xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
      <svg id="icon-close" xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:none;">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
    </button>
  </nav>
  <div id="mobile-menu" style="display:none;padding:0.5rem 1.5rem 1rem;border-top:1px solid rgba(255,255,255,0.06);">
    <ul style="list-style:none;display:flex;flex-direction:column;gap:0.25rem;">
      {navLinks.map(link => (
        <li>
          <a href={link.href} style={`display:block;text-decoration:none;padding:0.5rem 1rem;border-radius:0.5rem;font-size:0.875rem;font-weight:500;transition:background 0.2s,color 0.2s;${
            current === link.href ? 'background:rgba(79,70,229,0.2);color:#a5b4fc;' : 'color:#94a3b8;'
          }`}>{link.label}</a>
        </li>
      ))}
    </ul>
  </div>
</header>
<style>
  @media (min-width: 768px) {
    .desktop-nav-list { display: flex !important; }
    .mobile-btn { display: none !important; }
    #mobile-menu { display: none !important; }
  }
  @media (max-width: 767px) {
    .mobile-btn { display: block !important; }
  }
</style>
<script>
  const btn = document.getElementById('mobile-menu-btn');
  const menu = document.getElementById('mobile-menu');
  const iconOpen = document.getElementById('icon-open');
  const iconClose = document.getElementById('icon-close');
  btn?.addEventListener('click', () => {
    const open = menu?.style.display === 'block';
    if (menu) menu.style.display = open ? 'none' : 'block';
    if (iconOpen) iconOpen.style.display = open ? 'block' : 'none';
    if (iconClose) iconClose.style.display = open ? 'none' : 'block';
  });
  // Hover effect for desktop nav links
  document.querySelectorAll('.desktop-nav-list a').forEach(a => {
    a.addEventListener('mouseenter', () => { if (!a.style.background.includes('79,70,229,0.2')) { (a as HTMLElement).style.background = 'rgba(255,255,255,0.05)'; (a as HTMLElement).style.color = '#fff'; } });
    a.addEventListener('mouseleave', () => { if (!a.style.background.includes('79,70,229,0.2')) { (a as HTMLElement).style.background = ''; (a as HTMLElement).style.color = '#94a3b8'; } });
  });
</script>
""")

# ═══════════════════════════════════════════════════════════
# Footer
# ═══════════════════════════════════════════════════════════
w('components/Footer.astro', """\
<footer style="background-color:#0f0f1a;border-top:1px solid rgba(255,255,255,0.06);">
  <div class="container" style="padding:2.5rem 1.5rem;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:1.5rem;">
      <div style="display:flex;align-items:center;gap:1.25rem;">
        <a href="https://github.com/sibghatullah-laghari" target="_blank" rel="noopener" aria-label="GitHub"
           style="color:#64748b;transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#64748b'">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
          </svg>
        </a>
        <a href="https://linkedin.com/in/sibghatullah-laghari" target="_blank" rel="noopener" aria-label="LinkedIn"
           style="color:#64748b;transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#64748b'">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
          </svg>
        </a>
        <a href="mailto:siblaghari@gmail.com" aria-label="Email"
           style="color:#64748b;transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#64748b'">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
          </svg>
        </a>
      </div>
      <p style="font-size:0.75rem;color:#334155;">&copy; 2026 Sibghatullah Laghari &middot; Built with Astro &amp; Tailwind CSS</p>
    </div>
  </div>
</footer>
""")

# ═══════════════════════════════════════════════════════════
# index.astro — Home / About
# ═══════════════════════════════════════════════════════════
w('pages/index.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const skills = [
  { name: 'Java', color: '#f89820' },
  { name: 'Spring Boot', color: '#6db33f' },
  { name: 'Spring Security', color: '#6db33f' },
  { name: 'JWT', color: '#a5b4fc' },
  { name: 'REST APIs', color: '#818cf8' },
  { name: 'PostgreSQL', color: '#336791' },
  { name: 'MySQL', color: '#00758f' },
  { name: 'Git & GitHub', color: '#f05032' },
  { name: 'Maven', color: '#c71a36' },
  { name: 'Docker (basics)', color: '#2496ed' },
  { name: 'Linux', color: '#fcc624' },
  { name: 'Postman', color: '#ff6c37' },
];
---
<BaseLayout title="Sibghatullah Laghari | Backend Developer">

  <!-- Hero -->
  <section style="min-height:90vh;display:flex;align-items:center;padding:5rem 1.5rem;background:radial-gradient(ellipse at 60% 20%, rgba(79,70,229,0.12) 0%, transparent 60%), #0a0a0f;">
    <div class="container">
      <div style="max-width:42rem;">
        <div style="display:inline-flex;align-items:center;gap:0.5rem;background:rgba(79,70,229,0.15);border:1px solid rgba(79,70,229,0.3);border-radius:9999px;padding:0.35rem 0.9rem;font-size:0.75rem;font-weight:600;color:#a5b4fc;letter-spacing:0.05em;margin-bottom:1.5rem;">
          <span style="width:6px;height:6px;border-radius:50%;background:#4ade80;display:inline-block;animation:pulse 2s infinite;"></span>
          AVAILABLE FOR OPPORTUNITIES
        </div>
        <h1 style="font-size:clamp(2.25rem,5vw,3.75rem);font-weight:800;line-height:1.15;color:#f8fafc;margin-bottom:1.25rem;">
          Hi, I'm <span class="gradient-text">Sibghatullah</span><br/>Laghari
        </h1>
        <p style="font-size:1.125rem;line-height:1.75;color:#94a3b8;margin-bottom:0.75rem;font-weight:400;">
          Java Spring Boot Backend Developer — I design and build secure, scalable REST APIs,
          database-driven systems, and JWT-authenticated services.
        </p>
        <p style="font-size:0.9rem;color:#475569;margin-bottom:2rem;">
          Software Engineering student · Quetta, Pakistan
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:0.75rem;">
          <a href="/projects" class="btn-primary">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
            View Projects
          </a>
          <a href="/contact" class="btn-outline">
            Get In Touch
          </a>
          <a href="https://github.com/sibghatullah-laghari" target="_blank" rel="noopener" class="btn-outline">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
            GitHub
          </a>
        </div>
      </div>
    </div>
    <style>
      @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }
    </style>
  </section>

  <hr class="section-divider" style="margin:0 auto;max-width:72rem;" />

  <!-- Skills -->
  <section style="padding:4rem 1.5rem;background:#0f0f1a;">
    <div class="container">
      <div style="text-align:center;margin-bottom:3rem;">
        <p style="font-size:0.75rem;font-weight:700;letter-spacing:0.1em;color:#4f46e5;text-transform:uppercase;margin-bottom:0.75rem;">TECH STACK</p>
        <h2 style="font-size:2rem;font-weight:700;color:#f8fafc;">Technologies I Work With</h2>
        <p style="color:#64748b;margin-top:0.5rem;font-size:0.95rem;">Backend-focused, always learning.</p>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:0.75rem;justify-content:center;">
        {skills.map(skill => (
          <div style={`display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.1rem;border-radius:0.5rem;background:#14141f;border:1px solid #1a1a2e;font-size:0.875rem;font-weight:500;color:#cbd5e1;transition:transform 0.2s,border-color 0.2s,box-shadow 0.2s;cursor:default;`}
               onmouseover="this.style.transform='translateY(-3px)';this.style.borderColor='#4f46e5';this.style.boxShadow='0 8px 24px rgba(99,102,241,0.18)'"
               onmouseout="this.style.transform='';this.style.borderColor='#1a1a2e';this.style.boxShadow=''">
            <span style={`width:8px;height:8px;border-radius:50%;background:${skill.color};display:inline-block;flex-shrink:0;`}></span>
            {skill.name}
          </div>
        ))}
      </div>
    </div>
  </section>

  <hr class="section-divider" style="margin:0 auto;max-width:72rem;" />

  <!-- Quick Stats -->
  <section style="padding:4rem 1.5rem;">
    <div class="container">
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1.5rem;">
        {[
          { num: '2+', label: 'Years Coding' },
          { num: '5+', label: 'Projects Built' },
          { num: '10+', label: 'APIs Designed' },
          { num: 'BSE', label: 'Student' },
        ].map(stat => (
          <div style="text-align:center;padding:2rem 1rem;background:#0f0f1a;border:1px solid #1a1a2e;border-radius:1rem;transition:border-color 0.2s,transform 0.2s;"
               onmouseover="this.style.borderColor='#4f46e5';this.style.transform='translateY(-3px)'"
               onmouseout="this.style.borderColor='#1a1a2e';this.style.transform=''">
            <div style="font-size:2.25rem;font-weight:800;background:linear-gradient(135deg,#818cf8,#c7d2fe);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">{stat.num}</div>
            <div style="font-size:0.85rem;color:#64748b;margin-top:0.25rem;font-weight:500;">{stat.label}</div>
          </div>
        ))}
      </div>
    </div>
  </section>

</BaseLayout>
""")

# ═══════════════════════════════════════════════════════════
# experience.astro
# ═══════════════════════════════════════════════════════════
w('pages/experience.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const experiences = [
  {
    role: 'Backend Developer (Self-employed / Freelance)',
    company: 'Personal Projects & Portfolio',
    period: '2023 – Present',
    location: 'Quetta, Pakistan (Remote)',
    description: 'Designing and building production-ready Spring Boot backend applications with RESTful APIs, JWT-based authentication, and relational database integration.',
    highlights: [
      'Built CCTRS – Carbon Contribution & Reward Tracking System with full REST API',
      'Implemented JWT authentication and role-based access control',
      'Designed normalized PostgreSQL schemas with Hibernate/JPA',
      'Used Postman for API testing and documentation',
      'Managed project versioning and collaboration via GitHub',
    ],
    tech: ['Java', 'Spring Boot', 'JWT', 'PostgreSQL', 'JPA/Hibernate', 'Maven', 'GitHub'],
  },
  {
    role: 'BSE Student — Software Engineering',
    company: 'University',
    period: '2022 – Present',
    location: 'Pakistan',
    description: 'Studying Software Engineering fundamentals including data structures, algorithms, database systems, OOP, and software design patterns.',
    highlights: [
      'Coursework: DSA, DBMS, OOP, Software Design, Networks',
      'Academic projects using Java and database-driven systems',
      'Collaborated in team projects with Git version control',
    ],
    tech: ['Java', 'SQL', 'Git', 'OOP', 'DSA'],
  },
];
---
<BaseLayout title="Experience | Sibghatullah Laghari">

  <section style="padding:5rem 1.5rem;min-height:80vh;">
    <div class="container">
      <div style="margin-bottom:3.5rem;">
        <p style="font-size:0.75rem;font-weight:700;letter-spacing:0.1em;color:#4f46e5;text-transform:uppercase;margin-bottom:0.75rem;">BACKGROUND</p>
        <h1 style="font-size:2.5rem;font-weight:800;color:#f8fafc;margin-bottom:0.75rem;">Experience</h1>
        <p style="color:#64748b;font-size:1rem;max-width:36rem;">My journey in backend development — from university projects to real-world systems.</p>
      </div>

      <!-- Timeline -->
      <div style="position:relative;">
        <!-- Timeline line -->
        <div style="position:absolute;left:1.25rem;top:0;bottom:0;width:2px;background:linear-gradient(to bottom,#4f46e5,rgba(79,70,229,0.1));border-radius:2px;" class="timeline-line"></div>

        <div style="display:flex;flex-direction:column;gap:2.5rem;padding-left:3.5rem;">
          {experiences.map((exp, i) => (
            <div style="position:relative;">
              <!-- Dot -->
              <div style="position:absolute;left:-2.75rem;top:1.5rem;width:1rem;height:1rem;border-radius:50%;background:#4f46e5;border:3px solid #0a0a0f;box-shadow:0 0 0 2px #4f46e5;flex-shrink:0;"></div>

              <div class="card-hover" style="background:#0f0f1a;border:1px solid #1a1a2e;border-radius:1rem;padding:1.75rem;transition:transform 0.25s,box-shadow 0.25s,border-color 0.25s;">
                <div style="display:flex;flex-wrap:wrap;align-items:flex-start;justify-content:space-between;gap:0.75rem;margin-bottom:1rem;">
                  <div>
                    <h3 style="font-size:1.125rem;font-weight:700;color:#f8fafc;">{exp.role}</h3>
                    <p style="font-size:0.9rem;color:#818cf8;font-weight:600;margin-top:0.2rem;">{exp.company}</p>
                  </div>
                  <div style="text-align:right;">
                    <span style="font-size:0.8rem;font-weight:600;color:#4f46e5;background:rgba(79,70,229,0.15);padding:0.3rem 0.75rem;border-radius:9999px;border:1px solid rgba(79,70,229,0.3);">{exp.period}</span>
                    <p style="font-size:0.75rem;color:#475569;margin-top:0.35rem;">{exp.location}</p>
                  </div>
                </div>

                <p style="color:#94a3b8;font-size:0.9rem;line-height:1.7;margin-bottom:1.25rem;">{exp.description}</p>

                <ul style="list-style:none;display:flex;flex-direction:column;gap:0.4rem;margin-bottom:1.25rem;">
                  {exp.highlights.map(h => (
                    <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;">
                      <span style="color:#4f46e5;margin-top:0.2rem;flex-shrink:0;">&#8227;</span>
                      {h}
                    </li>
                  ))}
                </ul>

                <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
                  {exp.tech.map(t => (
                    <span class="tag">{t}</span>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

    </div>
  </section>

  <style>
    @media (max-width: 640px) {
      .timeline-line { display: none; }
    }
  </style>
</BaseLayout>
""")

# ═══════════════════════════════════════════════════════════
# working.astro
# ═══════════════════════════════════════════════════════════
w('pages/working.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const services = [
  {
    icon: '&#9881;',
    title: 'REST API Development',
    description: 'Design and implement scalable, well-structured RESTful APIs following best practices — proper routing, HTTP verbs, status codes, and versioning.',
    tags: ['Spring Boot', 'REST', 'JSON', 'Postman'],
  },
  {
    icon: '&#128274;',
    title: 'Authentication & Security',
    description: 'Secure backends using JWT tokens, Spring Security, role-based access control (RBAC), and password hashing with BCrypt.',
    tags: ['JWT', 'Spring Security', 'BCrypt', 'RBAC'],
  },
  {
    icon: '&#128196;',
    title: 'Database Design',
    description: 'Design normalized relational database schemas, write complex queries, and integrate with Spring Data JPA / Hibernate ORM.',
    tags: ['PostgreSQL', 'MySQL', 'JPA', 'Hibernate'],
  },
  {
    icon: '&#128268;',
    title: 'Backend Architecture',
    description: 'Structure projects using layered (MVC) architecture — Controllers, Services, Repositories — keeping code clean, testable, and maintainable.',
    tags: ['MVC', 'Layered Architecture', 'Clean Code'],
  },
  {
    icon: '&#128202;',
    title: 'API Testing & Docs',
    description: 'Thoroughly test endpoints with Postman collections. Document APIs clearly so frontend teams and consumers can integrate with ease.',
    tags: ['Postman', 'API Docs', 'Testing'],
  },
  {
    icon: '&#128640;',
    title: 'Version Control & Collaboration',
    description: 'Work with Git and GitHub for source control, branching strategies, and team collaboration on shared codebases.',
    tags: ['Git', 'GitHub', 'Branching'],
  },
];
---
<BaseLayout title="What I Do | Sibghatullah Laghari">

  <section style="padding:5rem 1.5rem;min-height:80vh;background:radial-gradient(ellipse at 30% 0%, rgba(79,70,229,0.07) 0%, transparent 60%),#0a0a0f;">
    <div class="container">
      <div style="text-align:center;max-width:40rem;margin:0 auto 4rem;">
        <p style="font-size:0.75rem;font-weight:700;letter-spacing:0.1em;color:#4f46e5;text-transform:uppercase;margin-bottom:0.75rem;">CAPABILITIES</p>
        <h1 style="font-size:2.5rem;font-weight:800;color:#f8fafc;margin-bottom:1rem;">What I Do</h1>
        <p style="color:#64748b;font-size:1rem;line-height:1.7;">
          Focused on backend engineering — crafting the logic, security, and data layer that powers applications.
        </p>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem;">
        {services.map(s => (
          <div class="card-hover" style="background:#0f0f1a;border:1px solid #1a1a2e;border-radius:1rem;padding:1.75rem;display:flex;flex-direction:column;gap:1rem;">
            <div style="font-size:1.75rem;width:3rem;height:3rem;display:flex;align-items:center;justify-content:center;background:rgba(79,70,229,0.12);border-radius:0.75rem;border:1px solid rgba(79,70,229,0.2);" set:html={s.icon}></div>
            <div>
              <h3 style="font-size:1.05rem;font-weight:700;color:#f8fafc;margin-bottom:0.5rem;">{s.title}</h3>
              <p style="font-size:0.875rem;color:#64748b;line-height:1.7;">{s.description}</p>
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-top:auto;">
              {s.tags.map(t => <span class="tag">{t}</span>)}
            </div>
          </div>
        ))}
      </div>

    </div>
  </section>

</BaseLayout>
""")

# ═══════════════════════════════════════════════════════════
# projects.astro
# ═══════════════════════════════════════════════════════════
w('pages/projects.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const projects = [
  {
    title: 'CCTRS — Carbon Contribution & Reward Tracking System',
    description: 'A full-stack backend system that tracks users\\' carbon-reducing activities, calculates contribution scores, and rewards eco-friendly behaviour. Built with Spring Boot and PostgreSQL.',
    tech: ['Java', 'Spring Boot', 'Spring Security', 'JWT', 'PostgreSQL', 'JPA'],
    github: 'https://github.com/sibghatullah-laghari',
    demo: null,
    highlight: true,
    status: 'Completed',
  },
  {
    title: 'JWT Authentication Service',
    description: 'Standalone authentication microservice with user registration, login, JWT token issuance, refresh tokens, and role-based access control.',
    tech: ['Spring Boot', 'JWT', 'BCrypt', 'MySQL', 'Spring Security'],
    github: 'https://github.com/sibghatullah-laghari',
    demo: null,
    highlight: false,
    status: 'Completed',
  },
  {
    title: 'Student Management REST API',
    description: 'CRUD REST API for managing student records with pagination, filtering, and full Postman test suite. Demonstrates clean layered architecture.',
    tech: ['Spring Boot', 'PostgreSQL', 'JPA', 'REST', 'Maven'],
    github: 'https://github.com/sibghatullah-laghari',
    demo: null,
    highlight: false,
    status: 'Completed',
  },
  {
    title: 'Personal Portfolio Website',
    description: 'This very website — built with Astro and Tailwind CSS. Fast, static, and GitHub Pages deployed. No backend required.',
    tech: ['Astro', 'Tailwind CSS', 'GitHub Pages'],
    github: 'https://github.com/sibghatullah-laghari/sibghatullah-laghari.github.io',
    demo: 'https://sibghatullah-laghari.github.io',
    highlight: false,
    status: 'Live',
  },
];
---
<BaseLayout title="Projects | Sibghatullah Laghari">

  <section style="padding:5rem 1.5rem;min-height:80vh;">
    <div class="container">
      <div style="margin-bottom:3.5rem;">
        <p style="font-size:0.75rem;font-weight:700;letter-spacing:0.1em;color:#4f46e5;text-transform:uppercase;margin-bottom:0.75rem;">PORTFOLIO</p>
        <h1 style="font-size:2.5rem;font-weight:800;color:#f8fafc;margin-bottom:0.75rem;">Projects</h1>
        <p style="color:#64748b;font-size:1rem;max-width:36rem;">A collection of real projects — from concept to code to deployment.</p>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.5rem;">
        {projects.map(p => (
          <div class="card-hover" style={`background:#0f0f1a;border:1px solid ${p.highlight ? 'rgba(99,102,241,0.4)' : '#1a1a2e'};border-radius:1rem;padding:1.75rem;display:flex;flex-direction:column;gap:1rem;${p.highlight ? 'box-shadow:0 0 0 1px rgba(99,102,241,0.15);' : ''}`}>
            <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:0.5rem;">
              <h3 style="font-size:1rem;font-weight:700;color:#f8fafc;line-height:1.4;">{p.title}</h3>
              <span style={`flex-shrink:0;font-size:0.65rem;font-weight:700;padding:0.2rem 0.5rem;border-radius:9999px;${p.status === 'Live' ? 'background:rgba(74,222,128,0.15);color:#4ade80;border:1px solid rgba(74,222,128,0.3);' : 'background:rgba(99,102,241,0.15);color:#a5b4fc;border:1px solid rgba(99,102,241,0.3);'}`}>{p.status}</span>
            </div>

            <p style="font-size:0.875rem;color:#64748b;line-height:1.7;flex:1;">{p.description}</p>

            <div style="display:flex;flex-wrap:wrap;gap:0.35rem;">
              {p.tech.map(t => <span class="tag">{t}</span>)}
            </div>

            <div style="display:flex;gap:0.75rem;margin-top:0.25rem;">
              {p.github && (
                <a href={p.github} target="_blank" rel="noopener" class="btn-outline" style="font-size:0.8rem;padding:0.45rem 1rem;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                  Code
                </a>
              )}
              {p.demo && (
                <a href={p.demo} target="_blank" rel="noopener" class="btn-primary" style="font-size:0.8rem;padding:0.45rem 1rem;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                  Live Demo
                </a>
              )}
            </div>
          </div>
        ))}
      </div>

    </div>
  </section>

</BaseLayout>
""")

# ═══════════════════════════════════════════════════════════
# blog.astro
# ═══════════════════════════════════════════════════════════
w('pages/blog.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const posts = [
  {
    title: 'Understanding JWT Authentication in Spring Boot',
    excerpt: 'A deep dive into how JSON Web Tokens work and how to implement secure stateless authentication in Spring Boot applications.',
    date: 'Feb 2026',
    readTime: '8 min read',
    tags: ['Spring Boot', 'JWT', 'Security'],
    slug: '#',
    status: 'coming-soon',
  },
  {
    title: 'Designing RESTful APIs — Best Practices',
    excerpt: 'From proper resource naming and HTTP methods to status codes and versioning — everything you need to design clean, professional REST APIs.',
    date: 'Jan 2026',
    readTime: '6 min read',
    tags: ['REST API', 'Backend', 'Design'],
    slug: '#',
    status: 'coming-soon',
  },
  {
    title: 'Spring Data JPA vs Raw JDBC — When to Use Which',
    excerpt: 'Comparing Spring Data JPA and raw JDBC with practical examples, performance considerations, and when each approach makes sense.',
    date: 'Jan 2026',
    readTime: '7 min read',
    tags: ['JPA', 'Spring Boot', 'Database'],
    slug: '#',
    status: 'coming-soon',
  },
];
---
<BaseLayout title="Blog | Sibghatullah Laghari">

  <section style="padding:5rem 1.5rem;min-height:80vh;">
    <div class="container">
      <div style="margin-bottom:3.5rem;">
        <p style="font-size:0.75rem;font-weight:700;letter-spacing:0.1em;color:#4f46e5;text-transform:uppercase;margin-bottom:0.75rem;">WRITING</p>
        <h1 style="font-size:2.5rem;font-weight:800;color:#f8fafc;margin-bottom:0.75rem;">Blog</h1>
        <p style="color:#64748b;font-size:1rem;max-width:36rem;">Thoughts, guides, and notes on backend development, Spring Boot, and software engineering.</p>
      </div>

      <!-- Coming soon banner -->
      <div style="background:rgba(79,70,229,0.08);border:1px solid rgba(79,70,229,0.25);border-radius:1rem;padding:1.25rem 1.5rem;display:flex;align-items:center;gap:0.75rem;margin-bottom:2.5rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="#a5b4fc"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <p style="font-size:0.875rem;color:#94a3b8;">Blog posts are coming soon! These are planned articles I'll be publishing.</p>
      </div>

      <div style="display:flex;flex-direction:column;gap:1.25rem;">
        {posts.map(post => (
          <article class="card-hover" style="background:#0f0f1a;border:1px solid #1a1a2e;border-radius:1rem;padding:1.5rem 1.75rem;display:flex;flex-wrap:wrap;align-items:center;gap:1.5rem;">
            <div style="flex:1;min-width:0;">
              <div style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-bottom:0.75rem;">
                {post.tags.map(t => <span class="tag">{t}</span>)}
              </div>
              <h2 style="font-size:1.05rem;font-weight:700;color:#f8fafc;margin-bottom:0.5rem;line-height:1.4;">{post.title}</h2>
              <p style="font-size:0.875rem;color:#64748b;line-height:1.6;">{post.excerpt}</p>
            </div>
            <div style="display:flex;flex-direction:column;align-items:flex-end;gap:0.5rem;flex-shrink:0;">
              <span style="font-size:0.75rem;color:#475569;">{post.date}</span>
              <span style="font-size:0.75rem;color:#475569;">{post.readTime}</span>
              <span style="font-size:0.7rem;font-weight:700;padding:0.2rem 0.6rem;border-radius:9999px;background:rgba(251,191,36,0.1);color:#fbbf24;border:1px solid rgba(251,191,36,0.25);">Coming Soon</span>
            </div>
          </article>
        ))}
      </div>

    </div>
  </section>

</BaseLayout>
""")

# ═══════════════════════════════════════════════════════════
# contact.astro
# ═══════════════════════════════════════════════════════════
w('pages/contact.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const contacts = [
  {
    label: 'Email',
    value: 'siblaghari@gmail.com',
    href: 'mailto:siblaghari@gmail.com',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>`,
    desc: 'Best way to reach me',
  },
  {
    label: 'GitHub',
    value: 'github.com/sibghatullah-laghari',
    href: 'https://github.com/sibghatullah-laghari',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>`,
    desc: 'Check out my code',
  },
  {
    label: 'LinkedIn',
    value: 'linkedin.com/in/sibghatullah-laghari',
    href: 'https://linkedin.com/in/sibghatullah-laghari',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>`,
    desc: 'Connect with me',
  },
];
---
<BaseLayout title="Contact | Sibghatullah Laghari">

  <section style="padding:5rem 1.5rem;min-height:80vh;display:flex;align-items:flex-start;justify-content:center;background:radial-gradient(ellipse at 50% 0%, rgba(79,70,229,0.08) 0%, transparent 60%),#0a0a0f;">
    <div class="container" style="max-width:52rem;">
      <div style="text-align:center;margin-bottom:3.5rem;">
        <p style="font-size:0.75rem;font-weight:700;letter-spacing:0.1em;color:#4f46e5;text-transform:uppercase;margin-bottom:0.75rem;">GET IN TOUCH</p>
        <h1 style="font-size:2.5rem;font-weight:800;color:#f8fafc;margin-bottom:1rem;">Contact</h1>
        <p style="color:#64748b;font-size:1rem;line-height:1.7;max-width:32rem;margin:0 auto;">
          Open to freelance opportunities, collaborations, and interesting backend engineering conversations. Feel free to reach out!
        </p>
      </div>

      <!-- Contact Cards -->
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.25rem;margin-bottom:2.5rem;">
        {contacts.map(c => (
          <a href={c.href} target={c.href.startsWith('http') ? '_blank' : '_self'} rel="noopener"
             class="card-hover" style="background:#0f0f1a;border:1px solid #1a1a2e;border-radius:1rem;padding:1.5rem;display:flex;flex-direction:column;gap:0.75rem;text-decoration:none;color:inherit;">
            <div style="color:#4f46e5;" set:html={c.icon}></div>
            <div>
              <p style="font-size:0.75rem;font-weight:600;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.2rem;">{c.label}</p>
              <p style="font-size:0.9rem;font-weight:600;color:#f8fafc;word-break:break-all;">{c.value}</p>
              <p style="font-size:0.8rem;color:#475569;margin-top:0.2rem;">{c.desc}</p>
            </div>
          </a>
        ))}
      </div>

      <!-- Availability Card -->
      <div style="background:#0f0f1a;border:1px solid rgba(74,222,128,0.2);border-radius:1rem;padding:1.75rem;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;">
        <div>
          <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;">
            <span style="width:8px;height:8px;border-radius:50%;background:#4ade80;display:inline-block;animation:pulse 2s infinite;"></span>
            <span style="font-size:0.8rem;font-weight:700;color:#4ade80;text-transform:uppercase;letter-spacing:0.05em;">Available</span>
          </div>
          <h3 style="font-size:1.1rem;font-weight:700;color:#f8fafc;">Open to Opportunities</h3>
          <p style="font-size:0.875rem;color:#64748b;margin-top:0.25rem;">Looking for backend developer roles, internships, or freelance projects.</p>
        </div>
        <a href="mailto:siblaghari@gmail.com" class="btn-primary">Send Email</a>
      </div>

    </div>
  </section>
  <style>
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }
  </style>
</BaseLayout>
""")

print("\\nAll files written successfully!")
