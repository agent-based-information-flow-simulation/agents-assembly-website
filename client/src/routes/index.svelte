<script context="module">
  export const prerender = true;
</script>

<script>
  import { fade } from 'svelte/transition';
</script>

<svelte:head>
  <title>*.aasm</title>
</svelte:head>

<div in:fade>
  <div class="flex flex-col items-center">
    <h1 class="text-4xl font-bold uppercase">Agents Assembly</h1>
  </div>
  <div class="flex items-center justify-center h-auto p-5">
    <div class="container">
      <div class="flex justify-center">
        <div class="bg-white shadow-xl text-center rounded-lg w-1/3">
          <ul class="divide-y divide-gray-300">
            <li class="p-4 hover:bg-gray-50">Agents concepts built into the language.</li>
            <li class="p-4 hover:bg-gray-50">If it compiles it works.</li>
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
