export interface SkillCategory {
  title: string;
  description: string;
  skills: string[];
  variant: 'core' | 'security' | 'tools' | 'exploring';
}

export const skillCategories: SkillCategory[] = [
  {
    title: 'Core Backend',
    description: 'Primary stack for building production-style services',
    skills: ['Java', 'Spring Boot', 'Spring Security', 'REST APIs', 'JPA', 'Hibernate', 'MySQL'],
    variant: 'core',
  },
  {
    title: 'Authentication & Security',
    description: 'Identity, access control, and secure API patterns',
    skills: ['JWT', 'RBAC', 'OAuth2', 'BCrypt'],
    variant: 'security',
  },
  {
    title: 'Tools',
    description: 'Day-to-day engineering workflow',
    skills: ['Git', 'GitHub', 'Maven', 'Postman', 'Linux'],
    variant: 'tools',
  },
  {
    title: 'Currently Exploring',
    description: 'Growing into — honest progression, not claimed mastery',
    skills: ['Docker', 'Microservices', 'Cloud', 'System Design', 'Open Source'],
    variant: 'exploring',
  },
];
