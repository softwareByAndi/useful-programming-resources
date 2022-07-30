# pokeAPI Project

project description can be viewed here: https://www.youtube.com/watch?v=FTn-yhmA-0Q&t=0s

project starter files are here: https://github.com/softwareByAndi/useful-programming-resources/blob/main/projects/pokeAPI/pokemonAPI_project_blank.zip




## Project resources

[javascript reference -- quickref.me](https://quickref.me/javascript)  
[javascript objects -- quickref.me](https://quickref.me/javascript#javascript-objects)  
[javascript arrays -- quickref.me](https://quickref.me/javascript#javascript-arrays)  
[javascript iterators -- quickref.me](https://quickref.me/javascript#javascript-iterators)  

<hr>

[javascript map -- geeksforgeeks.org](https://www.geeksforgeeks.org/javascript-array-map-method/)

<hr>

[pokeApi -- pokeapi.co](https://pokeapi.co/?ref=public-apis)  
[Javascript REST api call -- stackoverflow.com](https://stackoverflow.com/questions/36975619/how-to-call-a-rest-web-service-api-from-javascript)  
<hr>

```javascript

(
    await some_async_function(url)
)
  .map(obj => obj.data?.name)
  .filter(name => name !== undefined && name !== "")  // shorthand = .filter(name => name)
  .join(', ')
```
  
```javascript
(
    await some_async_function(url)
)
  .map(obj => obj.data)
  .filter(data => data)
  .map(async data => {
    const extra_data = (await new_query(data.nested?.url)) || {};
    return {
      x = data.x,
      y = extra_data.nested?.path.y || "not found..."
    }
  })
```
