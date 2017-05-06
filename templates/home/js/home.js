var home = {};

window.onload = function() {
  home.setListeners();
  homeCallback.newTopicButtonClickCallback();
};

home.setListeners = function() {
  var elem = document.getElementById("new_topic_button");
  elem.addEventListener("click", homeCallback.newTopicButtonClickCallback);
  elem = document.getElementById("search_box");
  elem.addEventListener("click", homeCallback.searchBoxClickCallback);
  elem = document.getElementById("modal_window");
  elem.addEventListener("click", homeCallback.modalWindowClickCallback);
  elem = document.getElementById("other_feelings_button");
  elem.addEventListener("click", homeCallback.otherFeelingsButtonClickCallback);
};

window.onkeyup = function(e) {
  homeCallback.enterKeyUpCallback(e);
};
