const myURL = "http://secure-reddit.herokuapp.com/simple"
const postURL = myURL + "/posts"

function loadData(URL) {
    
    let data = [];
    
    let MyRequester = new XMLHttpRequest;
    
    MyRequester.open("GET", URL);
    
    MyRequester.setRequestHeader("Content-Type", "application/json");
    
    MyRequester.setRequestHeader("Accept", "application/json");
    
    MyRequester.send();
    
    MyRequester.onload = function () {            
        data = JSON.parse(MyRequester.responseText);
        console.log('Response :', MyRequester.response);
        console.log('Response Tesxt :', MyRequester.responseText);
        console.log('Data :', data);
    };

    return data;   

}

console.log(loadData(postURL));



