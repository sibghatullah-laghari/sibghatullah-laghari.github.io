import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://sibghatullah-laghari.github.io',
  base: '/',
  integrations: [tailwind()],
});