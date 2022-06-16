
make sure to call the following command to turn compile.command into an executable:
```cmd
chmod +x compile.command
```

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
