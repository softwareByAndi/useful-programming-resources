# CSS Micro Class Compiler Project

this project aims to build a compiler for constructing a large amount of custom css micro classes using a maintainable and scalable structure

<br>
<hr>
<br>

# ITERATIVE DEVELOPMENT STEPS
each of these steps are aimed to produce a complete & functional compiler of increasing complexity

<br>

## STEP 1: MVP - bare minimun  

- [ ] ability read & write files  
  - [python file handeling -- quickref.me](https://quickref.me/python#python-file-handling)  
- [ ] read all files in a given directory & concatenate them into a single super file  
  - [python strings -- quickref.md](https://quickref.me/python#python-strings)
  - [python read all files in given directory -- stackoverflow.com](https://stackoverflow.com/questions/26695903/python-how-to-read-all-files-in-a-directory)  

<br>
<br>

## STEP 2: nested file structures  

- [ ] refactor step 1 to work with nested file structures  
  - [python check if file is path or directory -- pythonexamples.org](https://pythonexamples.org/python-check-if-path-is-file-or-directory/)  

<br>
<br>

## STEP 3: refactor to use builder files & remove redundant code

- [ ] create an optional `build.json` builder file that can be used to define class parameters
  - [python dictionary -- quickref.me](https://quickref.me/python#dictionary)
  - for example:
      ```json
      // build.json
      {
        "lg": "2rem",
        "md": "1rem",
        "sm": "0.7rem"
      }
      ```

- [ ] refactor the css file(s) so that each class/selector can be easily singled out using `string.split()`. 
  - for example: `css_selectors = css_file.split('!!!');`
  - *( another option is to have a single file for each class.... )*
  - it's recommended to use a test file from here on out while developing

- [ ] refactor the css file(s) again to replace instances of a parameter with some sort of tag. 
  - for example:    
    ```css
    .text-<<{key}>> {
      font-size: <<{{value}}>>;
    }!!!
    ```
  - another example:
    ```css
    .px-<<{key}>> {
      padding-left: <<{{value}}>>;
      padding-right: <<{{value}}>>;
    }!!!
    ```
  - remove any duplicate selectors while you're at it.

- [ ] split the css file to get each selector
- [ ] for each class/selector & for each key in the build.js file, append an instance of the selector template where the key tag is replaced with the build key and value tag is replaced with the build value for the given key.
  - the output for the `build.json` and the `text_size.css.template` files should look like this:
    ```css
    .text-lg {
      font-size: 2rem;
    }
    .text-md {
      font-size: 1rem;
    }
    .text-sm {
      font-size: 0.7rem;
    }
    ```

<br>
<br>

## STEP 4: refactor to include media queries
- [ ] refactor the `build.json` file to include optional media queries
  - for example:
    ```
    {
      "media_queries": {
        "lg": "only screen and (min-width: 64.063em)"
        "md": "only screen and (min-width: 40.063em)"
      },
      "params": {
        "lg": "2rem",
        "md": "1rem",
        "sm": "0.7rem"
      }
    }
    ```
- [ ] the `build.json` file above should produce the following output  

  *notice the automatic additions of:* `@media`, `\:`, `{`, `}`, *and* `indentation` *for the media query entries*   
  
  - media queries should only be processed for classes. not for ids or anything else.  
    *also notice that* `lg\:` *and* `md\:` *are added after the `.` selector and before the selector name.*  
  
  - input
    ```css
    .text-<<{key}>> {
      font-size: <<{{value}}>>;
    }!!!
    ```
  - output
    ```css
    .text-lg {
      font-size: 2rem;
    }
    .text-md {
      font-size: 1rem;
    }
    .text-sm {
      font-size: 0.7rem;
    }
    
    @media only screen and (min-width: 64.063em) {
      .lg\:text-lg {
        font-size: 2rem;
      }
      .lg\:text-md {
        font-size: 1rem;
      }
      .lg\:text-sm {
        font-size: 0.7rem;
      }
    }
    
    @media only screen and (min-width: 40.063em) {
      .md\:text-lg {
        font-size: 2rem;
      }
      .md\:text-md {
        font-size: 1rem;
      }
      .md\:text-sm {
        font-size: 0.7rem;
      }
    }
    ```

<br>
<br>

## STEP 5: order matters (sometimes) - refactor build.json to include the ability to specify order

notice in the previous file, that the .md: media query comes after the .lg: media query. Since in this particular example, the md query is always active when the lg query is; so the md query classes will overwrite lg query classes if an element contains both of them. we don't want this. 

Since we cannot control which order a dictionary's elements are indexed, we need to add an aditional property to specify which items should be written in which order.  

### there are a few ways we can do this:  

1. do it your own way. there are a number of valid solutions to this. tackle it in any way you want.
    
2. add an number to the key and simply remove it when processing
  - e.g.
    ```
    {
      "media_queries": {
        "1_sm": ...,
        "2_md": "only screen and (min-width: 40.063em)"
        "3_lg": "only screen and (min-width: 64.063em)"
      },
      "params": {
        "3_lg": "2rem",
        "2_md": "1rem",
        "1_sm": "0.7rem"
      }
    }
    ```
    
3. turn the value from a string to a dictionary and add an `order` property
  - if the order doesn't matter, then the value can be a string instead
  - e.g.
    ```
    {
      "media_queries": {
        "lg": {
          "order": 3,
          "value": "only screen and (min-width: 64.063em)"
        },
        "md": {
          "order": 2,
          "value": "only screen and (min-width: 40.063em)"
        }
      },
      "params": {
        "3_lg": "2rem",
        "2_md": "1rem",
        "1_sm": "0.7rem"
      }
    }
    ```

    
<br>
<br>

## STEP 6: add child selectors

- [ ] refactor `build.json` to include a property for selectors
  - for this step, all we care about are direct an indirect child selectors, so this can remain simple  
    *notice the automatic additions of:* `*` *for the media query entries*   
    *also notice that the media queries also include entries for the selectors. (if they do not, then refactor that part of your code)*
  - e.g.  
    ```
    {
      "media_queries": {...},
      "params": {...},
      
      "selectors": {
        "child": " > ",       // direct children
        "descendents": " ",   // all children, nested or not
      }
    }
    ```
    
    
- [ ] the `build.json` file above should produce the following output 

  - input
    ```css
    .text-<<{key}>> {
      font-size: <<{{value}}>>;
    }!!!
    ```
  - output
    ```css
    .text-lg {
      font-size: 2rem;
    }
    .text-md {
      font-size: 1rem;
    }
    .text-sm {
      font-size: 0.7rem;
    }
    
    .text-lg:child > * {
      font-size: 2rem;
    }
    .text-md:child > * {
      font-size: 1rem;
    }
    .text-sm:child > * {
      font-size: 0.7rem;
    }
    
    .text-lg:descendents * {
      font-size: 2rem;
    }
    .text-md:descendents * {
      font-size: 1rem;
    }
    .text-sm:descendents * {
      font-size: 0.7rem;
    }
    
    @media only screen and (min-width: 64.063em) {
      .lg\:text-lg {
        font-size: 2rem;
      }
      .lg\:text-md {
        font-size: 1rem;
      }
      .lg\:text-sm {
        font-size: 0.7rem;
      }

      .lg\:text-lg:child > * {
        font-size: 2rem;
      }
      .lg\:text-md:child > * {
        font-size: 1rem;
      }
      .lg\:text-sm:child > * {
        font-size: 0.7rem;
      }

      .lg\:text-lg:descendents * {
        font-size: 2rem;
      }
      .lg\:text-md:descendents * {
        font-size: 1rem;
      }
      .lg\:text-sm:descendents * {
        font-size: 0.7rem;
      }
    }
    
    @media only screen and (min-width: 40.063em) {...}
    ```
    
<br>
<br>

## STEP 7: generalize selectors  

- [ ] refactor `build.json` to generalize the selectors portion to be able to include any selector type
  - e.g. 
    ```
    {
      "media_queries": {...},
      "params": {...},
      
      "selectors": {
        "child": {            // e.g. text-size-md > *
          "selector": " > ",
          "tag": "*"
        },
        
        "descendents": {      // e.g. text-size-md *
          "selector": " ",
          "tag": "*"
        },
        
        "active": {
          "selector": ":",    // e.g. text-size-md:active
          "tag": "active"
        }
        
        "after": {
          "selector": "::",   // e.g. text-size-md::after
          "tag": "after"
        }
      }
    }
    ```
    
<br>
<br>

## STEP 8: filter unused classes for production use css file

This can actually be very simple or very complex.

- [ ] the easiest method is to rebuild the compiled css but only add a class if that class can be found in your code.
  - this is relatively straight forward: 
    1. concatenate all of your code files together into one long string
    2. simply check `if css_class_name in code`
    3. if true, then concatenate the css class details into your compiled css file
    4. otherwise skip it

- [ ] an alternative method is to use regex to obtain a list of all css classes
  - start with a test html file for this...
  - [python regex -- w3schools.com](https://www.w3schools.com/python/python_regex.asp)
  - [python uniqe -- freecodecap.org](https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/) (filter out duplicate entries)
  ```html
  <div class="text-md lg:text-lg">
    <h1>Hello world</h1>
    <p>this is a test file</p>
    <div class="text-sm:child">
      <p>this is some small text</p>
      <p>this is some more small text</p>
    </div>
  </div>
  ```
  - then use this list to filter in the same way as the previous method  


<br>
<br>


## STEP 9: dynamic compilation
Note that the first method is very easy, but the second method allows more flexibility for dynamic compilation, such as specifying specific values for a class

this step is to encorporate the ability to program dynamic variables into your classes.
- for example, the html code below:
  ```
  <p class="text-color-[#EA4A2A]> This text should be burnt orange </p>
  ```
- should **create** the following css class:
  ```
  .text-color-\[#EA4A2A\] {
    color: #EA4A2A
  }
  ```
- other examples:
  - `text-[10px]` => `.text-\[10px\] { font-size: 10px; }
  - `text-[1.3rem]` => `.text-\[1.3rem\] { font-size: 1.3rem; }
