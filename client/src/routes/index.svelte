<script context="module">
  export const prerender = true;
</script>

<script>
  import { fade } from 'svelte/transition';
  import { onMount } from 'svelte';
  import Typed from 'typed.js';
  import { browser } from '$app/env';
  import { typingStore } from '../stores/typingStore';
  import { clickAnywhere } from '../events/clickAnywhere';

  let isTypingInProgress;
  typingStore.subscribe((store) => {
    isTypingInProgress = store['isTypingInProgress'];
  });

  let isDoneTyping;
  typingStore.subscribe((store) => {
    isDoneTyping = store['isDoneTyping'];
  });

  const handleClickAnywhere = () => {
    typingStore.set({
      isTypingInProgress: false,
      isDoneTyping: true,
    });
  };

  const handleTypingAnimation = () => {
    if (browser) {
      // refresh
      if (isTypingInProgress && !isDoneTyping) {
        typingStore.set({
          isTypingInProgress: false,
          isDoneTyping: true,
        });
      }
      // first time
      else if (!isTypingInProgress && !isDoneTyping) {
        typingStore.set({
          isTypingInProgress: true,
          isDoneTyping: false,
        });

        const typedOptions = {
          strings: [
            "I'm simple.",
            "I'm agent-oriented.",
            "I'm safe.",
            "I'm target agnostic.",
            "I'm Agents Assembly.",
          ],
          typeSpeed: 110,
          backSpeed: 95,
          loop: false,
          showCursor: true,
          onComplete: () => {
            setTimeout(() => {
              typingStore.set({
                isTypingInProgress: false,
                isDoneTyping: true,
              });
            }, 1500);
          },
        };
        // start the animation
        const typed = new Typed('.typed', typedOptions);
      }
    }
  };

  onMount(() => {
    handleTypingAnimation();
  });
</script>

<svelte:head>
  <title>*.aasm</title>
</svelte:head>

<div use:clickAnywhere on:clickAnywhereEvent={handleClickAnywhere} class="content">
  {#if !isDoneTyping}
    <div class="aasm-typed flex flex-col items-center text-center">
      <h1 class="text-4xl font-bold uppercase"><span class="typed" /></h1>
    </div>
  {:else}
    <div>
      <div class="flex flex-col items-center">
        <h1 class="text-4xl font-bold uppercase">Agents Assembly</h1>
      </div>
      <div in:fade class="flex items-center justify-center h-auto p-5">
        <div class="container">
          <div class="flex justify-center">
            <div class="bg-white shadow-xl text-center rounded-lg">
              <ul class="divide-y divide-gray-300">
                <li class="p-4 hover:bg-gray-50">Simple domain specific language.</li>
                <li class="p-4 hover:bg-gray-50">Designed for agent-oriented programming.</li>
                <li class="p-4 hover:bg-gray-50">If it compiles, it works.</li>
                <li class="p-4 hover:bg-gray-50">Forget about runtime exceptions.</li>
                <li class="p-4 hover:bg-gray-50">Target language agnostic.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="flex flex-col items-center">
        <h1 class="text-2xl uppercase">Install using pip</h1>
        <pre>
      <code>
        pip install aasm
      </code>
    </pre>
      </div>
    </div>
  {/if}
</div>
