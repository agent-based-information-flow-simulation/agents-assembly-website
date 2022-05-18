import { writable } from 'svelte/store';

export const indexFadeAnimationStore = writable({
  isFadeAlreadyUsed: false,
});
