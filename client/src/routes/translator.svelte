<script context="module">
  export const prerender = true;
</script>

<script>
  import { getApiUrl } from '../utils/env';
  import CodeEditor from '../components/codeEditor.svelte';

  let aasmCode =
    'message facebook_post, query\n' +
    '\tprm photos, float\n' +
    'emessage\n' +
    '\n' +
    'agent user\n' +
    '\tprm friends, list, conn\n' +
    '\tprm num_seen_photos, float, init, 0\n' +
    '\n' +
    '\tbehav initialize, setup\n' +
    '\t\taction initialize_friends, modify_self\n' +
    '\t\t\tdecl max_friends, float, 0\n' +
    '\t\t\tlen max_friends, connections\n' +
    '\t\t\tdecl num_friends, float, 0\n' +
    '\t\t\trand num_friends, int, uniform, 0, max_friends\n' +
    '\t\t\tsubs friends, connections, num_friends\n' +
    '\t\teaction\n' +
    '\tebehav\n' +
    '\n' +
    '\tbehav facebook_activity, cyclic, 30\n' +
    '\t\taction post_photos, send_msg, facebook_post, query\n' +
    '\t\t\tdecl num_photos, float, 0\n' +
    '\t\t\trand num_photos, int, uniform, 21, 37\n' +
    '\t\t\tset send.photos, num_photos\n' +
    '\t\t\tsend friends\n' +
    '\t\teaction\n' +
    '\tebehav\n' +
    '\n' +
    '\tbehav read_posts, msg_rcv, facebook_post, query\n' +
    '\t\taction update_seen_photos, modify_self\n' +
    '\t\t\tadd num_seen_photos, rcv.photos\n' +
    '\t\teaction\n' +
    '\tebehav\n' +
    'eagent\n' +
    '\n' +
    'graph statistical\n' +
    '\tdefg user, 150, dist_exp, 0.1\n' +
    'egraph\n';
  let translatedCode = '';

  const API_URL = getApiUrl();

  const translate = async (aasmCode) => {
    const codeLines = aasmCode.split('\n');
    const body = {
      code_lines: codeLines,
    };
    const response = await fetch(`${API_URL}/code/spade`, {
      method: 'POST',
      body: JSON.stringify(body),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (response.ok) {
      const responseBody = await response.json();
      const translatorVersion = responseBody['translator_version'];
      translatedCode = `# translator version: ${translatorVersion}\n`;
      responseBody['agent_code_lines'].forEach((codeLine) => {
        translatedCode += codeLine;
      });
      if (responseBody['graph_code_lines'].length) {
        translatedCode += '\n# graph generation\n';
        responseBody['graph_code_lines'].forEach((codeLine) => {
          translatedCode += codeLine;
        });
      }
    } else if (response.status === 400) {
      const responseBody = await response.json();
      const translatorVersion = responseBody['translator_version'];
      translatedCode = `# translator version: ${translatorVersion}\n`;
      translatedCode += `${responseBody['place']}\n`;
      translatedCode += `${responseBody['reason']}\n`;
      translatedCode += `${responseBody['suggestion']}\n`;
    } else {
      throw new Error('Something went wrong... :(');
    }
  };

  const handleCtrlEnter = async (event) => {
    if (!event.ctrlKey || event.key !== 'Enter') return;
    event.preventDefault();
    await translate(aasmCode);
  };
</script>

<svelte:window on:keydown={handleCtrlEnter} />

<svelte:head>
  <title>translator.aasm</title>
</svelte:head>

<div class="flex flex-col items-center">
  <div class="flex flex-row items-stretch w-11/12">
    <div class="w-1/2 border">
      <CodeEditor bind:code={aasmCode} on:keydown />
    </div>
    <div class="w-1/2 border">
      <CodeEditor bind:code={translatedCode} isReadOnly={true} />
    </div>
  </div>
  <button
    class="w-11/12 bg-transparent hover:bg-green-500 text-green-700 hover:text-white py-2 px-4 border border-green-500 hover:border-transparent rounded"
    on:click={() => translate(aasmCode)}>translate (Ctrl + Enter)</button
  >
</div>
