'use strict'
// eats URL and API Key, returns an opened request (still need to wait for load) as on object
function httpRequest(targetURL, apiKey)
{
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", targetURL + '&api_key=' + apiKey, true );
    xmlHttp.send(null);
    return xmlHttp;
}
// from responseText.data get the image's thumbnail and medium URLs
function getUrls(data){
    return { 'small' : data.images.fixed_height_small_still['url'], 'big' : data.images.downsized_medium['url'] };
}
// based on thumbnail and medium URLs creates small images on the page and adds the on-click event to them
// to open up the bigger image
function postImg(urls) {
    let img = document.createElement('img');
    img.src = urls['small'];
    img.addEventListener("click", function () {window.open(urls['big'],"_self")});
    document.getElementById('test').appendChild(img);
}
// lets search for cat pictures on giphy
let myRequest = httpRequest('http://api.giphy.com/v1/gifs/search?q=cat', '9HVyXdXBauXw0EWYxaIksXkQFnJn1zAW') // <- ide írd be az API key-t
// when our request loads, get the URLs from the data and create images based on them
myRequest.onload = function() {
    JSON.parse(myRequest.responseText).data.map(getUrls).forEach(postImg);
}