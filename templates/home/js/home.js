var home = {};

window.onload = function() {
  home.setListeners();
  homeCallback.newTopicButtonClickCallback();
};

home.setListeners = function() {
  var elem = document.getElementById("new_topic_button");
  elem.addEventListener("click", homeCallback.newTopicButtonClickCallback);
};

window.onkeyup = function(e) {
  homeCallback.enterKeyUpCallback(e);
};
