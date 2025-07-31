<script>
    import {toc} from '/src/services/toc.js'
</script>

<style>
    a {
        @apply text-blue-700 font-semibold;
    }
    a:hover {
        @apply text-blue-300 cursor-pointer;
    }
</style>

<main class="page">
    <div class="flex flex-col gap-y-2">
        <h1>Turn a Concept Drawing into a Styled Web Page:</h1>
        <p>welcome, this style of written tutorial is a prototype, and may be a little rough.</p>
        <p>feel free to email any comments, recommendations, feature requests, &/or bug-fixes to: <a
                href="mailto:softwarebyandi@gmail.com">SoftwareByAndi@gmail.com
        </a></p>
    </div>

    <h2 class="mt-6">Table of Contents:</h2>
    <div class="flex flex-col gap-y-1">
        {#each toc as [page, title]}
            <a href="{page}">{title}</a>
        {/each}
    </div>
</main>

<footer>
    <p>feel free to email any comments, recommendations, feature requests, &/or bug-fixes to: <a
            href="mailto:softwarebyandi@gmail.com">SoftwareByAndi@gmail.com
    </a></p>
</footer>