var homeCallback = {};

homeCallback.handleSendTopicResponseCallback  = function(reply) {
  console.log(reply);
};

homeCallback.handleGetTopicResponsesCallback = function(reply) {
  if (reply.length === 0) {
    var text = "Hm... Seems like there no responses to this topic. Be the first!";
    document.getElementById("topic_responses_wrapper").innerHTML = "";
    document.getElementById("no_content_text").innerText = text;
    document.getElementById("no_content_wrapper").style.display = "block";
    return;
  }

  document.getElementById("topic_responses_wrapper").innerHTML = reply;

  var likeButtons = document.getElementsByClassName("like_button");
  var dislikeButtons = document.getElementsByClassName("dislike_button");
  for (var i = 0; i < likeButtons.length; i++) {
    var likeButton = likeButtons[i];
    var dislikeButton = dislikeButtons[i];
    likeButton.addEventListener("click",
      homeCallback.likeButtonClickCallback);
    dislikeButton.addEventListener("click",
      homeCallback.dislikeButtonClickCallback);
  }
};

homeCallback.handleLikeDislikeTopicResponseCallback = function(reply) {
  // var statusObject = JSON.parse(reply);
  console.log(reply);
};

homeCallback.handleGetRandomTopicCallback = function(reply) {
  console.log(reply);
  var data = JSON.parse(reply);
  var topicObject = data.topic_list[0];
  document.getElementById("topic").innerText = topicObject.topic;
};

homeCallback.handleGetSearchResultsCallback = function(reply) {
  document.getElementById("search_results_wrapper").innerHTML = reply;

  var resultTexts = document.getElementsByClassName("search_result_text");
  for (var i = 0; i < resultTexts.length; i++) {
    var paragraphElem = resultTexts[i];
    paragraphElem.addEventListener("click",
      homeCallback.searchResultTextClickCallback);
  }
};

homeCallback.likeButtonClickCallback = function(event) {
  topicResponseElem = helper.findAncestor(event.target, "topic_response");
  homeHandler.handleLikeDislikeTopicResponse(topicResponseElem.id, "like");
};

homeCallback.dislikeButtonClickCallback = function(event) {
  topicResponseElem = helper.findAncestor(event.target, "topic_response");
  homeHandler.handleLikeDislikeTopicResponse(topicResponseElem.id, "dislike");
};

homeCallback.newTopicButtonClickCallback = function(event) {
  homeHandler.handleGetRandomTopic();
};

homeCallback.otherFeelingsButtonClickCallback = function(event) {
  var topic = document.getElementById("topic").innerText;
  document.getElementById("modal_window").style.display = "block";
  document.getElementById("topic_responses_wrapper").style.display = "block";
  document.getElementById("search_box").disabled = true;
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
  document.getElementById("no_content_wrapper").style.display = "none";
  document.getElementById("search_results_wrapper").style.display = "none";
  document.getElementById("topic_responses_wrapper").style.display = "none";
  document.getElementById("search_box").value = "";
  document.getElementById("search_box").disabled = false;
  document.getElementById("modal_window").style.display = "none";
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
