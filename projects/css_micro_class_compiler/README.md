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

## STEP 3: refactor to use builder files
- [ ] create an optional `build.json` builder file that can be used to define class parameters
  - [python dictionary -- quickref.me](https://quickref.me/python#dictionary)
- [ ] refactor the css file(s) so that each class/selector can be easily singled out using `string.split()`
  - it's recommended to use a test file from here on out while developing
- [ ] refactor the css file(s) again to replace instances of a parameter with a parameter tag/key
  - remove any duplicate selectors while you're at it.
  - e.g:  

  original
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
  after refactor:

  ```json
  // build.json

  {
    "lg": "3rem",
    "md": "1rem",
    "sm": "0.5rem"
  }
  ```

  ```css
  /* new css file before processing */

  .text-<<{key}>> {
    font-size: <<{{value}}>>;
  }!!!
  ```

  ```css
  /* css result after processing */

  .text-lg {
    font-size: 3rem;
  }
  .text-md {
    font-size: 1rem;
  }
  .text-sm {
    font-size: 0.5rem;
  }
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
