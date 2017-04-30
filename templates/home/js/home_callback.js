var homeCallback = {};

homeCallback.handleSendTopicResponseCallback  = function(reply) {
  console.log(reply);
};

homeCallback.handleGetTopicResponsesCallback = function(reply) {
  console.log(reply);
};

homeCallback.enterKeyUpCallback = function(e) {
  var key = e.keyCode ? e.keyCode : e.which;
  var activeElement = document.activeElement;

    if (key === 13) { // Enter key
      if (activeElement.id === "response") {
        document.getElementById("response").value = "";
        var text = document.getElementById("response").value;
        homeHandler.handleSendTopicResponse(text);
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
      }
    } // end if block
};
