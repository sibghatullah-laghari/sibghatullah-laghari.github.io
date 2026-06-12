export interface Certification {
  name: string;
  provider: string;
  skillsLearned: string[];
  /** Set when verification URL is available */
  verificationUrl?: string;
  /** Optional completion or issue date */
  date?: string;
}

/**
 * Add certificates here with verification URLs when available.
 * Example:
 * {
 *   name: 'Spring Boot Developer',
 *   provider: 'Coursera',
 *   skillsLearned: ['Spring Boot', 'REST', 'Security'],
 *   verificationUrl: 'https://...',
 *   date: 'Jan 2026',
 * }
 */
export const certifications: Certification[] = [];
