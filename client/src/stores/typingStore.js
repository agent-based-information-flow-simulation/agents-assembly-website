import { writable } from "svelte/store";

export const typingStore = writable({
    isTypingInProgress: false,
    isDoneTyping: false,
});
