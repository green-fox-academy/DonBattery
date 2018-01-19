"use strict";

class User {
    
    constructor(userData) {
        this.userID = userData.userID;
        this.password = userData.password;
        this.name = userData.name;
        this.profilPic = userData.profilPic;
        this.permission = userData.permission;
        this.postcount = 0;
    }
    
    render(element) {        
        let userDiv = document.createElement('div');
        userDiv.className = "userDiv"
        userDiv.innerHTML += '<img class="profilPic" src="' + this.profilPic + '">' + " Username :" + this.name + " Permission:" + this.permission + " postcount:" + this.postcount;
        element.appendChild(userDiv);
        }
        
}

class Post {

    constructor(postData) {
        this.postID = postData.postID;
        this.point = postData.point;
        this.author = postData.author;
        this.title = postData.title;
        this.URL = postData.URL;
        this.text = postData.text;
        this.timestamp = Date.now();
        this.comment_counter = 0;
    }
    
    render(element) {        
        let postDiv = document.createElement('div');
        postDiv.className = "postDiv"
        postDiv.innerHTML += '<a class="postLink" href="' + this.URL + '">' + this.title + "</a>" 
        + '<div class="postText">' + "Time :" + this.timestamp + " ID :" +this.postID + " by:" + this.author + " points :" + this.point + " comments:" + this.comment_counter + " text:" + this.text; 
        element.appendChild(postDiv);
        }

}

class Comment {

    constructor(commentData) {
        this.commentID = commentData["commentID"];
        this.reference = commentData["reference"];
        this.author = commentData["author"];
        this.text = commentData["text"];
        this.timestamp = Date.now();
    }

    render(element) {        
        let commentDiv = document.createElement('div');
        commentDiv.className = "commentDiv"
        commentDiv.innerHTML += "Time :" + this.timestamp + " ID :" +this.commentID + " by:" + this.author + " refers to :" + this.reference + " comment:" + this.text;
        element.appendChild(commentDiv);
        }

    }

let testComment = new Comment(commentData[0]); // JSON.parse(commentData)
let testPost = new Post(postData[0]);
let testUser = new User(userData[0]);

let testCommentDiv = document.getElementById('testComment');
let testPostDiv = document.getElementById('testPost');
let testUserDiv = document.getElementById('testUser')

testComment.render(testCommentDiv);
testPost.render(testPostDiv);
testUser.render(testUserDiv);