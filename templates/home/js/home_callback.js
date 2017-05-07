var homeCallback = {};

homeCallback.handleSendTopicResponseCallback  = function(reply) {
  console.log(reply);
};

homeCallback.handleGetTopicResponsesCallback = function(reply) {
  console.log(reply);
};

homeCallback.handleLikeDislikeTopicResponseCallback = function(reply) {
  console.log(reply);
};

homeCallback.handleGetRandomTopicCallback = function(reply) {
  var data = JSON.parse(reply);
  var topic_object = data.topic_list[0];
  document.getElementById("topic").innerText = topic_object.topic;
};

homeCallback.handleGetSearchResultsCallback = function(reply) {
  document.getElementById("search_results_wrapper").innerHTML = reply;

  var result_texts = document.getElementsByClassName("search_result_text");
  for (var i = 0; i < result_texts.length; i++) {
    var paragraph_elem = result_texts[i];
    paragraph_elem.addEventListener("click",
      homeCallback.searchResultTextClickCallback);
  }
};

homeCallback.newTopicButtonClickCallback = function(event) {
  homeHandler.handleGetRandomTopic();
};

homeCallback.otherFeelingsButtonClickCallback = function(event) {
  var topic = document.getElementById("topic").innerText;
  homeHandler.handleGetTopicResponses(topic);
};

homeCallback.searchBoxClickCallback = function(event) {
  document.getElementById("search_results_wrapper").style.display = "block";
  document.getElementById("modal_window").style.display = "block";
};

homeCallback.searchResultTextClickCallback = function(event) {
  document.getElementById("topic").innerText = event.target.innerText;
  document.getElementById("search_box").value = "";
  homeCallback.modalWindowClickCallback();
};

homeCallback.modalWindowClickCallback = function(event) {
  document.getElementById("search_results_wrapper").style.display = "none";
  document.getElementById("modal_window").style.display = "none";
  document.getElementById("search_box").value = "";
};

homeCallback.enterKeyUpCallback = function(e) {
  var key = e.keyCode ? e.keyCode : e.which;
  var activeElement = document.activeElement;
  if (activeElement.id === "response") {
    var input = activeElement;
    var text = activeElement.value;
    if (key === 13) { // Enter key
      homeHandler.handleSendTopicResponse(text);
      activeElement.value = "";
    } else {
      if (text.split(" ").length > 5) {
        input.style.backgroundColor = "red";
      } else {
        input.style.backgroundColor = "";
      }
    }
  } else if (activeElement.id === "search_box") {
    var text = activeElement.value;
    if ((key >= 65 && key <= 90) || key === 8) { // A-Z or backspace
      if (text.length == 0)
        return;
      homeHandler.handleGetSearchResults(text);
    }
  }
};
