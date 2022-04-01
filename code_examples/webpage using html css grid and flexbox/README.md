# Video tutorial for this code can be found here:
[implementing a webpage using css grid and flex box -- youtube](https://www.youtube.com/watch?v=WSVBw0l7knc)

as a note, If I could go back, I would have done this tutorial a bit differently, using:  
```css
grid-template-columns: 2rem 5fr 2fr 3fr 2rem
```
<br>

# Notes:
- [`fox.png`](https://github.com/softwareByAndi/useful-programming-resources/blob/main/code_examples/webpage%20using%20html%20css%20grid%20and%20flexbox/fox.png) is not my image. I stole it from ['blue fox on Muro' by doddlefurr - deviantart.com](https://www.deviantart.com/doddlefur/art/blue-fox-on-Muro-302282804)
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
