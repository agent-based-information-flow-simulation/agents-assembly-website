import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-auto';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter({
			out: 'build',
			precompress: false,
			env: {
				host: 'HOST',
				port: 'PORT',
			},
		}),

    // hydrate the <div id="svelte"> element in src/app.html
    target: '#svelte',
  },

  preprocess: [
    preprocess({
      postcss: true,
    }),
  ],
};

export default config;
