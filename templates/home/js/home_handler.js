var homeHandler = {};

homeHandler.handleSendTopicResponse = function(response) {
  var topic = document.getElementById("topic").innerText;
  var arr = response.split(" ");
  if (arr.length <= 5 && arr.length > 0) {
    var data = {
      "topic": topic,
      "response": response
    };

    var request_package = {
      "request_type": homeDefine.INSERT_TOPIC_RESPONSE,
      "data": JSON.stringify(data)
    }

    var params = helper.constructURLParams(request_package);
    var url = window.location.origin + "/?" + params;
    console.log(url);
    helper.httpPostAsync(url, homeCallback.handleSendTopicResponseCallback, null);
  }
};

homeHandler.handleGetTopicResponses = function(topic) {
  if (topic.length > 0) {
    var object = {
      "request_type": homeDefine.GET_TOPIC_RESPONSES,
      "topic": topic,
    };

    var params = helper.constructURLParams(object);
    var url = window.location.origin + '/?' + params;

    helper.httpGetAsync(url, homeCallback.handleGetTopicResponsesCallback);
  }
};
