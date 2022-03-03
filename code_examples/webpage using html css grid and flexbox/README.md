# Video tutorial for this code can be found here:
[implementing a webpage using css grid and flex box -- youtube](https://www.youtube.com/watch?v=WSVBw0l7knc)

<br>

# Notes:
- everything in the body should really be wrapped in another div with class="page"

i.e.:
```html
<body>
  <div class="page">
    <!-- ... page content goes here --> 
  </div>
</body>

<style>
  .page {
    width: 100%;
    max-width: 1280px;
    height: fit-content;
    min-height: 100vh;
  }
</style>
```
