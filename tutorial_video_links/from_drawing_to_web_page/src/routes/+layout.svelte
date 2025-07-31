<script>
    import "../app.css";
    import "../globals.css"
    import "../nav.css"

    import { toc } from "../services/toc.js"
</script>

<header class="px-4 py-1 bg-neutral-500">
    <nav class="flex flex-wrap gap-x-8 gap-y-1 ">
        <a class="text-neutral-900 hover:text-neutral-200" href="/">home</a>
    </nav>
</header>


<slot />

<footer class="flex flex-col px-4 py-16 justify-center items-center bg-neutral-400 text-neutral-900">
    <p>feel free to email any comments, recommendations, feature requests, &/or bug-fixes to:</p>
    <a class="text-neutral-900 hover:text-neutral-200"
            href="mailto:softwarebyandi@gmail.com">SoftwareByAndi@gmail.com
    </a>
</footer>