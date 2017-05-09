var helper = {};

helper.httpGetAsync = function(theUrl, callback) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          callback(xmlHttp.responseText);
  }
  xmlHttp.open("GET", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
}

helper.httpPostAsync = function(theUrl, callback) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          callback(xmlHttp.responseText);
  }
  xmlHttp.open("POST", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
}

helper.constructURLParams = function(object) {
  var someList = [];
  for (k in object) {
    someList.push(encodeURIComponent(k) + "=" + encodeURIComponent(object[k]));
  }
  return someList.join("&");
}

helper.findAncestor  = function(el, cls) {
    while ((el = el.parentElement) && !el.classList.contains(cls));
    return el;
}
