// see line 36
function event_handler(event) {
    event.preventDefault();
    const target_element = event.target;
    // do stuff with target_element
}


// note that we will often need to wait until the page is 
// fully loaded before accessing any DOM elements
// we can do this by setting a handler for the `onload` event
// which is triggered when the page finishes loading.

window.onload = () => { // we don't have to accept any event parameter if we don't have any use for it.
    const element = document.getElementById("element_id");
    const element_value = element.value; // for input elements

    /**
    * there are several ways we can add an event handler to an element, 
    * the simplest and most reliable way is to use the `addEventListener()` function. 
    *
    * the basic version of this function takes two parameters:
    *    1. the name of the event (e.g. "load", "mouseover", "click", ...etc)
    *    2. the event handler function (this can be an anonymous function or a REFERENCE to an existing function)
    *
    * the addEventListener function creates a listener for the given event, and calls the 
    * referenced function whenever that event is triggered.
    *
    * note that the event handler function is also passed an event instance as a parameter, which we can use to:
    *    1. prevent default event behavior
    *    2. access the targeted DOM element for which the event was triggered
    *    3. a whole lot of other stuff too.
    */

    // we can set the handler to an existing function
    element.addEventListener("event_name", event_handler); // note we just specify the funciton name

    // or we can set the listener to an anonymous function
    element.addEventListener("event_name", (event) => {
        event.preventDefault()
        const target_element = event.target; // note that this is a constant reference. not constant data.
        // do stuff with target_element

        // ...

        // other useful code.
        const new_element = document.createElement("element_tag") // i.e. "div", "p", "a", ...etc
        new_element.style.background = "#ff4d4d" // styling set via javascript will overwrite any CSS styling 
        new_element.textContent = "text"; // for paragraph elements
        new_element.innerHTML = `<p>
          hello
          <span class="some-classes" style="color: white;">
            world
          </span>
        </p>`;

        target_element.appendChild(new_element);

        console.log("has children nodes? = ", target_element.hasChildNodes()) // returns a boolean (true or false)
        console.log("first child: ", target_element.children[0])

        target_element.removeChild(target_element.children[0])
        target_element.innerHTML = ""; // alternate way to delete all children or html content
    })
}
