export const profile = {
  name: 'Sibghatullah Laghari',
  shortName: 'Sibghatullah',
  title: 'Backend Engineer',
  tagline: 'Java · Spring Boot · REST APIs · Security',
  location: 'Sindh, Pakistan',
  email: 'siblaghari@gmail.com',
  github: 'https://github.com/sibghatullah-laghari',
  linkedin: 'https://linkedin.com/in/sibghatullah-laghari',
  fiverr: 'https://www.fiverr.com/sibghatullah-laghari',
  siteUrl: 'https://sibghatullah-laghari.github.io',
  resumePath: '/resume.pdf',
  resumeLastUpdated: 'June 2026',
  education: {
    degree: 'BE Software Engineering',
    university: 'Mehran University of Engineering & Technology',
    semester: '4th Semester Completed',
    cgpa: '3.8',
    period: '2024 — Present',
  },
  availability: [
    'Internship',
    'Full-Time',
    'Freelance',
    'Remote',
    'Hybrid',
    'Relocation',
  ],
  focus: [
    'Backend Engineering',
    'Product Engineering',
    'Open Source Contributions',
    'Scalable API Design',
    'System Design Learning',
  ],
  stats: [
    { value: '5+', label: 'Backend Systems' },
    { value: '10+', label: 'REST APIs Built' },
    { value: '1+', label: 'Yr Building' },
    { value: '3.8', label: 'CGPA' },
  ],
} as const;

export const aboutSummary = [
  'I build backend systems that solve real problems — authentication flows, data models, and APIs that other engineers can integrate with confidence.',
  'My work centers on Java and Spring Boot: layered architecture, secure endpoints, and relational databases designed for maintainability.',
  'I learn by shipping. Every project pushes me deeper into security, API design, and the engineering decisions that make software reliable at scale.',
  'Open source and collaboration are part of how I grow — I contribute where I can, review code, and build software meant to be used.',
];

export const openSource = {
  title: 'Open Source & Collaboration',
  description:
    'I build in public and collaborate with other engineers on backend systems, API design, and useful open source tools.',
  points: [
    'Contributing to and maintaining backend projects on GitHub',
    'Open to pair programming, code reviews, and architecture discussions',
    'Interested in projects where clean APIs and solid engineering matter',
    'Always looking to collaborate on software that solves real user problems',
  ],
};

export const experienceItems = [
  {
    id: 'freelance',
    role: 'Backend Engineer',
    org: 'Freelance · Independent Projects',
    period: 'Aug 2024 — Present',
    location: 'Sindh, Pakistan · Remote',
    summary:
      'Design and deliver backend systems end-to-end — from API contracts and database schemas to authentication and deployment-ready Spring Boot services.',
    bullets: [
      'Architect REST APIs with clear resource models, consistent error handling, and role-protected endpoints',
      'Implement JWT authentication, BCrypt hashing, and RBAC with Spring Security filter chains',
      'Design normalized MySQL schemas and map entities with JPA/Hibernate for query-efficient data access',
      'Structure services using Controller → Service → Repository layering with DTOs and separation of concerns',
      'Validate and document APIs with Postman collections for frontend and client integration',
      'Ship iteratively with Git feature branches, structured commits, and maintainable Maven builds',
    ],
    tech: ['Java', 'Spring Boot', 'Spring Security', 'JWT', 'MySQL', 'JPA', 'Maven', 'Git', 'Postman'],
    icon: 'code',
  },
  {
    id: 'education',
    role: 'BE Software Engineering',
    org: 'Mehran University of Engineering & Technology',
    period: '2024 — Present',
    location: 'Sindh, Pakistan',
    summary:
      'Engineering fundamentals applied to production-style backend work — databases, algorithms, and software design alongside hands-on Spring Boot projects.',
    bullets: [
      'Implement data structures and algorithms in Java with focus on practical problem solving',
      'Design relational databases — normalization, SQL queries, and schema-to-entity mapping',
      'Apply OOP, design patterns, and SOLID principles in layered backend codebases',
      'Collaborate on team projects using Git workflows, code reviews, and Agile practices',
      'CGPA 3.8 · 4th semester completed',
    ],
    tech: ['Java', 'DSA', 'SQL', 'OOP', 'Git', 'Software Engineering'],
    icon: 'education',
  },
];
