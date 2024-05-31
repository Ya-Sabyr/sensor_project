// jQuery, Popper.js, and Bootstrap JavaScript

// jQuery
var script = document.createElement('script');
script.src = "https://code.jquery.com/jquery-3.3.1.slim.min.js";
script.integrity = "sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo";
script.crossOrigin = "anonymous";
document.head.appendChild(script);

// Popper.js
var popperScript = document.createElement('script');
popperScript.src = "https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js";
popperScript.integrity = "sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1";
popperScript.crossOrigin = "anonymous";
document.head.appendChild(popperScript);

// Bootstrap
var bootstrapScript = document.createElement('script');
bootstrapScript.src = "https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js";
bootstrapScript.integrity = "sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM";
bootstrapScript.crossOrigin = "anonymous";
document.head.appendChild(bootstrapScript);
