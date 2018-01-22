"use strict";

const tpsURL = "http://localhost:1337";
const apiURL = "http://secure-reddit.herokuapp.com/simple";
// const pleaseURL = ;

let MyPath = apiURL;


class MightyJSON {
    
    constructor() {
        this.posts = [];        
        this.comments = [];
        this.users = [];
        this.loadAll();
    }
    
    loadData(URL) {
        let data = [];
        let MyRequester = new XMLHttpRequest();
        MyRequester.open("GET", MyPath + URL);
        MyRequester.setRequestHeader("Content-Type", "application/json");
        MyRequester.setRequestHeader("Accept", "application/json");
        MyRequester.send();
        MyRequester.onload = function () {            
            data = JSON.parse(MyRequester.response);
            console.log('Response :', MyRequester.response);
            console.log('Response Tesxt :', MyRequester.responseText);
            console.log('Data :', data);
        };
        return data;    
    }

    loadAll() {
        this.users = this.loadData('/data/users.json');
        this.posts = this.loadData('/data/posts.json');
        this.comments = this.loadData('/data/comments.json');
    }
    
    renderPosts(targetElement) {

        posts.forEach(element => {

            let postAuthor = users[this.getUserIndexByID(element['author'])];
            
            let postDiv = document.createElement('div');
            
            postDiv.className = "post";
            postDiv.id = 'post' + element['postID'];



            
            let pointBox = document.createElement('div');
            pointBox.className = "point_box";
            
            let upvoteButton = document.createElement('div');
            upvoteButton.className = "upvote_button arrow_button";
            
            let pointCounter = document.createElement('div');
            pointCounter.className = "point_counter";
            
            let downvoteButton = document.createElement('div');
            downvoteButton.className = "downvote_button arrow_button";
            
            pointBox.appendChild(upvoteButton);
            pointBox.appendChild(pointCounter);
            pointBox.appendChild(downvoteButton);
            
            postDiv.appendChild(pointBox);
            
            let avatarBox = document.createElement('div');           
            avatarBox.className = "avatar_box";
            avatarBox.innerHTML = '<img class="profilPic" src="' + postAuthor['profilPic'] + '">'
            
            postDiv.appendChild(avatarBox);
            
            let postBox = document.createElement('div');
            postBox.className = "post_box";
            
            let userName = document.createElement('div');
            userName.className = "username";
            userName.innerHTML = postAuthor['name'];
            
            let linkBox = document.createElement('div');
            linkBox.className = "link_box";
            linkBox.innerHTML = '<a href ="' + element['URL'] + '"</a>';
            
            let postText = document.createElement('div');
            postText.className = "post_text";
            postText.innerHTML = element['text'];
            
            postBox.appendChild(userName);
            postBox.appendChild(linkBox);
            postBox.appendChild(postText);
            
            postDiv.appendChild(postBox);
            
            let commentBox = document.createElement('div');     
            
            let commentCounter = document.createElement('div');           
            let commentAuthor = document.createElement('div');           
            let commentText = document.createElement('div');
            
            commentBox.appendChild(commentCounter);
            commentBox.appendChild(commentAuthor);
            commentBox.appendChild(commentText);
            
            postDiv.appendChild(commentBox);
            
            targetElement.appendChild(postDiv);
        });      
    }

    getUserIndexByID(index) {
        for (let i = 0; i < users.length; i++) {
            if (users[i]['userID'] == index) {
                return i;
            }
        }
        return -1;
    } 

}

let jsonController = new MightyJSON();

let contentBox = document.getElementById("content");

let testP = document.createElement('p');
testP.innerHTML = "TESTING!";
contentBox.appendChild(testP);

console.log('Users : ', this.users)
console.log('Posts : ', this.posts)
console.log('Comments : ', this.comments)

jsonController.renderPosts(contentBox);