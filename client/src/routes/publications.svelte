<script context="module">
  export const prerender = true;
  export const hydrate = false;
</script>

<svelte:head>
  <title>publications.aasm</title>
</svelte:head>

<div class="flex flex-col items-center ml-0 mr-0 md:ml-24 md:mr-24">
  <p class="text-center">Related publications:</p>
  <ul class="text-center list-none md:text-left md:list-disc">
    <li>
      <p>
        <a
          class="text-blue-800 hover:underline font-bold"
          href="https://doi.org/10.1007/978-3-031-18192-4_42"
          >Agents Assembly: Domain Specific Language for Agent Simulations</a
        > (PAAMS'22)
      </p>
      <p>
        by
        <a class="text-blue-800 hover:underline" href="https://orcid.org/0000-0001-5425-7440"
          >Przemysław Hołda</a
        >,
        <a class="text-blue-800 hover:underline" href="https://orcid.org/0000-0003-1524-7877"
          >Kajetan Rachwał</a
        >,
        <a class="text-blue-800 hover:underline" href="https://orcid.org/0000-0002-8930-7564"
          >Jan Sawicki</a
        >,
        <a class="text-blue-800 hover:underline" href="https://orcid.org/0000-0001-7714-4844"
          >Maria Ganzha</a
        >, and
        <a class="text-blue-800 hover:underline" href="https://orcid.org/0000-0002-8069-2152"
          >Marcin Paprzycki</a
        >.
      </p>
      <br />
      <p class="italic">
        Researchers studying group behavior, social dynamics, or epidemiology lack an easy-to-use
        tool to run large-scale simulations. This contribution introduces a domain specific language
        (Agents Assembly; AASM) and a toolset for creating and running scalable simulations, using
        containerized environment. The proposed language supports describing abstract concepts, such
        as agent, message, and behavior. Its structure, resembling assembly mnemonics, is simple to
        understand. The language is supported by a code generation module with a graphical user
        interface, which allows defining simulations using instruction blocks. The AASM code is
        translated to Python and runs in a distributed containerized ecosystem, utilizing a slightly
        modified SPADE agent framework. The developed toolset includes also data storage and live
        visualization.
      </p>
      <br />
      <p>
        The demonstration took place during the 20th International Conference on Practical
        Applications of Agents and Multi-Agents Systems (PAAMS'22). The paper won second place in
        the IBM Demonstration Award.
      </p>
    </li>
  </ul>
</div>
