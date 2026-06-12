export interface ProjectCaseStudy {
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  status: 'Completed' | 'In Progress' | 'Live';
  priority: number;
  featured: boolean;
  backendOnly?: boolean;
  github: string;
  problem: string;
  solution: string;
  architecture: string;
  keyFeatures: string[];
  challenges: string;
  learning: string;
  impact: string;
  tech: string[];
}

export const flagshipProjects: ProjectCaseStudy[] = [
  {
    id: 'cctrs',
    slug: 'cctrs',
    title: 'CCTRS',
    subtitle: 'Carbon Contribution & Reward Tracking System',
    status: 'Completed',
    priority: 1,
    featured: true,
    github: 'https://github.com/sibghatullah-laghari',
    problem:
      'Organizations need a reliable way to log carbon-reducing activities, score contributions, and issue rewards — with different access levels for users and administrators.',
    solution:
      'Built a Spring Boot backend with REST endpoints for activity logging, score calculation, and reward issuance. JWT-secured routes enforce USER vs ADMIN permissions across all operations.',
    architecture:
      'Layered design: REST controllers → service layer (business rules) → JPA repositories → MySQL. Stateless auth via JWT filter chain in Spring Security.',
    keyFeatures: [
      'Multi-role API access (USER, ADMIN)',
      'Contribution logging and reward calculation engine',
      'Admin dashboard endpoints for oversight',
      'Documented REST API for client integration',
    ],
    challenges:
      'Balancing reward calculation logic in the service layer while keeping controllers thin and repositories focused on persistence.',
    learning:
      'How to model domain rules in services, protect routes by role, and design APIs that stay consistent as features grow.',
    impact:
      'End-to-end backend system demonstrating authentication, RBAC, and business logic in a real tracking domain.',
    tech: ['Java', 'Spring Boot', 'Spring Security', 'JWT', 'MySQL', 'JPA/Hibernate', 'Maven', 'REST APIs'],
  },
  {
    id: 'mediconnect',
    slug: 'mediconnect',
    title: 'MediConnect',
    subtitle: 'Healthcare Backend API Platform',
    status: 'Completed',
    priority: 2,
    featured: true,
    backendOnly: true,
    github: 'https://github.com/sibghatullah-laghari',
    problem:
      'Healthcare workflows need a secure backend that manages users, roles, and sensitive data — without coupling business logic to any single frontend.',
    solution:
      'Designed and built a backend-only Spring Boot service with REST endpoints, role-based access, and a relational schema shaped around core healthcare entities and workflows.',
    architecture:
      'Client → REST API → Spring Security (JWT + RBAC) → Service Layer → JPA/Hibernate → MySQL. API-first design with clear request/response contracts.',
    keyFeatures: [
      'REST API with role-protected endpoints',
      'JWT authentication and authorization flow',
      'Normalized database schema for core entities',
      'Postman-tested endpoint documentation',
    ],
    challenges:
      'Designing secure data flow and access boundaries for sensitive domain data while keeping the API predictable for future clients.',
    learning:
      'Backend-first product thinking — security, schema design, and API contracts matter as much as feature coverage when there is no frontend in scope.',
    impact:
      'Demonstrates ability to deliver a complete backend platform: API design, security, and database architecture without relying on UI screenshots.',
    tech: ['Java', 'Spring Boot', 'Spring Security', 'JWT', 'RBAC', 'MySQL', 'JPA', 'REST APIs', 'Postman'],
  },
  {
    id: 'ulsm',
    slug: 'ulsm',
    title: 'ULSM',
    subtitle: 'User Login & Service Management API',
    status: 'Completed',
    priority: 3,
    featured: true,
    github: 'https://github.com/sibghatullah-laghari',
    problem:
      'Applications need a dependable user management backend — registration, login, profile updates, and admin control — with secure, token-based access to protected routes.',
    solution:
      'Implemented a production-style user management API covering the full auth lifecycle: BCrypt registration, JWT login, token-protected routes, and role-specific capabilities.',
    architecture:
      'Standard Spring Boot layering with a dedicated security config, UserDetailsService integration, and JPA-backed user persistence in MySQL.',
    keyFeatures: [
      'User registration with password hashing',
      'JWT issuance and stateless session management',
      'Profile management for authenticated users',
      'ADMIN endpoints for user oversight',
    ],
    challenges:
      'Configuring Spring Security filter order and ensuring protected vs public routes behave correctly across all HTTP methods.',
    learning:
      'Deep understanding of authentication vs authorization and how to structure security config that stays maintainable as endpoints grow.',
    impact:
      'Reusable auth foundation applicable to any product needing secure user management and RBAC.',
    tech: ['Spring Boot', 'Spring Security', 'JWT', 'BCrypt', 'MySQL', 'JPA', 'Maven'],
  },
];

export const otherProjects: ProjectCaseStudy[] = [
  {
    id: 'complaint-tracking',
    slug: 'complaint-tracking',
    title: 'Complaint & Case Tracking',
    subtitle: 'Multi-Role Case Workflow API',
    status: 'Completed',
    priority: 4,
    featured: false,
    github: 'https://github.com/sibghatullah-laghari',
    problem:
      'Citizen complaints require structured workflows — submission, assignment, status updates, and resolution — with different roles at each stage.',
    solution:
      'Built a REST backend supporting citizen submission, moderator processing, and admin oversight with status tracking and audit-friendly data modeling.',
    architecture:
      'Role-based REST API over a normalized MySQL schema optimized for case queries and status transitions.',
    keyFeatures: [
      'Multi-role workflow (citizen, moderator, admin)',
      'Case status lifecycle management',
      'Audit-friendly relational schema',
    ],
    challenges:
      'Modeling state transitions cleanly in the service layer without leaking workflow logic into controllers.',
    learning:
      'Designing APIs around domain workflows rather than generic CRUD endpoints.',
    impact:
      'Shows capability to build workflow-driven backends with proper access control.',
    tech: ['Spring Boot', 'Spring Security', 'MySQL', 'JPA', 'REST APIs', 'Maven'],
  },
  {
    id: 'portfolio',
    slug: 'portfolio',
    title: 'Portfolio Website',
    subtitle: 'Static Site · GitHub Pages',
    status: 'Live',
    priority: 5,
    featured: false,
    github: 'https://github.com/sibghatullah-laghari/sibghatullah-laghari.github.io',
    problem:
      'Need a fast, professional portfolio that recruiters can scan in under a minute — without backend overhead or CMS complexity.',
    solution:
      'Built with Astro for static generation, deployed via GitHub Actions to GitHub Pages. Component-based architecture with global design system.',
    architecture:
      'Astro SSG → static HTML/CSS → GitHub Pages CDN. Zero runtime backend, optimized for load time and SEO.',
    keyFeatures: [
      'Static site generation for fast loads',
      'Responsive dark-theme UI',
      'GitHub Actions CI/CD pipeline',
    ],
    challenges:
      'Balancing rich content structure with minimal JavaScript and fast first paint.',
    learning:
      'Product-minded delivery — ship something useful, iterate, and keep the stack simple.',
    impact:
      'Live deployment demonstrating full-stack awareness from build pipeline to production hosting.',
    tech: ['Astro', 'Tailwind CSS', 'GitHub Pages', 'GitHub Actions'],
  },
];

export const currentlyBuilding = {
  title: 'Flagship Project',
  description:
    'Reserved for the next major backend system — microservices architecture, advanced API design, or open source contribution at scale.',
  status: 'Planning',
  focus: ['System Design', 'Scalable APIs', 'Open Source'],
};

export const allProjects = [...flagshipProjects, ...otherProjects].sort(
  (a, b) => a.priority - b.priority,
);
