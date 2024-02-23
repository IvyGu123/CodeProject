---
marp : true
---

# Lecture 5: Web Storage And The lifecycle of an HTML page 

---

## Life Cycle of a Web Page
The lifecycle of an HTML page has three important events:
- `DOMContentLoaded` event
- `load` event
- `beforeunload/unload` event

---

## Onload Event
```js
window.onload = function() { // can also use window.addEventListener('load', (event) => {
  alert('Page loaded');
};
```

---

## Web Storage

Session Storeage...

---

## Homework

1. Make the `login` page more beautiful (CSS)
2. Display the user's name on the `home` page (localStorage) (DomContentLoaded,load)
3. Make the `buy` and `cancel` button into the `cardview` (Html, CSS)
<<<<<<< HEAD
=======

---

## Display(CSS)

### Flex

- Center
  - The items are packed flush to each other toward the center of the alignment container along the main axis.
- Right
- Left
- Space-between
  - The items are evenly distributed within the alignment container along the main axis. The spacing between each pair of adjacent items is the same. The first item is flush with the main-start edge, and the last item is flush with the main-end edge.
- Space-around

---

## Center the elements

```css
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---
>>>>>>> 88e47e1 (Initial commit)
