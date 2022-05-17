<script context="module">
  import { marked } from 'marked';

  export async function load({ fetch }) {
    const documentationUrl =
      'https://raw.githubusercontent.com/agent-based-information-flow-simulation/agents-assembly-translator/main/DOCS.md';
    const response = await fetch(documentationUrl);
    if (response.ok) {
      const textMarkdown = await response.text();
      // without target='_target' double click is required
      const htmlDocumentation = marked(textMarkdown).replaceAll(
        '<a',
        '<a class="hover:underline" target="_target"'
      );
      return {
        props: {
          htmlDocumentation,
        },
      };
    } else {
      return {
        props: {
          htmlDocumentation: `<p>Couldn't load the documentation :(</p>`,
        },
      };
    }
  }

  export const prerender = true;
</script>

<script>
  export let htmlDocumentation;
</script>

<svelte:head>
  <title>*.aasm - docs</title>
</svelte:head>

<div class="markdown">
  {@html htmlDocumentation}
</div>

<style>
  .markdown :global() {
    margin-left: 1em;
    margin-right: 1em;
  }
  .markdown :global(h1) {
    font-size: larger;
    font-weight: bold;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }

  .markdown :global(h2) {
    font-size: large;
    font-weight: bold;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }

  .markdown :global(h3) {
    font-size: medium;
    font-weight: bold;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }

  .markdown :global(p) {
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }

  .markdown :global(pre) {
    margin-left: 1em;
    margin-right: 1em;
  }

  .markdown :global(ul) {
    margin-left: 1em;
    margin-right: 1em;
    list-style-type: circle;
  }

  .markdown :global(li) {
    margin-left: 1em;
    margin-right: 1em;
  }

  .markdown :global(code) {
    font-style: italic;
  }
</style>
