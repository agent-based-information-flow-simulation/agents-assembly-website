<script context="module">
  import { marked } from 'marked';

  export const load = async ({ fetch }) => {
    const documentationUrl =
      'https://raw.githubusercontent.com/agent-based-information-flow-simulation/agents-assembly-translator/main/DOCS.md';
    const response = await fetch(documentationUrl);
    if (response.ok) {
      const textMarkdown = await response.text();
      // without target='_self' double click is required
      const htmlDocumentation = marked(textMarkdown).replaceAll(
        '<a',
        '<a class="hover:underline" target="_self"'
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
  };

  export const prerender = true;
  export const hydrate = false;
</script>

<script>
  export let htmlDocumentation;
</script>

<svelte:head>
  <title>docs.aasm</title>
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
    font-size: x-large;
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
