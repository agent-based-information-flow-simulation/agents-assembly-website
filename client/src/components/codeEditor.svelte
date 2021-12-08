<script>
  import { tick } from 'svelte';

  export let code = '';
  export let isReadOnly = false;

  async function handleTab(event) {
    if (event.key !== 'Tab') return;
    event.preventDefault();
    const { selectionStart, selectionEnd, value } = this;
    code = (
      value.slice(0, selectionStart) + '\t' + value.slice(selectionEnd)
    )
    await tick();
    this.selectionStart = this.selectionEnd = selectionStart + 1;
  };
</script>

<textarea bind:value={code} readonly={isReadOnly} on:keydown={handleTab} spellcheck="false" />

<style>
  textarea {
    width: 100%;
    height: 85vh;
    resize: none;
  }
  textarea:focus {
    outline: none;
  }
</style>
