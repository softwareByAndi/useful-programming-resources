<script>
    const _default = {
        href: "/",
        label: "home"
    };
    export let next = _default;
    export let prev = _default;
</script>

<style>
    .nav-buttons {
        @apply my-8 flex justify-around hover:opacity-70;
    }
    .nav-buttons>a {
        @apply bg-blue-100 rounded-full px-6 py-1 border-2 border-blue-600;
    }
</style>

<nav class="nav-buttons">
    {#each [next, prev] as {href, label}}
        <a href="{href}">
            Next -- {label} -->
        </a>
    {/each}
</nav>

