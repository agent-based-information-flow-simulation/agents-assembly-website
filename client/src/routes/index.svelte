<script context="module">
  export const prerender = true;
</script>

<script>
  import { fade } from 'svelte/transition';
  import { onMount } from 'svelte';
  import Typed from 'typed.js';
  import { browser } from '$app/env';
  import { typingStore } from '../stores/typingStore';
  import { indexFadeAnimationStore } from '../stores/indexFadeAnimationStore';
  import { clickAnywhere } from '../events/clickAnywhere';

  let isTypingInProgress;
  typingStore.subscribe((store) => {
    isTypingInProgress = store['isTypingInProgress'];
  });

  let isDoneTyping;
  typingStore.subscribe((store) => {
    isDoneTyping = store['isDoneTyping'];
  });

  let isFadeAlreadyUsed;
  indexFadeAnimationStore.subscribe((store) => {
    isFadeAlreadyUsed = store['isFadeAlreadyUsed'];
  });

  $: singleFadeAnimation = isFadeAlreadyUsed
    ? () => {}
    : (node) => {
        indexFadeAnimationStore.set({
          isFadeAlreadyUsed: true,
        });
        return fade(node, { duration: 400 });
      };

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

        const unshuffled = [
          "I'm simple.",
          "I'm agent-oriented.",
          "I'm safe.",
          "I'm target agnostic.",
        ];

        const shuffled = unshuffled
          .map((value) => ({ value, sort: Math.random() }))
          .sort((a, b) => a.sort - b.sort)
          .map(({ value }) => value);

        shuffled.push("I'm Agents Assembly.");

        const typedOptions = {
          strings: shuffled,
          typeSpeed: 110,
          backSpeed: 90,
          loop: false,
          showCursor: true,
          backDelay: 1000,
          onComplete: () => {
            setTimeout(() => {
              typingStore.set({
                isTypingInProgress: false,
                isDoneTyping: true,
              });
            }, 2000);
          },
        };

        // start the animation
        new Typed('.typed', typedOptions);
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
      <div in:singleFadeAnimation class="flex items-center justify-center h-auto p-5">
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
