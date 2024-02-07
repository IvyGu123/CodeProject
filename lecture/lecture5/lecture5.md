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
