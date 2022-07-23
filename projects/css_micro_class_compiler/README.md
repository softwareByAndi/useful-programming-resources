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

# STEP 5: order matters (sometimes) - refactor build.json to include the ability to specify order

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

# STEP 6: add child selectors

- [ ] refactor `build.json` to include a property for selectors
  - for this step, all we care about are direct an indirect child selectors, so this can remain simple
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
    .text-md:child > *{
      font-size: 1rem;
    }
    .text-sm:child > * {
      font-size: 0.7rem;
    }
    
    .text-lg:descendents * {
      font-size: 2rem;
    }
    .text-md:descendents *{
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
      .lg\:text-md:child > *{
        font-size: 1rem;
      }
      .lg\:text-sm:child > * {
        font-size: 0.7rem;
      }

      .lg\:text-lg:descendents * {
        font-size: 2rem;
      }
      .lg\:text-md:descendents *{
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
<hr>
<br>
<br>

# TODO:
## refactor to reduce duplicate code & increase flexibility
- [ ] split micro-class files into `micro-class builder files`:
  - pre-processor files (media queries, etc...) 
  - target selector files (child selectors, property selectors, etc...)
  - property files (min-height, gap, text, etc...)
  - parameter files:
    - size files (full, screen, 1.5, xl, 2/3, [100px], etc...)
    - position files(center, start, end, etc...)
    - etc...
- [ ] add script (python? bash?) to compile all micro-class builder files in a given folder into a single compiled-micro-classes.css:
  - `property-parameter`
    ```css
      /* `target:property-parameter` */
        .property-parameter {
          ith-property-value: parameter-value; optional-parameter-comment
          ...
        }
      /* EXAMPLES */
        
      /* px-3.5` */
      .px-3\.5 {
        padding-left: 0.875rem; /* 14px */
        padding-right: 0.875rem; /* 14px */
      }
        
      /* `px-3.5` */
      .px-3\.5 {
        padding-left: 0.875rem; /* 14px */
        padding-right: 0.875rem; /* 14px */
      }
    ```
        
  - `pre-processor:property-parameter`
    ```css
      /* `pre-processor:property-parameter` */
      @pre-processor-value {
        .pre-processor\:property-parameter {
          ith-property-value: parameter-value;
          ...
        }
      }
      /* EXAMPLE */
        
      /* `lg:px-3.5` */
      @media only screen and (min-width: 64.063em) { /* min-width 1025px, large screens */
        .lg\:px-3\.5 {
          padding-left: 0.875rem; /* 14px */
          padding-right: 0.875rem; /* 14px */
        }
      }
    ```
        
  - `target:property-parameter`
    ```css
      /* `target:property-parameter` */
        .target\:property-parameter target-selector-and-value {
          ith-property-value: parameter-value;
          ...
        }
      /* EXAMPLES */
        
      /* `child:px-3.5` */
      .child\:px-3\.5 > * {
        padding-left: 0.875rem; /* 14px */
        padding-right: 0.875rem; /* 14px */
      }
        
      /* `lg:first-child:px-3.5` */
      .first-child\:px-3\.5:first-child {
        padding-left: 0.875rem; /* 14px */
        padding-right: 0.875rem; /* 14px */
      }
    ```

  - `pre-processor:target:property-parameter`
    ```css
      /* `pre-processor:target:property-parameter` */
      @pre-processor-value {
        .pre-processor\:target\:property-parameter target-selector-and-value {
          ith-property-value: parameter-value;
          ...
        }
      }
      /* EXAMPLES */
        
      /* `lg:child:px-3.5` */
      @media only screen and (min-width: 64.063em) { /* min-width 1025px, large screens */
        .lg\:child\:px-3\.5 > * {
          padding-left: 0.875rem; /* 14px */
          padding-right: 0.875rem; /* 14px */
        }
      }
        
      /* `lg:first-child:px-3.5` */
      @media only screen and (min-width: 64.063em) { /* min-width 1025px, large screens */
        .lg\:first-child\:px-3\.5:first-child {
          padding-left: 0.875rem; /* 14px */
          padding-right: 0.875rem; /* 14px */
        }
      }
    ```
