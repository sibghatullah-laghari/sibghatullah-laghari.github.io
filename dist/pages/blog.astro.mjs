import { c as createComponent, r as renderComponent, a as renderTemplate, m as maybeRenderHead, b as addAttribute } from '../chunks/astro/server_D57DNOQO.mjs';
import 'kleur/colors';
import { $ as $$BaseLayout } from '../chunks/BaseLayout_C_UA5XDo.mjs';
export { renderers } from '../renderers.mjs';

const $$Blog = createComponent(($$result, $$props, $$slots) => {
  const posts = [
    {
      title: "How JWT Authentication Works in Spring Boot",
      excerpt: "A practical walkthrough of stateless JWT auth \u2014 token generation on login, secret key signing, filter chain configuration in Spring Security, and protected route setup.",
      date: "Mar 2026",
      readTime: "9 min read",
      tags: ["Spring Boot", "JWT", "Spring Security"],
      category: "Tutorial"
    },
    {
      title: "Designing Clean REST APIs \u2014 Beyond the Basics",
      excerpt: "Move past CRUD. Proper resource naming, HTTP semantics, idempotency, pagination, error response schemas, and versioning strategies for production APIs.",
      date: "Feb 2026",
      readTime: "7 min read",
      tags: ["REST API", "API Design", "Backend"],
      category: "Guide"
    },
    {
      title: "Spring Data JPA Deep Dive \u2014 Queries, Projections & Performance",
      excerpt: "JPQL vs native queries, derived method names, projections for selective data fetching, and N+1 problem diagnosis and solutions with Hibernate.",
      date: "Feb 2026",
      readTime: "11 min read",
      tags: ["JPA", "Hibernate", "Spring Boot", "MySQL"],
      category: "Deep Dive"
    },
    {
      title: "Role-Based Access Control in Spring Security",
      excerpt: "Implementing RBAC with Spring Security from scratch \u2014 UserDetailsService, GrantedAuthority, method-level security with @PreAuthorize, and securing REST endpoints.",
      date: "Jan 2026",
      readTime: "8 min read",
      tags: ["Spring Security", "RBAC", "Authorization"],
      category: "Tutorial"
    },
    {
      title: "Database Schema Design for Backend Developers",
      excerpt: "Normalization to 3NF, foreign key strategies, index design, and how your database schema decisions directly impact your JPA entity modeling and query performance.",
      date: "Jan 2026",
      readTime: "10 min read",
      tags: ["Database", "MySQL", "Schema Design"],
      category: "Guide"
    }
  ];
  const catColor = {
    "Tutorial": "badge-indigo",
    "Guide": "badge-green",
    "Deep Dive": "badge-yellow"
  };
  return renderTemplate`${renderComponent($$result, "BaseLayout", $$BaseLayout, { "title": "Blog \u2014 Sibghatullah Laghari" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<section class="sec"> <div class="wrap"> <!-- Header --> <div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:1.5rem;margin-bottom:3.5rem;"> <div> <span class="s-eyebrow">Writing</span> <h1 class="s-title">Blog</h1> <p class="s-desc">Technical articles on Spring Boot, JWT, REST API design, and backend engineering.</p> </div> <span class="badge badge-yellow" style="font-size:.75rem;align-self:flex-end;">Publishing soon</span> </div> <!-- Info Banner --> <div style="display:flex;align-items:flex-start;gap:.875rem;padding:1.1rem 1.4rem;background:rgba(99,102,241,.07);border:1px solid rgba(99,102,241,.2);border-radius:.75rem;margin-bottom:2.5rem;"> <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:var(--accent2);flex-shrink:0;margin-top:.1rem;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> <p style="font-size:.875rem;color:var(--txt2);line-height:1.6;">These are planned articles I'm writing based on real backend problems I've encountered. Publishing schedule: ~1 article every 2 weeks.</p> </div> <!-- Posts --> <div style="display:flex;flex-direction:column;gap:1.25rem;"> ${posts.map((post, i) => renderTemplate`<article class="card" style="display:flex;flex-wrap:wrap;align-items:stretch;gap:1.5rem;padding:1.5rem 1.75rem;"> <!-- Left: number --> <div style="font-size:2.5rem;font-weight:900;color:var(--txt3);letter-spacing:-.04em;font-variant-numeric:tabular-nums;line-height:1;padding-top:.1rem;width:2.5rem;flex-shrink:0;font-family:'JetBrains Mono',monospace;"> ${String(i + 1).padStart(2, "0")} </div> <!-- Right: content --> <div style="flex:1;min-width:0;"> <div style="display:flex;flex-wrap:wrap;align-items:center;gap:.5rem;margin-bottom:.75rem;"> <span${addAttribute(`badge ${catColor[post.category] || "badge-neutral"}`, "class")} style="font-size:.65rem;">${post.category}</span> ${post.tags.map((t) => renderTemplate`<span class="badge badge-neutral" style="font-size:.65rem;">${t}</span>`)} </div> <h2 style="font-size:1rem;font-weight:700;margin-bottom:.5rem;line-height:1.4;">${post.title}</h2> <p style="font-size:.875rem;color:var(--txt2);line-height:1.7;margin-bottom:.75rem;">${post.excerpt}</p> <div style="display:flex;align-items:center;gap:1rem;font-size:.75rem;color:var(--txt3);"> <span>${post.date}</span> <span>&middot;</span> <span>${post.readTime}</span> <span>&middot;</span> <span style="color:var(--accent2);font-weight:600;">Coming Soon</span> </div> </div> </article>`)} </div> </div> </section> ` })}`;
}, "C:/Users/sibla/Downloads/sibghatullah-laghari.github.io/src/pages/blog.astro", void 0);

const $$file = "C:/Users/sibla/Downloads/sibghatullah-laghari.github.io/src/pages/blog.astro";
const $$url = "/blog";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Blog,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
