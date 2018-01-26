function timeStampToDate(stamp) {
  return new Date(stamp * 1000).toGMTString();
}

function getPostURL(post) {
    let postURL = "http://burymewithmymoney.com/"    
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
        <img class = "avatar_pic" src = ${user['profilePicURL']} alt = "profil_pic">
    </div>  
    <div class = "post_box">        
        <div class = "username">by: ${user['name']} at: ${timeStampToDate(post[])}</div>
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
        </div>        
    </div>`
    htmlElement.appendChild(newPost);
} 