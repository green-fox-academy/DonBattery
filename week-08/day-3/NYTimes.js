// Built by LucyBot. www.lucybot.com
var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Hungary"

function httpRequest(targetURL, apiKey)
{
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", targetURL + '&api_key=' + apiKey, true );
    xmlHttp.send(null);
    return xmlHttp;
}

function getUrls(data){
    return data['web_url'];
}

function post(url) {
    let link = document.createElement('a');
    link.href = url;
    link.innerText = "Post";
    document.getElementById('test').appendChild(link);
}

let myRequest = httpRequest(url, 'c3434139080a492f982523a8b67c5dd7')

myRequest.onload = function() {
    console.log(myRequest.responseText)    
    JSON.parse(myRequest.responseText).response.docs.map(getUrls).forEach(post);
}