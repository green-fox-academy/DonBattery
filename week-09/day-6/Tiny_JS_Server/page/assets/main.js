"use strict";

const myURL = "http://localhost:1337";
const testURL = "http://secure-reddit.herokuapp.com/simple";
const LeviURL = "https://time-radish.glitch.me/posts";

let users = [];
let posts = [];
let comments = [];

users = [
    {
        'name' : 'Sanya'
    }
];

let contentBox = document.getElementById("content");

function getUserIndexByID(index) {
    for (let i = 0; i < users.length; i++) {
        if (users[i]['userID'] == index) {
            return i;
        }
    }
    return -1;
} 

function loadData(URL) {
    let data = [];
    let MyRequester = new XMLHttpRequest();
    MyRequester.open("GET", URL);
    MyRequester.setRequestHeader("Content-Type", "application/json");
    MyRequester.setRequestHeader("Accept", "application/json");
    MyRequester.send();
    MyRequester.onload = function () {            
        posts = JSON.parse(MyRequester.responseText).posts;
        console.log(posts);
        posts.forEach(post => renderPost(users[getUserIndexByID(post['author'])], post, contentBox))
    }   
}

function loadAll(URL) {
    // this.users = this.loadData('/data/users.json');
    loadData(URL);
    // this.comments = this.loadData('/data/comments.json');
}
   
function timeStampToDate(stamp) {
    return new Date(stamp).toGMTString();
}
      
function getPostURL(post) {
    let postUrl = "http://burymewithmymoney.com/"    
    if ("url" in post){
        postUrl = post["url"];
    } else if ("href" in post) {
        postUrl = post["href"];
    }
}
      
function renderPost(user, post, htmlElement) {
    let newPost = document.createElement('div');
    newPost.id = "postID" + post['id'];
    newPost.classList = "post"
    newPost.innerHTML = `                 
        <div class = "point_box">
            <div class = "upvote_button arrow_button">▲</div>
            <div class = "point_counter">${post['score']}</div>
            <div class = "downvote_button arrow_button">▼</div>
        </div>  
        <div class = "avatar_box">
            <img class = "avatar_pic" src = "https://pbs.twimg.com/profile_images/824716853989744640/8Fcd0bji.jpg" alt = "profil_pic">
        </div>  
        <div class = "post_box">        
            <div class = "username">by: ${user['name']} on: ${timeStampToDate(post['timestamp'])}</div>
            <div class = "link_box">
                <a href = >${getPostURL(post)}</a>
            </div>        
        <div class = "post_text">
            ${post['title']}
        </div>        
        <div class = "comment_box">
            <div class = "comment_counter"></div>
            <div class = "comment_author"></div>
            <div class = "comment_text"></div>
        </div>`
    htmlElement.appendChild(newPost);
}

loadAll(LeviURL);

setTimeout(logger, 1000);

function logger() {
    console.log('Users : ', users)
    console.log('Posts : ', posts)
    console.log('Comments : ', comments)
}
    
