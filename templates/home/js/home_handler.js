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
    };

    var params = helper.constructURLParams(request_package);
    var url = window.location.origin + "/?" + params;
    helper.httpPostAsync(url, homeCallback.handleSendTopicResponseCallback);
  }
};

homeHandler.handleGetTopicResponses = function(topic) {
  if (topic.length > 0) {
    var data = {
      "topic": topic,
    };

    var request_package = {
      "request_type": homeDefine.GET_TOPIC_RESPONSES,
      "data": JSON.stringify(data)
    };

    var params = helper.constructURLParams(request_package);
    var url = window.location.origin + '/?' + params;
    helper.httpGetAsync(url, homeCallback.handleGetTopicResponsesCallback);
  }
};

homeHandler.handleLikeDislikeTopicResponse = function(id, type) {
  var data = {
    "uuid": id
  };

  var request_type = "";
  if (type === "like")
    request_type = homeDefine.LIKE_TOPIC_RESPONSE;
  else
    request_type = homeDefine.DISLIKE_TOPIC_RESPONSE;

  var request_package = {
    "request_type": request_type,
    "data": data
  };

  var params = helper.constructURLParams(request_package);
  var url = window.location.origin + '/?' + params;
  helper.httpGetAsync(url, homeCallback.handleLikeDislikeTopicResponseCallback);
};

homeHandler.handleGetRandomTopic = function() {
  var request_package = {
    "request_type": homeDefine.GET_RANDOM_TOPIC,
  };

  var params = helper.constructURLParams(request_package);
  var url = window.location.origin + '/?' + params;
  helper.httpGetAsync(url, homeCallback.handleGetRandomTopicCallback);
};

homeHandler.handleGetSearchResults = function(search_string) {
  var data = {
    "search_string": search_string,
  };

  var request_package = {
    "request_type": homeDefine.GET_SEARCH_RESULTS,
    "data": JSON.stringify(data)
  };

  var params = helper.constructURLParams(request_package);
  var url = window.location.origin + '/?' + params;
  helper.httpGetAsync(url, homeCallback.handleGetSearchResultsCallback);
};
