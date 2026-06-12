import { profile } from './profile';

export const defaultSeo = {
  title: `${profile.name} — Backend Engineer | Java · Spring Boot`,
  description:
    'Backend Engineer specializing in Java, Spring Boot, REST APIs, JWT authentication, and database-driven systems. Open to internships, full-time, and freelance opportunities.',
  keywords: [
    'Backend Engineer',
    'Java Developer',
    'Spring Boot Developer',
    'Software Engineer',
    'Product Engineer',
    'REST API',
    'JWT',
    'MySQL',
    'Pakistan',
    'Remote',
  ].join(', '),
  ogImage: `${profile.siteUrl}/og-image.png`,
  twitterHandle: '@sibghatullah',
};

export const navLinks = [
  { href: '/', label: 'Home' },
  { href: '/projects', label: 'Projects' },
  { href: '/experience', label: 'Experience' },
  { href: '/working', label: 'What I Do' },
  { href: '/resume', label: 'Resume' },
  { href: '/blog', label: 'Blog' },
  { href: '/contact', label: 'Contact' },
];
