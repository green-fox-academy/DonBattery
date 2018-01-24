"use strict";

const testURL = "http://secure-reddit.herokuapp.com/simple/"
const LeviURL = "https://time-radish.glitch.me/posts"

let posts = [];

class DataLoader {
  constructor(URL){
    this.url = URL;
  }

  loadData(){
    let myRequest = new XMLHttpRequest();
    myRequest.open("GET", LeviURL, true);
    // myRequest.setRequestHeader("Content-Type", "application/json");
    myRequest.setRequestHeader("Accept", "application/json");
    myRequest.send();
    myRequest.onload = function () {
      posts = JSON.parse(myRequest.responseText).posts;
      console.log(posts);
    }
  }
}

class Renderer {
  constructor(){    
  }

  timeStampToDate(timeStamp) {
    let date = new Date(timeStamp*1000);
    let hours = date.getHours();
    let minutes = "0" + date.getMinutes();
    let seconds = "0" + date.getSeconds();
    return hours + ':' + minutes.substr(-2);
  }

  renderPost(htmlElement, postData){

    console.log("Rendering :", postData);

    let postUrl = "";
    let newTag = document.createElement('div');
    newTag.id = "post" + postData['id'];
    newTag.className = "post"

    if ("url" in postData){
      postUrl = postData["url"];
    } else if ("href" in postData) {
      postUrl = postData["href"];
    }

    let newData = `
        <div class = "feedback">
          <div class = "upvote">🡅</div>
          <div class = "score">${postData["score"]}</div>
          <div class = "downvote">🡇</div>
        </div>
        <div class = "postBody">
          <div class = "topic">${postData["title"]}</div>
          <div class = "url"><a href=${postUrl}>Link</a></div>
          <div class = "postInfo">${this.timeStampToDate(postData["timestamp"])} poster:${postData["owner"]}</div>
        </div>
      </div>
    `;

  newTag.innerHTML = newData;

  htmlElement.appendChild(newTag);

  console.log(htmlElement.innnerHTML)
  }

}


let myRenderer = new Renderer;

let myDataLoader = new DataLoader(LeviURL);

myDataLoader.loadData();

let targetHtmlElement = document.querySelector("#content");

console.log(posts);

function postPosts(){
  for (let i = 0; i < posts.length; i++){
    myRenderer.renderPost(targetHtmlElement, posts[i]);
  }
}

setTimeout(postPosts, 2000);


// console.log(targetHtmlElement);




