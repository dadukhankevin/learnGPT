<script lang="ts">
    	import { Stepper, Step} from '@skeletonlabs/skeleton';
        import { onMount } from 'svelte';
        import { Modal, modalStore } from '@skeletonlabs/skeleton';
        import type { ModalSettings, ModalComponent } from '@skeletonlabs/skeleton';
	    import { query_selector_all } from 'svelte/internal';
        let locker = true;
        
        function check(answer: string) {
            const modal: ModalSettings = {
                type: 'confirm',
                title: 'Grade yourself!',
                buttonTextConfirm: "I was correct",
                buttonTextCancel: "Try again",
                body: 'Here was the correct answer: ' + answer,
                response: (r: boolean) => {
                locker = !r;
                },
            };
            modalStore.trigger(modal);
        }

        function update(){
      
            const answerElements = document.getElementsByClassName("answer");
            for (const answerElement of answerElements) {
                const text = answerElement.innerHTML;
                const container = answerElement.nextElementSibling as HTMLElement;
                container.innerHTML = "";
                const words = text.split(/\s+/).filter(word => word.length > 0);
                for (const word of words) {
                    console.log(word)
                    const span = document.createElement("span");
                    span.className = "word";
                    span.textContent = " "+word;
                    const fadeInSpeed = Math.floor(Math.random() * 5000);
                    // span.style.animationDelay = fadeInSpeed + "ms";
                    const fadeOutSpeed = Math.floor(Math.random() * 5000);
                    if (container) {
                    container.appendChild(span);
                    setInterval(() => {
                        span.style.opacity = "1";
                        span.style.transition = "opacity 1s ease-in-out";
                        setTimeout(() => {
                        span.style.opacity = "0";
                        }, fadeInSpeed);
                    }, fadeOutSpeed);
                    }
                }
            }
        }
    //stuff for the stepper
    let data: Record<string, {term: string, definition: string}> = {};
  let keys: string[] = []; // get the keys of the json object
  let index: number = 0; // keep track of the current step index
  let input: HTMLInputElement; // bind to the input element


  function onStep(e: CustomEvent<{state: {current: number}, step: number}>) {
    // update the index when the step changes
    index = e.detail.state.current;
    update();
  }
  let currentMessage = '';
  async function fetchData() {
    // fetch the json data from example.com/get
    const urlParams = new URLSearchParams(window.location.search);
    let set = urlParams.get("set");
    let category = urlParams.get("category");

    let response = await fetch('http://127.0.0.1:5000/learn?set='+set +'&category='+category);
    if (response.ok) {
      data = await response.json();
      keys = Object.keys(data);
    } else {
      alert('Error fetching data');
    }
  }
  onMount(fetchData); 

</script>
<div class="h-full grid grid-rows-[auto_1fr_auto] gap-1">

	<div class="bg-surface-500/30 p-4"></div>
	<div class="bg-surface-500/30 p-4">
    <div class="card">
    <div class="spacer"></div>
    <div class="pader">
        <Stepper on:step={onStep}>
            {#each keys as key}
              <Step stepTerm='a' locked={index < keys.length - 1 && locker}>
                <svelte:fragment slot="header">{data[key].term}</svelte:fragment>
                <div class="center">
                  <div hidden class="answer">
                    {data[key].definition}
                  </div>
                  <div class="container"></div>
                  <div class="mb-6">
                    <form on:submit|preventDefault={() => check(data[key].definition)}>

                    <input type="text" id="large-input" bind:value={input} class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                  </form>
                  </div>
                  <button type="button" class="btn variant-filled" on:click={() => update()}>Hint</button>
                  <button type="button" class="btn variant-filled" on:click={() => check(data[key].definition)}>Check</button>
                </div>
                
              </Step>
              
            {/each}
            </Stepper>
            <div class="spacer"></div>
            <div class="input-group input-group-divider grid-cols-[auto_1fr_auto] rounded-container-token">
              <button class="input-group-shim">+</button>
              <textarea
                bind:value={currentMessage}
                class="bg-transparent border-0 ring-0"
                name="prompt"
                id="prompt"
                placeholder="Write a message..."
                rows="1"
              />
              <button class="variant-filled-primary">Send</button>
            </div>
            <div class="card-block">
              <div class="spacer"></div>
              <pre class="pre"></pre>
            </div>
</div>
    <div class="spacer"></div>

</div>  
</div>
</div>
<div class="bg-surface-500/30 p-4"></div>	