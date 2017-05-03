var homeCallback = {};

homeCallback.handleSendTopicResponseCallback  = function(reply) {
  console.log(reply);
};

homeCallback.handleGetTopicResponsesCallback = function(reply) {
  console.log(reply);
};

homeCallback.handleGetRandomTopicCallback = function(reply) {
  var data = JSON.parse(reply);
  var topic_object = data.topic_list[0];
  document.getElementById("topic").innerText = topic_object.topic;
}

homeCallback.handleGetSearchResultsCallback = function(reply) {
  var data = JSON.parse(reply);
  var topic_object_list = data.topic_list
  console.log("----------------------------");
  for (var i = 0; i < topic_object_list.length; i++) {
    console.log(topic_object_list[i].topic);
  }
  console.log("----------------------------");
}

homeCallback.newTopicButtonClickCallback = function(event) {
  homeHandler.handleGetRandomTopic();
}

homeCallback.enterKeyUpCallback = function(e) {
  var key = e.keyCode ? e.keyCode : e.which;
  var activeElement = document.activeElement;

    if (key === 13) { // Enter key
      if (activeElement.id === "response") {
        var text = document.getElementById("response").value;
        homeHandler.handleSendTopicResponse(text);
        document.getElementById("response").value = "";
      } else if (activeElement.id === "search_box") {
        var text = activeElement.value;
        if (text.length == 0)
          return;
        homeHandler.handleGetSearchResults(text);
        activeElement.value = "";
      }
    } else {
      if (activeElement.id === "response") {
        var input = activeElement;
        var text = input.value;
        if (text.split(" ").length > 5) {
          input.style.backgroundColor = "red";
        } else {
          input.style.backgroundColor = "";
        }
      } else if (activeElement.id === "search_box") {
        var text = activeElement.value;
        if (text.length == 0)
          return;
        homeHandler.handleGetSearchResults(text);
      }
    } // end if block
};
