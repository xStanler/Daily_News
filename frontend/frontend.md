# FRONTEND

## Folder Structure
.
├── images/
│   ├── logo.png
│   └── favicon.ico
├── index.html
└── style.css

## Files:
logo.png -> image of our logo
favicon.ico -> favicon of our site
index.html -> main page enhanced by htmx
style.css -> styles of index.html

## Key functionalities:
### **Attaching HTMX**
```html
<script src="https://unpkg.com/htmx.org@2.0.4"></script>

<script defer
  src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js">
</script>

```

### **Setting up style.css and favicon**
```html
<link rel="stylesheet" href="/frontend/style.css"/>
<link rel="icon" type="image/x-icon" href="/frontend/images/favicon.ico"
```

### **Attaching font from fonts.google.com**
```css
@import url('https://fonts.googleapis.com/css2?family=Iosevka+Charon:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap');
```

### **HTMX properties**
```html
<a hx-get="">       -- Sends HTTP GET/ request
<a hx-target="">    -- Specifies which element (by class or id) would be swaped with serever's response
<a hx-trigger="">   -- Specifies when the action is triggered, eg. on load after delay etc.
```

### **JavaScript functionality**
This JavaScript functions changes style of selected 'subpage'.
```javascript
function selectButton(element) {
    const currentActive = document.querySelector(".nav-btn-selected");

    if(currentActive) {
        currentActive.classList.remove("nav-btn-selected");
    }

    element.classList.add("nav-btn-selected");
}
```

