SERVER_URL = ''; //insert ngrok endpoint here

// FormApp.getActiveForm();

function onFormSubmit(e) {
  Logger.log(e.response.getItemResponses());
  itemResponses = e.response.getItemResponses();
  var responseData = {}; 
  for (var i = 0; i < itemResponses.length; i++) {
      var itemResponse = itemResponses[i];
      var itemTitle = itemResponse.getItem().getTitle();
      var responseValue = itemResponse.getResponse();

      // Save item response data into the JSON object
      responseData[itemTitle] = responseValue;
  }

  // Log the constructed JSON object
  Logger.log(JSON.stringify(responseData));
    
  // Example: Send the JSON data through an HTTP request
  sendDataToServer(JSON.stringify(responseData));
  
  //var formData = e.namedValues; // Get form submission values
  //sendDataToServer(formData);
}

function sendDataToServer(data) {
  const payload = {
    formdata: data
  };

  var options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload),
  };

  // Send data to Flask server
  var response = UrlFetchApp.fetch(url, options);
}


