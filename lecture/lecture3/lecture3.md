---
marp : true
---

# DOM Tree

---

## The HTML DOM model is constructed as a tree of Objects
![Alt text](./assets/1.png)

---

## JS 

With the object model, JavaScript gets all the power it needs to create dynamic HTML:
- JavaScript can change all the HTML **elements** in the page
- JavaScript can change all the HTML **attributes** in the page
- JavaScript can change all the CSS styles in the page
- JavaScript can remove existing HTML elements and attributes
- JavaScript can add new HTML elements and attributes
- JavaScript can react to all existing HTML events in the page
- JavaScript can create new HTML events in the page

--- 

## What is the DOM?
The HTML DOM is a standard object model and programming interface for HTML. It defines:

- The HTML elements as objects
- The properties of all HTML elements
- The methods to access all HTML elements
- The events for all HTML elements

---

## Requirements

![Alt text](./assets/2.png)

When to click the button, the text will change to "Sold"

---

## How to fulfill the requirements?

1. Get the button element
2. Make a click event listener for the button
3. Find the text element
4. Make the button event listener to change the text

---

## Example

```html
<html>
  <head>
    <title>Book Store</title>
    <script>
      function changeText() {
        document.getElementById("text").innerHTML = "Sold";
      }
    </script>
  </head>
  <body>
    <div style="border: 1px solid #ccc;width: fit-content;">
      <img src="./assets/book.png" onclick="myFun">
      <h2 align="center">Book1</h2>
      <p style="color: red;font-size: large;margin-left: 10%;">$100</p>
      <p style="color: black;font-size: large;margin-left: 10%;" id="text">Not Sold</p>
    </div>
    <button onclick="changeText()">Buy</button>
  </body>
</html>
```

---

## Homework

1. add a button to `cancel`
2. when click the `cancel` button, make the color of the text to be `black`
3. change the title of the page