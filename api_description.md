# APIs description
This document define the 3 rest APIs: user, post and comment.

## Users
- get: /users => return the total number of users
- post: /users => create a new user
    by providing "Name" and "Password", JSON encoded
- post: /user => identify a user, return jwt if identified
    by providing "Name" and "Password", FORM encoded

## Comments
- get: /comments => return the total number of comments
- post: /comments => return every comments of a post
    by providing "postId", JSON encoded
- post: /comment => create a new comment
    by providing "PostId", "Value" and "jwt", FORM encoded

## Post
- get: /show_posts => return every posts stored in database (with id, name, content and datum)
- post: /add_post => crate a new post
    by providing "post" and "jwt", FORM encoded
