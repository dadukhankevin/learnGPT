<script lang="ts">
    import { onMount } from 'svelte';
  
    let section: string | null;
    let categories: string[] = [];
  
    onMount(async () => {
      const urlParams = new URLSearchParams(window.location.search);
      section = urlParams.get("section");
  
      if (section) {
        const response = await fetch(`http://127.0.0.1:5000/get_category?category=${section}`);
        const data = await response.json();
        categories = data || [];
      }
    });
  </script>
  <div class="h-full grid grid-rows-[auto_1fr_auto] gap-1">

    <div class="bg-surface-500/30 p-4"></div>
    <div class="bg-surface-500/30 p-4">
  <h1>{section}</h1>
  <div class="spacer-large"></div>
  <div class="grid-container grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 card-block">
    <!-- Using #each to loop through the JSON data -->
    {#each categories as item}
      <!--{#each Object.entries(item) as [name, data]} -->
        <div class="grid-item rounded-md p-4 text-center block-card card-hover card">
          <a href="/learn?set={item}&category={section}"><h4>{item}</h4></a>
        </div>
      {/each}
   <!-- {/each} -->
</div>
</div>
<div class="bg-surface-500/30 p-4">
	Learn anything
	</div>  
</div>
