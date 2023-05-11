<!-- YOU CAN DELETE EVERYTHING IN THIS PAGE -->
<script lang="ts">
	import { InputChip, ProgressBar, Autocomplete} from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';

	let list: any[] = [];
	let inputValue = '';
	function handleInputChange(event: Event) {
		const target = event.target as HTMLInputElement;
    	inputValue = target.value;  
		const index: number = items.indexOf(inputValue);
		match = index !== -1;
	}
	let items: any[] = [];
	let match: boolean = false;
	async function fetchData() {
		const response = await fetch('http://127.0.0.1:5000/list');
		const data = await response.json();
		items = data;
		items = items;
	}
	onMount(fetchData);
	$: items = items;
	$: match = match;
	function new_category(){
		let category = document.getElementById("category") as HTMLInputElement;
		match = true;
		fetch("http://127.0.0.1:5000/add?name="+category.value).then(()=>{fetchData()})
	}
</script>
<div class="h-full grid grid-rows-[auto_1fr_auto] gap-1">

	<div class="bg-surface-500/30 p-4"></div>
	<div class="bg-surface-500/30 p-4">
		<div class="card p-4 center">
		<InputChip bind:value={list} max={3} name="chips" placeholder="Enter any value..." />
		<div class="spacer"></div>

		{#if list.length < 3}
		<ProgressBar label="Progress Bar" bind:value={list.length} max={3} />
		{/if}
		{#if list.length > 0}
		<div class="spacer-large"></div>
		<input type="search" list="languages" on:input="{handleInputChange}" placeholder="Pick a category" class ="card" id="category">
		<datalist id="languages">
		{#each items as item}
			<option value={item} />
		{/each}
		</datalist>
		{#if match === false}

		<button on:click="{new_category}" type="button" class="btn varient-filled">Create New</button>
		{/if}
		{#if match === true}
		<button type="button" class="btn variant-filled">Generate Learning Set</button>
		{/if}

		{/if}


		
		</div>
		<div class="spacer-large"></div>
		<div class="spacer-large"></div>
			<div class="grid-container grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
			  <!-- Using #each to loop through the JSON data -->
			  {#each items as item}
				<!--{#each Object.entries(item) as [name, data]} -->
				  <div class="grid-item rounded-md p-4 text-center block-card card-hover card">
					<h4>{item}</h4>
				  </div>
				{/each}
			 <!-- {/each} -->
			</div>
		  
</div>		  
	<div class="bg-surface-500/30 p-4">
	Learn anything
	</div>
</div>
				