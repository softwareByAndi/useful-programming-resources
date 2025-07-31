<script>
    import { toc } from '/src/services/toc.js'
    let next = toc.get(1);
    next = {
        href: next[0],
        label: next[1]
    }
    import Prev_Next from "$lib/Prev_Next.svelte";
</script>

<div class="flex flex-col lg:flex-row gap-2 page">
    <h2>Step 1: Draw Wrappers</h2>
    <p>break down your concept reference elements into wrappers</p>

    <figure class="image-wrapper">
        <figcaption>source reference</figcaption>
        <img src="/src/assets/page-screen-snippet.png" alt="concept reference">
    </figure>

    <figure class="image-wrapper">
        <figcaption>broken down into wrappers</figcaption>
        <img src="/src/assets/page-breakdown.png" alt="broken into wrappers">
    </figure>

    <Prev_Next next={next}/>

</div>