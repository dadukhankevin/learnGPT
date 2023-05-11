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
        
                const words = text.split(/\s+/).filter(word => word.length > 0);
                for (const word of words) {
                    console.log(word)
                    const span = document.createElement("span");
                    span.className = "word";
                    span.textContent = " "+word;
                    const fadeInSpeed = Math.floor(Math.random() * 10000);
                    // span.style.animationDelay = fadeInSpeed + "ms";
                    const fadeOutSpeed = Math.floor(Math.random() * 20000);
                    const container = answerElement.nextElementSibling;
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
        onMount(update);
</script>
<div class="h-full grid grid-rows-[auto_1fr_auto] gap-1">

	<div class="bg-surface-500/30 p-4"></div>
	<div class="bg-surface-500/30 p-4">
    <div class="card">
    <div class="spacer"></div>
    <div class="pader">
    <Stepper>
        <Step locked={locker}>
            <svelte:fragment slot="header">What is the meaning of life, the universe, and everything?
            </svelte:fragment>
            <div class="center">
              <div hidden class="answer">
                test
              </div>
              <div class="container"></div>
              <div class="mb-6">
                <input type="text" id="large-input" on:change = {() => check(document.querySelector(".answer")?.innerHTML ?? "")} class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              </div>
              <button type="button" class="btn variant-filled" on:click = {() => check(document.querySelector(".answer")?.innerHTML ?? "")}>Check</button>
            </div>
          </Step>
          
	<Step></Step>
	<!-- ... -->
    </Stepper>
</div>
    <div class="spacer"></div>

</div>  
</div>
</div>
<div class="bg-surface-500/30 p-4"></div>	