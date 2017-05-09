var homeHandler = {};

homeHandler.handleSendTopicResponse = function(response) {
  var topic = document.getElementById("topic").innerText;
  var arr = response.split(" ");
  if (arr.length <= 5 && arr.length > 0) {
    var data = {
      "topic": topic,
      "response": response
    };

    var requestPackage = {
      "request_type": homeDefine.INSERT_TOPIC_RESPONSE,
      "data": JSON.stringify(data)
    };

    var params = helper.constructURLParams(requestPackage);
    var url = window.location.origin + "/?" + params;
    helper.httpPostAsync(url, homeCallback.handleSendTopicResponseCallback);
  }
};

homeHandler.handleGetTopicResponses = function(topic) {
  if (topic.length > 0) {
    var data = {
      "topic": topic,
    };

    var requestPackage = {
      "request_type": homeDefine.GET_TOPIC_RESPONSES,
      "data": JSON.stringify(data)
    };

    var params = helper.constructURLParams(requestPackage);
    var url = window.location.origin + '/?' + params;
    helper.httpGetAsync(url, homeCallback.handleGetTopicResponsesCallback);
  }
};

homeHandler.handleLikeDislikeTopicResponse = function(id, type) {
  var data = {
    "uuid": id
  };

  var requestType = "";
  if (type === "like")
    requestType = homeDefine.LIKE_TOPIC_RESPONSE;
  else if (type === "dislike")
    requestType = homeDefine.DISLIKE_TOPIC_RESPONSE;
  else
    return

  var requestPackage = {
    "request_type": requestType,
    "data": JSON.stringify(data)
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + '/?' + params;
  helper.httpPostAsync(url,
    homeCallback.handleLikeDislikeTopicResponseCallback);
};

homeHandler.handleGetRandomTopic = function() {
  var requestPackage = {
    "request_type": homeDefine.GET_RANDOM_TOPIC,
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + '/?' + params;
  helper.httpGetAsync(url, homeCallback.handleGetRandomTopicCallback);
};

homeHandler.handleGetSearchResults = function(searchString) {
  var data = {
    "search_string": searchString,
  };

  var requestPackage = {
    "request_type": homeDefine.GET_SEARCH_RESULTS,
    "data": JSON.stringify(data)
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + '/?' + params;
  helper.httpGetAsync(url, homeCallback.handleGetSearchResultsCallback);
};
