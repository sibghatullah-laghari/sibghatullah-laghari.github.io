import os

BASE = r'c:\Users\sibla\Downloads\sibghatullah-laghari.github.io\src'

def write(rel, content):
    path = os.path.join(BASE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('✓', rel)

# ─────────────────────────────────────────────────────────
# BASE LAYOUT
# ─────────────────────────────────────────────────────────
write('layouts/BaseLayout.astro', """\
---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';

export interface Props {
  title?: string;
  description?: string;
}

const {
  title = 'Sibghatullah Laghari — Java Backend Developer',
  description = 'Java Spring Boot Backend Developer specializing in REST APIs, JWT authentication, and scalable backend systems.',
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
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
  <style is:global>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg:       #06080f;
      --bg2:      #0b0d1a;
      --bg3:      #0f1120;
      --card:     #0f1120;
      --card2:    #131527;
      --border:   rgba(255,255,255,0.07);
      --borderH:  rgba(99,102,241,0.45);
      --accent:   #6366f1;
      --accent2:  #818cf8;
      --glow:     rgba(99,102,241,0.2);
      --txt:      #f0f4ff;
      --txt2:     #8892a4;
      --txt3:     #3d4559;
      --green:    #22c55e;
      --T:        all 0.22s cubic-bezier(0.4,0,0.2,1);
    }
    html  { font-family:'Inter',system-ui,-apple-system,sans-serif; -webkit-font-smoothing:antialiased; }
    body  { background:var(--bg); color:var(--txt); overflow-x:hidden; }
    ::selection { background:var(--accent); color:#fff; }
    ::-webkit-scrollbar { width:5px; }
    ::-webkit-scrollbar-track { background:var(--bg); }
    ::-webkit-scrollbar-thumb { background:var(--accent); border-radius:9px; }
    h1,h2,h3,h4 { font-weight:800; line-height:1.15; color:var(--txt); }
    p { line-height:1.75; }
    a { text-decoration:none; }

    /* ─ Gradient text ─────────────────────────── */
    .gt  { background:linear-gradient(135deg,#818cf8,#a78bfa,#c084fc); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
    .gt2 { background:linear-gradient(90deg,#6366f1,#8b5cf6); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }

    /* ─ Buttons ───────────────────────────────── */
    .btn { display:inline-flex; align-items:center; gap:.45rem; padding:.7rem 1.6rem; border-radius:.5rem; font-weight:600; font-size:.875rem; font-family:inherit; transition:var(--T); cursor:pointer; border:none; letter-spacing:.01em; }
    .btn-primary { background:var(--accent); color:#fff; }
    .btn-primary:hover { background:#4f46e5; transform:translateY(-2px); box-shadow:0 12px 30px var(--glow); }
    .btn-outline { background:transparent; color:var(--txt2); border:1.5px solid var(--border); }
    .btn-outline:hover { border-color:var(--accent); color:var(--txt); transform:translateY(-2px); }
    .btn-sm { padding:.45rem 1rem; font-size:.78rem; border-radius:.4rem; }

    /* ─ Cards ─────────────────────────────────── */
    .card { background:var(--card); border:1px solid var(--border); border-radius:1rem; padding:1.75rem; transition:var(--T); }
    .card:hover { border-color:var(--borderH); box-shadow:0 24px 60px rgba(0,0,0,.45),0 0 0 1px rgba(99,102,241,.08); transform:translateY(-4px); }

    /* ─ Badges ────────────────────────────────── */
    .badge { display:inline-flex; align-items:center; gap:.35rem; padding:.22rem .7rem; border-radius:9999px; font-size:.7rem; font-weight:700; letter-spacing:.04em; }
    .badge-indigo  { background:rgba(99,102,241,.12); color:var(--accent2); border:1px solid rgba(99,102,241,.22); }
    .badge-green   { background:rgba(34,197,94,.1);   color:#4ade80;       border:1px solid rgba(34,197,94,.22); }
    .badge-yellow  { background:rgba(251,191,36,.1);  color:#fbbf24;       border:1px solid rgba(251,191,36,.2); }
    .badge-neutral { background:rgba(255,255,255,.06); color:var(--txt2);  border:1px solid var(--border); }

    /* ─ Skill chips ───────────────────────────── */
    .chip { display:inline-flex; align-items:center; gap:.45rem; padding:.5rem 1.05rem; background:var(--card); border:1px solid var(--border); border-radius:.5rem; font-size:.82rem; font-weight:500; color:var(--txt2); transition:var(--T); cursor:default; }
    .chip:hover { border-color:var(--accent); color:var(--txt); box-shadow:0 0 14px var(--glow); transform:translateY(-2px); }
    .chip-dot { width:7px; height:7px; border-radius:50%; flex-shrink:0; }

    /* ─ Layout ────────────────────────────────── */
    .sec { padding:5.5rem 1.5rem; }
    .sec-alt { background:var(--bg2); }
    .wrap { max-width:78rem; margin:0 auto; width:100%; }
    .divider { height:1px; background:linear-gradient(90deg,transparent,var(--border),transparent); border:none; }

    /* ─ Section headings ──────────────────────── */
    .s-eyebrow { display:block; font-size:.7rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--accent); margin-bottom:.65rem; }
    .s-title   { font-size:2.25rem; font-weight:800; line-height:1.15; }
    .s-desc    { color:var(--txt2); font-size:.95rem; margin-top:.5rem; max-width:38rem; line-height:1.75; }

    /* ─ Terminal ──────────────────────────────── */
    .terminal { background:#0c0e18; border:1px solid rgba(255,255,255,.09); border-radius:.875rem; overflow:hidden; box-shadow:0 30px 60px rgba(0,0,0,.55),0 0 0 1px rgba(99,102,241,.1); }
    .tbar { background:#12141f; padding:.65rem 1rem; display:flex; align-items:center; gap:.4rem; border-bottom:1px solid rgba(255,255,255,.06); }
    .dr { width:12px; height:12px; border-radius:50%; background:#ff5f57; flex-shrink:0; }
    .dy { width:12px; height:12px; border-radius:50%; background:#febc2e; flex-shrink:0; }
    .dg { width:12px; height:12px; border-radius:50%; background:#28c840; flex-shrink:0; }
    .tname { margin-left:.5rem; font-size:.7rem; font-family:'JetBrains Mono',monospace; color:rgba(255,255,255,.25); }
    .tbody { padding:1.4rem 1.6rem; font-family:'JetBrains Mono',monospace; font-size:.8rem; line-height:2; }
    .tl { display:flex; gap:.35rem; white-space:nowrap; }
    .c1 { color:#3e4a5e; }
    .c2 { color:#7c8cf8; }
    .c3 { color:#a5d6ff; }
    .c4 { color:#79c0ff; }
    .c5 { color:#d2a8ff; }
    .c6 { color:#56d364; }
    .c7 { color:#ffa657; }
    .c8 { color:#2d3748; }
    .cursor { display:inline-block; width:2px; height:.9em; background:var(--accent2); vertical-align:middle; animation:blink 1s step-end infinite; }

    /* ─ Timeline ──────────────────────────────── */
    .tl-line { position:absolute; left:1.125rem; top:1.5rem; bottom:-1.5rem; width:2px; background:linear-gradient(to bottom,var(--accent),rgba(99,102,241,.05)); border-radius:2px; }
    .tl-dot  { position:absolute; left:0; top:1.5rem; width:2.25rem; height:2.25rem; border-radius:50%; background:var(--accent); border:3px solid var(--bg); box-shadow:0 0 0 2px rgba(99,102,241,.4); display:flex; align-items:center; justify-content:center; flex-shrink:0; }

    /* ─ Animations ────────────────────────────── */
    @keyframes blink    { 0%,100%{opacity:1} 50%{opacity:0} }
    @keyframes float    { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }
    @keyframes fadein   { from{opacity:0;transform:translateY(16px)} to{opacity:1;transform:translateY(0)} }
    @keyframes pulsedot { 0%,100%{transform:scale(1);opacity:1} 50%{transform:scale(1.4);opacity:.5} }
    .animate-float { animation:float 5s ease-in-out infinite; }
    .animate-in    { animation:fadein .5s ease forwards; }
    .pulse-dot     { animation:pulsedot 2.2s ease-in-out infinite; }

    /* ─ Responsive ────────────────────────────── */
    @media(max-width:768px) {
      .sec { padding:4rem 1.25rem; }
      .s-title { font-size:1.875rem; }
      .hide-mobile { display:none !important; }
    }
  </style>
</head>
<body>
  <Navbar />
  <main><slot /></main>
  <Footer />
</body>
</html>
""")

# ─────────────────────────────────────────────────────────
# NAVBAR
# ─────────────────────────────────────────────────────────
write('components/Navbar.astro', """\
---
const links = [
  { href: '/',           label: 'Home'        },
  { href: '/experience', label: 'Experience'  },
  { href: '/working',    label: 'What I Do'   },
  { href: '/projects',   label: 'Projects'    },
  { href: '/blog',       label: 'Blog'        },
  { href: '/contact',    label: 'Contact'     },
];
const p = Astro.url.pathname;
const active = (h: string) => h === '/' ? p === '/' : p.startsWith(h);
---
<header id="nav" style="position:sticky;top:0;z-index:50;background:rgba(6,8,15,0.82);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,0.06);transition:box-shadow .3s;">
  <div class="wrap" style="display:flex;align-items:center;justify-content:space-between;padding:.9rem 1.5rem;">

    <!-- Logo -->
    <a href="/" style="display:flex;align-items:center;gap:.65rem;text-decoration:none;" aria-label="Home">
      <div style="width:2.1rem;height:2.1rem;border-radius:.5rem;background:linear-gradient(135deg,#6366f1,#8b5cf6);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:.75rem;color:#fff;flex-shrink:0;letter-spacing:.04em;">SL</div>
      <span style="font-weight:700;font-size:1rem;color:#f0f4ff;letter-spacing:-.01em;">Sibghatullah <span style="color:rgba(255,255,255,.3);font-weight:400;">/</span> Backend Dev</span>
    </a>

    <!-- Desktop links -->
    <nav style="display:flex;align-items:center;gap:.2rem;" class="desk-nav" aria-label="Main navigation">
      {links.map(l => (
        <a href={l.href}
           style={`padding:.4rem .85rem;border-radius:.4rem;font-size:.875rem;font-weight:500;transition:all .2s;text-decoration:none;${
             active(l.href)
               ? 'background:rgba(99,102,241,.18);color:#818cf8;'
               : 'color:#8892a4;'
           }`}
           onmouseover={`if(!this.style.background.includes('99,102,241,.18')){this.style.background='rgba(255,255,255,.05)';this.style.color='#f0f4ff';}`}
           onmouseout={`if(!this.style.background.includes('99,102,241,.18')){this.style.background='';this.style.color='#8892a4';}`}
        >{l.label}</a>
      ))}
      <a href="/contact"
         style="margin-left:.5rem;padding:.4rem 1rem;border-radius:.4rem;background:rgba(99,102,241,.15);color:#818cf8;font-size:.8rem;font-weight:700;border:1px solid rgba(99,102,241,.25);transition:all .2s;display:flex;align-items:center;gap:.35rem;text-decoration:none;"
         onmouseover="this.style.background='rgba(99,102,241,.28)';this.style.borderColor='rgba(99,102,241,.5)';"
         onmouseout="this.style.background='rgba(99,102,241,.15)';this.style.borderColor='rgba(99,102,241,.25)';">
        <span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;" class="pulse-dot"></span>
        Available
      </a>
    </nav>

    <!-- Mobile burger -->
    <button id="burger" aria-label="Menu" style="display:none;background:none;border:1px solid rgba(255,255,255,.1);border-radius:.4rem;cursor:pointer;padding:.4rem;color:#8892a4;line-height:0;" class="mob-btn">
      <svg id="ico-open" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      <svg id="ico-close" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:none;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
    </button>
  </div>

  <!-- Mobile menu -->
  <div id="mob-menu" style="display:none;border-top:1px solid rgba(255,255,255,.06);padding:.75rem 1.5rem 1.25rem;">
    <nav style="display:flex;flex-direction:column;gap:.2rem;">
      {links.map(l => (
        <a href={l.href} style={`padding:.65rem 1rem;border-radius:.5rem;font-size:.9rem;font-weight:500;transition:all .2s;text-decoration:none;${
          active(l.href) ? 'background:rgba(99,102,241,.15);color:#818cf8;' : 'color:#8892a4;'
        }`}>{l.label}</a>
      ))}
    </nav>
  </div>
</header>

<style>
  @media(min-width:769px) { .mob-btn { display:none !important; } }
  @media(max-width:768px) {
    .desk-nav { display:none !important; }
    .mob-btn   { display:block !important; }
  }
</style>
<script>
  const burger = document.getElementById('burger');
  const mob    = document.getElementById('mob-menu');
  const iopen  = document.getElementById('ico-open');
  const iclose = document.getElementById('ico-close');
  burger?.addEventListener('click', () => {
    const open = mob?.style.display === 'block';
    if (mob)   mob.style.display   = open ? 'none' : 'block';
    if (iopen) iopen.style.display = open ? 'block' : 'none';
    if (iclose) iclose.style.display = open ? 'none' : 'block';
  });
  // Scroll shadow
  window.addEventListener('scroll', () => {
    const nav = document.getElementById('nav');
    if (nav) nav.style.boxShadow = window.scrollY > 20 ? '0 4px 30px rgba(0,0,0,.5)' : 'none';
  });
</script>
""")

# ─────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────
write('components/Footer.astro', """\
<footer style="background:#06080f;border-top:1px solid rgba(255,255,255,0.06);">
  <div class="wrap" style="padding:3rem 1.5rem;">
    <div style="display:grid;grid-template-columns:1fr auto;align-items:center;gap:2rem;flex-wrap:wrap;">

      <div>
        <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem;">
          <div style="width:1.8rem;height:1.8rem;border-radius:.4rem;background:linear-gradient(135deg,#6366f1,#8b5cf6);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:.65rem;color:#fff;">SL</div>
          <span style="font-weight:700;color:#f0f4ff;font-size:.95rem;">Sibghatullah Laghari</span>
        </div>
        <p style="font-size:.82rem;color:#3d4559;max-width:28rem;line-height:1.6;">Java Spring Boot Backend Developer &mdash; building secure, scalable backend systems.</p>
      </div>

      <div style="display:flex;align-items:center;gap:1rem;">
        <a href="https://github.com/sibghatullah-laghari" target="_blank" rel="noopener" aria-label="GitHub"
           style="color:#3d4559;transition:color .2s;" onmouseover="this.style.color='#f0f4ff'" onmouseout="this.style.color='#3d4559'">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
        </a>
        <a href="https://linkedin.com/in/sibghatullah-laghari" target="_blank" rel="noopener" aria-label="LinkedIn"
           style="color:#3d4559;transition:color .2s;" onmouseover="this.style.color='#f0f4ff'" onmouseout="this.style.color='#3d4559'">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        </a>
        <a href="mailto:siblaghari@gmail.com" aria-label="Email"
           style="color:#3d4559;transition:color .2s;" onmouseover="this.style.color='#f0f4ff'" onmouseout="this.style.color='#3d4559'">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
        </a>
      </div>
    </div>

    <hr class="divider" style="margin:2rem 0;" />
    <p style="text-align:center;font-size:.75rem;color:#242a36;">&copy; 2026 Sibghatullah Laghari &middot; Built with Astro &amp; Tailwind &middot; Hosted on GitHub Pages</p>
  </div>
</footer>
""")

# ─────────────────────────────────────────────────────────
# HOME / INDEX
# ─────────────────────────────────────────────────────────
write('pages/index.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const skills = [
  { label:'Java',             color:'#f89820' },
  { label:'Spring Boot',      color:'#6db33f' },
  { label:'Spring Security',  color:'#6db33f' },
  { label:'REST APIs',        color:'#818cf8' },
  { label:'JWT Auth',         color:'#a78bfa' },
  { label:'MySQL',            color:'#00758f' },
  { label:'Oracle DB',        color:'#c74634' },
  { label:'JPA / Hibernate',  color:'#59666c' },
  { label:'Git & GitHub',     color:'#f05032' },
  { label:'Maven',            color:'#c71a36' },
  { label:'Postman',          color:'#ff6c37' },
  { label:'Linux CLI',        color:'#fcc624' },
];
---
<BaseLayout>

<!-- ── HERO ──────────────────────────────────────────── -->
<section class="sec" style="min-height:92vh;display:flex;align-items:center;padding-top:4rem;padding-bottom:4rem;background:radial-gradient(ellipse 80% 55% at 50% -10%,rgba(99,102,241,.16) 0%,transparent 65%),var(--bg);">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;" class="hero-grid">

      <!-- Left -->
      <div style="animation:fadein .6s ease forwards;">
        <!-- Badge -->
        <div style="display:flex;align-items:center;gap:.5rem;margin-bottom:1.75rem;">
          <span class="badge badge-green" style="font-size:.72rem;">
            <span class="pulse-dot" style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span>
            Open to work &mdash; Backend Developer
          </span>
        </div>

        <!-- Heading -->
        <h1 style="font-size:clamp(2.75rem,5.5vw,4.5rem);font-weight:900;line-height:1.08;letter-spacing:-.02em;margin-bottom:1.1rem;">
          Hi, I'm<br/>
          <span class="gt">Sibghatullah</span><br/>
          <span style="color:var(--txt);">Laghari.</span>
        </h1>

        <!-- Role line -->
        <p style="font-size:1.1rem;font-weight:600;color:var(--accent2);letter-spacing:.01em;margin-bottom:1.25rem;display:flex;align-items:center;gap:.5rem;">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:var(--accent);flex-shrink:0;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
          Java &middot; Spring Boot &middot; Backend Developer
        </p>

        <!-- Intro -->
        <p style="font-size:1rem;color:var(--txt2);line-height:1.8;margin-bottom:2rem;max-width:30rem;">
          I build production-ready backend systems &mdash; REST APIs, JWT authentication, role-based access control, and
          database-driven services. Currently pursuing BE Software Engineering at Mehran UET.
        </p>

        <!-- CTAs -->
        <div style="display:flex;flex-wrap:wrap;gap:.875rem;margin-bottom:2.75rem;">
          <a href="/projects" class="btn btn-primary">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
            View Projects
          </a>
          <a href="/contact" class="btn btn-outline">
            Get In Touch
          </a>
          <a href="https://github.com/sibghatullah-laghari" target="_blank" rel="noopener" class="btn btn-outline">
            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
            GitHub
          </a>
        </div>

        <!-- Stats -->
        <div style="display:flex;align-items:center;gap:2rem;padding:1.25rem 1.5rem;background:var(--card2);border:1px solid var(--border);border-radius:.75rem;">
          <div style="text-align:center;">
            <div style="font-size:1.6rem;font-weight:900;" class="gt2">1+</div>
            <div style="font-size:.75rem;color:var(--txt3);margin-top:.15rem;font-weight:500;">Yr Experience</div>
          </div>
          <div style="width:1px;height:2.5rem;background:var(--border);"></div>
          <div style="text-align:center;">
            <div style="font-size:1.6rem;font-weight:900;" class="gt2">5+</div>
            <div style="font-size:.75rem;color:var(--txt3);margin-top:.15rem;font-weight:500;">Projects</div>
          </div>
          <div style="width:1px;height:2.5rem;background:var(--border);"></div>
          <div style="text-align:center;">
            <div style="font-size:1.6rem;font-weight:900;" class="gt2">10+</div>
            <div style="font-size:.75rem;color:var(--txt3);margin-top:.15rem;font-weight:500;">APIs Built</div>
          </div>
          <div style="width:1px;height:2.5rem;background:var(--border);"></div>
          <div style="text-align:center;">
            <div style="font-size:1.6rem;font-weight:900;" class="gt2">BSE</div>
            <div style="font-size:.75rem;color:var(--txt3);margin-top:.15rem;font-weight:500;">Mehran UET</div>
          </div>
        </div>
      </div>

      <!-- Right: Terminal -->
      <div class="animate-float hide-mobile" style="animation-delay:.2s;">
        <div class="terminal">
          <div class="tbar">
            <div class="dr"></div><div class="dy"></div><div class="dg"></div>
            <span class="tname">Developer.java</span>
          </div>
          <div class="tbody">
            <div class="tl"><span class="c1">// ─ Backend Developer Profile</span></div>
            <div class="tl">&nbsp;</div>
            <div class="tl"><span class="c2">public class</span>&nbsp;<span class="c5">Developer</span>&nbsp;<span style="color:#8892a4;">&#123;</span></div>
            <div class="tl">&nbsp;</div>
            <div class="tl">&nbsp;&nbsp;<span class="c2">String</span>&nbsp;<span class="c4">name</span>&nbsp;&nbsp;&nbsp;= <span class="c3">"Sibghatullah Laghari"</span>;</div>
            <div class="tl">&nbsp;&nbsp;<span class="c2">String</span>&nbsp;<span class="c4">role</span>&nbsp;&nbsp;&nbsp;= <span class="c3">"Backend Developer"</span>;</div>
            <div class="tl">&nbsp;&nbsp;<span class="c2">String</span>&nbsp;<span class="c4">status</span>&nbsp;= <span class="c6">"Available"</span>;</div>
            <div class="tl">&nbsp;&nbsp;<span class="c2">String</span>&nbsp;<span class="c4">uni</span>&nbsp;&nbsp;&nbsp;= <span class="c3">"Mehran UET"</span>;</div>
            <div class="tl">&nbsp;</div>
            <div class="tl">&nbsp;&nbsp;<span class="c2">String[]</span>&nbsp;<span class="c4">stack</span>&nbsp;= <span style="color:#8892a4;">&#123;</span></div>
            <div class="tl">&nbsp;&nbsp;&nbsp;&nbsp;<span class="c3">"Spring Boot"</span>, <span class="c3">"JWT Auth"</span>,</div>
            <div class="tl">&nbsp;&nbsp;&nbsp;&nbsp;<span class="c3">"REST APIs"</span>,&nbsp;&nbsp;<span class="c3">"MySQL"</span>,</div>
            <div class="tl">&nbsp;&nbsp;&nbsp;&nbsp;<span class="c3">"Spring Security"</span></div>
            <div class="tl">&nbsp;&nbsp;<span style="color:#8892a4;">&#125;</span>;</div>
            <div class="tl">&nbsp;</div>
            <div class="tl"><span style="color:#8892a4;">&#125;</span></div>
            <div class="tl">&nbsp;</div>
            <div class="tl"><span class="c1">$</span>&nbsp;<span class="c6">./run-api</span>&nbsp;<span class="c7">--port</span>=<span class="c3">8080</span>&nbsp;<span class="cursor"></span></div>
          </div>
        </div>
        <!-- Glow beneath terminal -->
        <div style="height:1px;background:radial-gradient(ellipse 80% 1px at 50% 0,rgba(99,102,241,.4),transparent);margin-top:1px;"></div>
      </div>
    </div>
  </div>

  <style>
    @media(max-width:900px) {
      .hero-grid { grid-template-columns: 1fr !important; }
    }
  </style>
</section>

<hr class="divider" />

<!-- ── SKILLS ──────────────────────────────────────────── -->
<section class="sec sec-alt">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 2fr;gap:3.5rem;align-items:start;" class="skills-grid">
      <div>
        <span class="s-eyebrow">Tech Stack</span>
        <h2 class="s-title">Technologies<br/>I Work With</h2>
        <p class="s-desc">Backend-focused. Production-tested. Always learning.</p>
        <a href="/working" class="btn btn-outline" style="margin-top:1.75rem;font-size:.82rem;">
          See What I Build
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </a>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:.6rem;align-content:flex-start;">
        {skills.map(s => (
          <span class="chip">
            <span class="chip-dot" style={`background:${s.color};`}></span>
            {s.label}
          </span>
        ))}
      </div>
    </div>
  </div>
  <style>
    @media(max-width:768px) { .skills-grid { grid-template-columns:1fr !important; } }
  </style>
</section>

<hr class="divider" />

<!-- ── ABOUT STRIP ────────────────────────────────────── -->
<section class="sec" style="padding:4rem 1.5rem;">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5rem;" class="about-grid">

      <div class="card" style="border-color:rgba(99,102,241,.2);">
        <div style="font-size:1.5rem;margin-bottom:.75rem;">&#127979;</div>
        <h3 style="font-size:1rem;font-weight:700;margin-bottom:.5rem;">Education</h3>
        <p style="font-size:.875rem;color:var(--txt2);line-height:1.7;">BE Software Engineering<br/>
          <span style="color:var(--accent2);font-weight:600;">Mehran UET</span><br/>
          <span style="font-size:.8rem;color:var(--txt3);">2024 &mdash; Present &middot; Sindh, Pakistan</span>
        </p>
      </div>

      <div class="card" style="border-color:rgba(99,102,241,.2);">
        <div style="font-size:1.5rem;margin-bottom:.75rem;">&#128188;</div>
        <h3 style="font-size:1rem;font-weight:700;margin-bottom:.5rem;">Experience</h3>
        <p style="font-size:.875rem;color:var(--txt2);line-height:1.7;">Self-Employed Backend Developer<br/>
          <span style="color:var(--accent2);font-weight:600;">Java &middot; Spring Boot</span><br/>
          <span style="font-size:.8rem;color:var(--txt3);">Aug 2024 &mdash; Present</span>
        </p>
      </div>

      <div class="card" style="border-color:rgba(99,102,241,.2);">
        <div style="font-size:1.5rem;margin-bottom:.75rem;">&#127759;</div>
        <h3 style="font-size:1rem;font-weight:700;margin-bottom:.5rem;">Location</h3>
        <p style="font-size:.875rem;color:var(--txt2);line-height:1.7;">Sindh, Pakistan<br/>
          <span style="color:var(--accent2);font-weight:600;">Remote / Hybrid Ready</span><br/>
          <span style="font-size:.8rem;color:var(--txt3);">Open to relocation</span>
        </p>
      </div>

    </div>
  </div>
  <style>
    @media(max-width:768px) { .about-grid { grid-template-columns:1fr !important; } }
  </style>
</section>

</BaseLayout>
""")

# ─────────────────────────────────────────────────────────
# EXPERIENCE
# ─────────────────────────────────────────────────────────
write('pages/experience.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Experience — Sibghatullah Laghari">

<section class="sec" style="background:radial-gradient(ellipse 60% 40% at 20% 0,rgba(99,102,241,.1) 0%,transparent 60%),var(--bg);">
  <div class="wrap">

    <!-- Header -->
    <div style="max-width:38rem;margin-bottom:4rem;">
      <span class="s-eyebrow">Background</span>
      <h1 class="s-title">Experience &amp; Education</h1>
      <p class="s-desc">My journey into backend engineering &mdash; from the classroom to real-world systems.</p>
    </div>

    <!-- Timeline -->
    <div style="display:flex;flex-direction:column;gap:0;">

      <!-- Item 1 -->
      <div style="display:flex;gap:2rem;position:relative;padding-bottom:3rem;" class="tl-item">
        <div style="position:relative;flex-shrink:0;width:2.25rem;">
          <div class="tl-dot">
            <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" fill="none" viewBox="0 0 24 24" stroke="#fff"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
          </div>
          <div class="tl-line"></div>
        </div>
        <div class="card" style="flex:1;margin-top:0;">
          <div style="display:flex;flex-wrap:wrap;align-items:flex-start;justify-content:space-between;gap:1rem;margin-bottom:1.25rem;">
            <div>
              <h3 style="font-size:1.15rem;font-weight:800;margin-bottom:.3rem;">Java Spring Boot Backend Developer</h3>
              <p style="font-size:.9rem;color:var(--accent2);font-weight:600;">Self-Employed &middot; Freelance</p>
            </div>
            <div style="text-align:right;flex-shrink:0;">
              <span class="badge badge-indigo" style="font-size:.72rem;">Aug 2024 &mdash; Present</span>
              <p style="font-size:.75rem;color:var(--txt3);margin-top:.4rem;">Sindh, Pakistan &middot; Remote</p>
            </div>
          </div>
          <p style="font-size:.9rem;color:var(--txt2);margin-bottom:1.25rem;line-height:1.8;">
            Designing and developing production-grade backend applications using Java and Spring Boot.
            Focus on REST API design, authentication systems, and scalable layered architecture.
          </p>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:.5rem;margin-bottom:1.5rem;">
            {[
              'Designed and built RESTful APIs with proper resource modeling, status codes, and versioning',
              'Implemented JWT-based authentication with stateless token management and refresh logic',
              'Built role-based access control (RBAC) using Spring Security — USER, ADMIN, MODERATOR roles',
              'Designed normalized MySQL/Oracle database schemas with full JPA/Hibernate integration',
              'Developed layered backend architecture: Controller → Service → Repository pattern',
              'Used Maven for dependency management and Postman for API testing and documentation',
              'Managed all projects via Git with feature branching and structured commit history',
            ].map(item => (
              <li style="display:flex;align-items:flex-start;gap:.6rem;font-size:.875rem;color:var(--txt2);">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:var(--accent);flex-shrink:0;margin-top:.2rem;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                {item}
              </li>
            ))}
          </ul>
          <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
            {['Java','Spring Boot','Spring Security','JWT','REST APIs','MySQL','Oracle','JPA/Hibernate','Maven','Git','Postman'].map(t => (
              <span class="badge badge-indigo">{t}</span>
            ))}
          </div>
        </div>
      </div>

      <!-- Item 2 -->
      <div style="display:flex;gap:2rem;position:relative;padding-bottom:3rem;" class="tl-item">
        <div style="position:relative;flex-shrink:0;width:2.25rem;">
          <div class="tl-dot" style="background:linear-gradient(135deg,#8b5cf6,#7c3aed);">
            <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" fill="none" viewBox="0 0 24 24" stroke="#fff"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
          </div>
          <div class="tl-line" style="background:linear-gradient(to bottom,#8b5cf6,rgba(99,102,241,.05));"></div>
        </div>
        <div class="card" style="flex:1;">
          <div style="display:flex;flex-wrap:wrap;align-items:flex-start;justify-content:space-between;gap:1rem;margin-bottom:1.25rem;">
            <div>
              <h3 style="font-size:1.15rem;font-weight:800;margin-bottom:.3rem;">BE Software Engineering</h3>
              <p style="font-size:.9rem;color:var(--accent2);font-weight:600;">Mehran University of Engineering &amp; Technology</p>
            </div>
            <div style="text-align:right;flex-shrink:0;">
              <span class="badge badge-indigo" style="font-size:.72rem;">2024 &mdash; Present</span>
              <p style="font-size:.75rem;color:var(--txt3);margin-top:.4rem;">Sindh, Pakistan</p>
            </div>
          </div>
          <p style="font-size:.9rem;color:var(--txt2);margin-bottom:1.25rem;line-height:1.8;">
            Bachelor of Engineering in Software Engineering. Studying core computer science and engineering fundamentals
            while applying them to real-world backend projects.
          </p>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:.5rem;margin-bottom:1.5rem;">
            {[
              'Data Structures & Algorithms — practical implementation in Java',
              'Database Management Systems — relational design, SQL, normalization',
              'Object-Oriented Programming — design patterns, SOLID principles',
              'Computer Networks & Operating Systems fundamentals',
              'Software Engineering practices: SDLC, Agile, version control',
              'Team-based software projects using Git collaboration workflows',
            ].map(item => (
              <li style="display:flex;align-items:flex-start;gap:.6rem;font-size:.875rem;color:var(--txt2);">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:#8b5cf6;flex-shrink:0;margin-top:.2rem;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                {item}
              </li>
            ))}
          </ul>
          <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
            {['Java','OOP','DSA','SQL','Git','Software Engineering','Agile'].map(t => (
              <span class="badge badge-neutral">{t}</span>
            ))}
          </div>
        </div>
      </div>

    </div>

  </div>
</section>

</BaseLayout>
""")

# ─────────────────────────────────────────────────────────
# WORKING / WHAT I DO
# ─────────────────────────────────────────────────────────
write('pages/working.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const services = [
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>',
    title: 'REST API Development',
    desc:  'Design and build RESTful APIs with proper resource modeling, HTTP semantics, status codes, pagination, filtering, and versioning using Spring Boot.',
    tags:  ['Spring Boot','REST','JSON','Postman','Swagger'],
    color: '#6366f1',
  },
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>',
    title: 'Authentication & Security',
    desc:  'Implement JWT-based authentication, stateless token management, BCrypt password hashing, and Spring Security filter chains with custom configurations.',
    tags:  ['JWT','Spring Security','BCrypt','RBAC','OAuth2'],
    color: '#22c55e',
  },
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"/></svg>',
    title: 'Database Design & Integration',
    desc:  'Design normalized relational schemas, write optimized SQL queries, and integrate databases using Spring Data JPA and Hibernate ORM with MySQL and Oracle.',
    tags:  ['MySQL','Oracle','JPA','Hibernate','SQL'],
    color: '#00758f',
  },
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>',
    title: 'Layered Architecture',
    desc:  'Structure Spring Boot projects using Controller → Service → Repository layering with proper separation of concerns, DTOs, and clean, maintainable code.',
    tags:  ['MVC','DTO Pattern','Clean Code','SOLID','Design Patterns'],
    color: '#f89820',
  },
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
    title: 'API Testing & Documentation',
    desc:  'Thoroughly test endpoints with Postman collections and environments. Document APIs with clear request/response examples for frontend team integration.',
    tags:  ['Postman','API Docs','Unit Testing','Integration Testing'],
    color: '#ff6c37',
  },
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>',
    title: 'Version Control & Collaboration',
    desc:  'Work with Git and GitHub using feature branching, pull requests, and structured commit history to collaborate effectively in team-based development.',
    tags:  ['Git','GitHub','Branching','Pull Requests','Code Review'],
    color: '#f05032',
  },
];
---
<BaseLayout title="What I Do — Sibghatullah Laghari">

<section class="sec" style="background:radial-gradient(ellipse 70% 50% at 80% 0,rgba(99,102,241,.1) 0%,transparent 60%),var(--bg);">
  <div class="wrap">

    <!-- Header -->
    <div style="text-align:center;max-width:42rem;margin:0 auto 4rem;">
      <span class="s-eyebrow">Capabilities</span>
      <h1 class="s-title">What I Build</h1>
      <p class="s-desc" style="margin:0 auto;">Focused on backend engineering &mdash; the logic, security, and data layer that powers applications. Here's what I bring to a project.</p>
    </div>

    <!-- Services Grid -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem;">
      {services.map(s => (
        <div class="card" style="display:flex;flex-direction:column;gap:1rem;">
          <!-- Icon box -->
          <div style={`width:2.75rem;height:2.75rem;border-radius:.625rem;background:${s.color}18;border:1px solid ${s.color}30;display:flex;align-items:center;justify-content:center;color:${s.color};flex-shrink:0;`} set:html={s.icon}></div>
          <!-- Content -->
          <div>
            <h3 style="font-size:1rem;font-weight:700;margin-bottom:.45rem;">{s.title}</h3>
            <p style="font-size:.875rem;color:var(--txt2);line-height:1.75;">{s.desc}</p>
          </div>
          <!-- Tags -->
          <div style="display:flex;flex-wrap:wrap;gap:.35rem;margin-top:auto;">
            {s.tags.map(t => <span class="badge badge-indigo" style="font-size:.67rem;">{t}</span>)}
          </div>
        </div>
      ))}
    </div>

    <!-- Bottom CTA -->
    <div style="text-align:center;margin-top:4rem;padding:2.5rem;background:var(--card2);border:1px solid var(--border);border-radius:1rem;">
      <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:.75rem;">Ready to work on your backend?</h3>
      <p style="color:var(--txt2);font-size:.9rem;margin-bottom:1.5rem;max-width:32rem;margin-left:auto;margin-right:auto;">
        I'm available for freelance projects, internships, and full-time backend developer roles.
      </p>
      <a href="/contact" class="btn btn-primary">Get In Touch</a>
    </div>

  </div>
</section>

</BaseLayout>
""")

# ─────────────────────────────────────────────────────────
# PROJECTS
# ─────────────────────────────────────────────────────────
write('pages/projects.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const projects = [
  {
    title:    'CCTRS — Carbon Contribution & Reward Tracking System',
    desc:     'A backend system that tracks users\\' carbon-reducing activities, calculates contribution scores, and issues rewards. Features multi-role access and a fully documented REST API.',
    long:     'Built with a clean layered architecture: REST controllers, service layer with business logic, JPA repositories connected to MySQL. Full JWT authentication with USER and ADMIN roles. Includes contribution logging, reward calculation engine, and admin dashboard APIs.',
    tech:     ['Java','Spring Boot','Spring Security','JWT','MySQL','JPA/Hibernate','Maven','REST APIs'],
    github:   'https://github.com/sibghatullah-laghari',
    status:   'Completed',
    featured: True,
  },
  {
    title:    'User Management REST API',
    desc:     'A production-ready user management backend with registration, login, JWT authentication, profile management, and role-based endpoint protection.',
    long:     'Implements the full authentication lifecycle: registration with BCrypt hashing, JWT issuance on login, token-based authorization on protected routes. ADMIN can manage all users; USER can manage their own profile.',
    tech:     ['Spring Boot','Spring Security','JWT','BCrypt','MySQL','JPA','Maven'],
    github:   'https://github.com/sibghatullah-laghari',
    status:   'Completed',
    featured: False,
  },
  {
    title:    'Complaint & Case Tracking System',
    desc:     'A backend for managing citizen complaints and case workflows. Cases can be submitted, assigned, updated, and resolved through a structured REST API with role-based access.',
    long:     'Designed for multi-role workflows: citizens submit complaints, moderators process and assign them, admins oversee all. Features case status tracking, audit logs, and a relational database schema designed for query efficiency.',
    tech:     ['Spring Boot','Spring Security','MySQL','JPA','REST APIs','Maven'],
    github:   'https://github.com/sibghatullah-laghari',
    status:   'Completed',
    featured: False,
  },
  {
    title:    'Portfolio Website',
    desc:     'This portfolio — built with Astro (static site generator) and Tailwind CSS. Zero backend, zero CMS, deployed to GitHub Pages. Fast, accessible, responsive.',
    long:     'Component-based Astro architecture with global CSS design system. Deployed via GitHub Actions to GitHub Pages. Fully static — no JavaScript frameworks, just clean HTML + CSS.',
    tech:     ['Astro','Tailwind CSS','GitHub Pages','HTML5','CSS3'],
    github:   'https://github.com/sibghatullah-laghari/sibghatullah-laghari.github.io',
    status:   'Live',
    featured: False,
  },
];
---
<BaseLayout title="Projects — Sibghatullah Laghari">

<section class="sec">
  <div class="wrap">

    <!-- Header -->
    <div style="margin-bottom:3.5rem;">
      <span class="s-eyebrow">Portfolio</span>
      <h1 class="s-title">Projects</h1>
      <p class="s-desc">Backend systems I've designed, built, and deployed &mdash; from authentication engines to tracking platforms.</p>
    </div>

    <!-- Featured Project -->
    {projects.filter(p => p.featured).map(p => (
      <div class="card" style="margin-bottom:2rem;border-color:rgba(99,102,241,.3);background:linear-gradient(135deg,var(--card),var(--card2));position:relative;overflow:hidden;">
        <div style="position:absolute;top:0;right:0;width:300px;height:300px;background:radial-gradient(circle,rgba(99,102,241,.06) 0%,transparent 70%);pointer-events:none;"></div>
        <div style="display:flex;flex-wrap:wrap;align-items:flex-start;justify-content:space-between;gap:1rem;margin-bottom:1.25rem;">
          <div>
            <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem;">
              <span class="badge badge-green" style="font-size:.65rem;">Featured Project</span>
              <span class="badge badge-indigo" style="font-size:.65rem;">{p.status}</span>
            </div>
            <h2 style="font-size:1.3rem;font-weight:800;line-height:1.3;">{p.title}</h2>
          </div>
          <a href={p.github} target="_blank" rel="noopener" class="btn btn-outline btn-sm">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
            View on GitHub
          </a>
        </div>
        <p style="font-size:.9rem;color:var(--txt2);line-height:1.8;margin-bottom:.75rem;">{p.desc}</p>
        <p style="font-size:.875rem;color:var(--txt3);line-height:1.75;margin-bottom:1.5rem;">{p.long}</p>
        <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
          {p.tech.map(t => <span class="badge badge-indigo">{t}</span>)}
        </div>
      </div>
    ))}

    <!-- Other Projects Grid -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem;">
      {projects.filter(p => !p.featured).map(p => (
        <div class="card" style="display:flex;flex-direction:column;gap:.875rem;">
          <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:.75rem;">
            <div style="flex:1;">
              <div style="display:flex;align-items:center;gap:.5rem;margin-bottom:.5rem;">
                <span class={`badge ${p.status === 'Live' ? 'badge-green' : 'badge-indigo'}`} style="font-size:.65rem;">{p.status}</span>
              </div>
              <h3 style="font-size:.975rem;font-weight:700;line-height:1.4;">{p.title}</h3>
            </div>
            <a href={p.github} target="_blank" rel="noopener" aria-label="GitHub"
               style="color:var(--txt3);transition:color .2s;flex-shrink:0;margin-top:.25rem;"
               onmouseover="this.style.color='var(--accent2)'" onmouseout="this.style.color='var(--txt3)'">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
            </a>
          </div>
          <p style="font-size:.875rem;color:var(--txt2);line-height:1.75;flex:1;">{p.desc}</p>
          <div style="display:flex;flex-wrap:wrap;gap:.35rem;">
            {p.tech.map(t => <span class="badge badge-indigo" style="font-size:.65rem;">{t}</span>)}
          </div>
        </div>
      ))}
    </div>

    <!-- GitHub CTA -->
    <div style="text-align:center;margin-top:3rem;padding:2rem;border:1px dashed var(--border);border-radius:1rem;">
      <p style="color:var(--txt2);font-size:.9rem;margin-bottom:1rem;">More projects and code available on GitHub</p>
      <a href="https://github.com/sibghatullah-laghari" target="_blank" rel="noopener" class="btn btn-outline">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
        github.com/sibghatullah-laghari
      </a>
    </div>

  </div>
</section>

</BaseLayout>
""")

# ─────────────────────────────────────────────────────────
# BLOG
# ─────────────────────────────────────────────────────────
write('pages/blog.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';

const posts = [
  {
    title:    'How JWT Authentication Works in Spring Boot',
    excerpt:  'A practical walkthrough of stateless JWT auth — token generation on login, secret key signing, filter chain configuration in Spring Security, and protected route setup.',
    date:     'Mar 2026',
    readTime: '9 min read',
    tags:     ['Spring Boot','JWT','Spring Security'],
    category: 'Tutorial',
  },
  {
    title:    'Designing Clean REST APIs — Beyond the Basics',
    excerpt:  'Move past CRUD. Proper resource naming, HTTP semantics, idempotency, pagination, error response schemas, and versioning strategies for production APIs.',
    date:     'Feb 2026',
    readTime: '7 min read',
    tags:     ['REST API','API Design','Backend'],
    category: 'Guide',
  },
  {
    title:    'Spring Data JPA Deep Dive — Queries, Projections & Performance',
    excerpt:  'JPQL vs native queries, derived method names, projections for selective data fetching, and N+1 problem diagnosis and solutions with Hibernate.',
    date:     'Feb 2026',
    readTime: '11 min read',
    tags:     ['JPA','Hibernate','Spring Boot','MySQL'],
    category: 'Deep Dive',
  },
  {
    title:    'Role-Based Access Control in Spring Security',
    excerpt:  'Implementing RBAC with Spring Security from scratch — UserDetailsService, GrantedAuthority, method-level security with @PreAuthorize, and securing REST endpoints.',
    date:     'Jan 2026',
    readTime: '8 min read',
    tags:     ['Spring Security','RBAC','Authorization'],
    category: 'Tutorial',
  },
  {
    title:    'Database Schema Design for Backend Developers',
    excerpt:  'Normalization to 3NF, foreign key strategies, index design, and how your database schema decisions directly impact your JPA entity modeling and query performance.',
    date:     'Jan 2026',
    readTime: '10 min read',
    tags:     ['Database','MySQL','Schema Design'],
    category: 'Guide',
  },
];

const catColor: Record<string, string> = {
  'Tutorial':  'badge-indigo',
  'Guide':     'badge-green',
  'Deep Dive': 'badge-yellow',
};
---
<BaseLayout title="Blog — Sibghatullah Laghari">

<section class="sec">
  <div class="wrap">

    <!-- Header -->
    <div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:1.5rem;margin-bottom:3.5rem;">
      <div>
        <span class="s-eyebrow">Writing</span>
        <h1 class="s-title">Blog</h1>
        <p class="s-desc">Technical articles on Spring Boot, JWT, REST API design, and backend engineering.</p>
      </div>
      <span class="badge badge-yellow" style="font-size:.75rem;align-self:flex-end;">Publishing soon</span>
    </div>

    <!-- Info Banner -->
    <div style="display:flex;align-items:flex-start;gap:.875rem;padding:1.1rem 1.4rem;background:rgba(99,102,241,.07);border:1px solid rgba(99,102,241,.2);border-radius:.75rem;margin-bottom:2.5rem;">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:var(--accent2);flex-shrink:0;margin-top:.1rem;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
      <p style="font-size:.875rem;color:var(--txt2);line-height:1.6;">These are planned articles I'm writing based on real backend problems I've encountered. Publishing schedule: ~1 article every 2 weeks.</p>
    </div>

    <!-- Posts -->
    <div style="display:flex;flex-direction:column;gap:1.25rem;">
      {posts.map((post, i) => (
        <article class="card" style="display:flex;flex-wrap:wrap;align-items:stretch;gap:1.5rem;padding:1.5rem 1.75rem;">
          <!-- Left: number -->
          <div style="font-size:2.5rem;font-weight:900;color:var(--txt3);letter-spacing:-.04em;font-variant-numeric:tabular-nums;line-height:1;padding-top:.1rem;width:2.5rem;flex-shrink:0;font-family:'JetBrains Mono',monospace;">
            {String(i + 1).padStart(2, '0')}
          </div>
          <!-- Right: content -->
          <div style="flex:1;min-width:0;">
            <div style="display:flex;flex-wrap:wrap;align-items:center;gap:.5rem;margin-bottom:.75rem;">
              <span class={`badge ${catColor[post.category] || 'badge-neutral'}`} style="font-size:.65rem;">{post.category}</span>
              {post.tags.map(t => <span class="badge badge-neutral" style="font-size:.65rem;">{t}</span>)}
            </div>
            <h2 style="font-size:1rem;font-weight:700;margin-bottom:.5rem;line-height:1.4;">{post.title}</h2>
            <p style="font-size:.875rem;color:var(--txt2);line-height:1.7;margin-bottom:.75rem;">{post.excerpt}</p>
            <div style="display:flex;align-items:center;gap:1rem;font-size:.75rem;color:var(--txt3);">
              <span>{post.date}</span>
              <span>&middot;</span>
              <span>{post.readTime}</span>
              <span>&middot;</span>
              <span style="color:var(--accent2);font-weight:600;">Coming Soon</span>
            </div>
          </div>
        </article>
      ))}
    </div>

  </div>
</section>

</BaseLayout>
""")

# ─────────────────────────────────────────────────────────
# CONTACT
# ─────────────────────────────────────────────────────────
write('pages/contact.astro', """\
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Contact — Sibghatullah Laghari">

<section class="sec" style="min-height:88vh;display:flex;align-items:flex-start;background:radial-gradient(ellipse 70% 50% at 50% 0,rgba(99,102,241,.1) 0%,transparent 60%),var(--bg);">
  <div class="wrap">

    <!-- Header -->
    <div style="text-align:center;max-width:36rem;margin:0 auto 4rem;">
      <span class="s-eyebrow">Get In Touch</span>
      <h1 class="s-title">Contact</h1>
      <p class="s-desc" style="margin:0 auto;">
        Whether it's a backend project, a full-time role, or just a technical conversation &mdash; I'd love to hear from you.
      </p>
    </div>

    <!-- Main grid -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;align-items:start;" class="contact-grid">

      <!-- Left: Contact Cards -->
      <div style="display:flex;flex-direction:column;gap:1rem;">

        <a href="mailto:siblaghari@gmail.com"
           style="display:flex;align-items:center;gap:1.1rem;padding:1.4rem 1.6rem;background:var(--card);border:1px solid var(--border);border-radius:.875rem;transition:var(--T);text-decoration:none;color:inherit;"
           onmouseover="this.style.borderColor='rgba(99,102,241,.4)';this.style.transform='translateY(-3px)';this.style.boxShadow='0 16px 40px rgba(0,0,0,.4)'"
           onmouseout="this.style.borderColor='rgba(255,255,255,.07)';this.style.transform='';this.style.boxShadow=''">
          <div style="width:2.75rem;height:2.75rem;border-radius:.625rem;background:rgba(99,102,241,.12);border:1px solid rgba(99,102,241,.2);display:flex;align-items:center;justify-content:center;color:var(--accent);flex-shrink:0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
          </div>
          <div>
            <p style="font-size:.72rem;font-weight:700;color:var(--txt3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.2rem;">Email</p>
            <p style="font-size:.95rem;font-weight:600;color:var(--txt);">siblaghari@gmail.com</p>
            <p style="font-size:.78rem;color:var(--txt3);">Preferred contact method</p>
          </div>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="margin-left:auto;color:var(--txt3);flex-shrink:0;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </a>

        <a href="https://github.com/sibghatullah-laghari" target="_blank" rel="noopener"
           style="display:flex;align-items:center;gap:1.1rem;padding:1.4rem 1.6rem;background:var(--card);border:1px solid var(--border);border-radius:.875rem;transition:var(--T);text-decoration:none;color:inherit;"
           onmouseover="this.style.borderColor='rgba(99,102,241,.4)';this.style.transform='translateY(-3px)';this.style.boxShadow='0 16px 40px rgba(0,0,0,.4)'"
           onmouseout="this.style.borderColor='rgba(255,255,255,.07)';this.style.transform='';this.style.boxShadow=''">
          <div style="width:2.75rem;height:2.75rem;border-radius:.625rem;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;color:var(--txt2);flex-shrink:0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
          </div>
          <div>
            <p style="font-size:.72rem;font-weight:700;color:var(--txt3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.2rem;">GitHub</p>
            <p style="font-size:.95rem;font-weight:600;color:var(--txt);">github.com/sibghatullah-laghari</p>
            <p style="font-size:.78rem;color:var(--txt3);">Projects & open source</p>
          </div>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="margin-left:auto;color:var(--txt3);flex-shrink:0;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
        </a>

        <a href="https://linkedin.com/in/sibghatullah-laghari" target="_blank" rel="noopener"
           style="display:flex;align-items:center;gap:1.1rem;padding:1.4rem 1.6rem;background:var(--card);border:1px solid var(--border);border-radius:.875rem;transition:var(--T);text-decoration:none;color:inherit;"
           onmouseover="this.style.borderColor='rgba(99,102,241,.4)';this.style.transform='translateY(-3px)';this.style.boxShadow='0 16px 40px rgba(0,0,0,.4)'"
           onmouseout="this.style.borderColor='rgba(255,255,255,.07)';this.style.transform='';this.style.boxShadow=''">
          <div style="width:2.75rem;height:2.75rem;border-radius:.625rem;background:rgba(0,119,181,.12);border:1px solid rgba(0,119,181,.25);display:flex;align-items:center;justify-content:center;color:#0077b5;flex-shrink:0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          </div>
          <div>
            <p style="font-size:.72rem;font-weight:700;color:var(--txt3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.2rem;">LinkedIn</p>
            <p style="font-size:.95rem;font-weight:600;color:var(--txt);">linkedin.com/in/sibghatullah-laghari</p>
            <p style="font-size:.78rem;color:var(--txt3);">Connect professionally</p>
          </div>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="margin-left:auto;color:var(--txt3);flex-shrink:0;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
        </a>

      </div>

      <!-- Right: Availability + Quick profile -->
      <div style="display:flex;flex-direction:column;gap:1.25rem;">

        <!-- Availability Card -->
        <div style="padding:2rem;background:linear-gradient(135deg,rgba(34,197,94,.08),rgba(99,102,241,.08));border:1px solid rgba(34,197,94,.2);border-radius:1rem;">
          <div style="display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;">
            <span class="pulse-dot" style="width:8px;height:8px;border-radius:50%;background:#22c55e;display:inline-block;flex-shrink:0;"></span>
            <span style="font-size:.7rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#4ade80;">Currently Available</span>
          </div>
          <h3 style="font-size:1.2rem;font-weight:800;margin-bottom:.5rem;">Open to Opportunities</h3>
          <p style="font-size:.875rem;color:var(--txt2);line-height:1.7;margin-bottom:1.5rem;">
            Looking for backend developer internships, junior roles, or freelance projects.
            Available for remote work and hybrid arrangements.
          </p>
          <a href="mailto:siblaghari@gmail.com" class="btn btn-primary" style="width:100%;justify-content:center;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            Send Me an Email
          </a>
        </div>

        <!-- Quick Info -->
        <div class="card">
          <h4 style="font-size:.85rem;font-weight:700;color:var(--txt2);text-transform:uppercase;letter-spacing:.08em;margin-bottom:1rem;">Quick Info</h4>
          <div style="display:flex;flex-direction:column;gap:.75rem;">
            {[
              { label: 'Role',       value: 'Backend Developer' },
              { label: 'Stack',      value: 'Java · Spring Boot · MySQL' },
              { label: 'Education',  value: 'BE SE · Mehran UET' },
              { label: 'Location',   value: 'Sindh, Pakistan' },
              { label: 'Type',       value: 'Full-time / Internship / Freelance' },
              { label: 'Response',   value: 'Within 24 hours' },
            ].map(item => (
              <div style="display:flex;justify-content:space-between;gap:.5rem;font-size:.855rem;border-bottom:1px solid var(--border);padding-bottom:.75rem;">
                <span style="color:var(--txt3);font-weight:500;flex-shrink:0;">{item.label}</span>
                <span style="color:var(--txt);font-weight:600;text-align:right;">{item.value}</span>
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>

  </div>
</section>

<style>
  @media(max-width:768px) { .contact-grid { grid-template-columns:1fr !important; } }
</style>

</BaseLayout>
""")

print("\\n✅  All files written successfully!")
