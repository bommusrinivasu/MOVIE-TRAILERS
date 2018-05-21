#!/usr/bin/env python
import webbrowser
import os
import re
print("Content-type:text/html \n")

main_page_head = '''
<!DOCTYPE html>
<html>
<head >
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Movie trailers</title>

   <style>

    .style {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top:100px;
    left: 0;
    top: 0;
    width:100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}
body {
            padding-top: 80px;
            background-image: url("http://wallpapercave.com/wp/m9dpOvQ.jpg");
        }

.style-content {
    margin: 5% auto; /* 5% from the top and centered */
    padding: 20px;
    width: 60%; /* Could be more or less, depending on screen size */
    min-height:315px;
}

/* The Close Button */
.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    background-color: black;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}
      .container{
        display:flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
       }
     .box{
          width:100%;
          min-height:150px;
          cursor:pointer;
        }
      @media screen and (min-width :450px)  {
      div.v1:hover{
             border:1px;
             background-color:skyblue;
             }
       div.v2:hover{
             border:1px;
             background-color:skyblue;
             }
       div.v3:hover{
             border:1px;
             background-color:skyblue;
             }
       div.v4:hover{
             border:1px;
             background-color:skyblue;
             }
       div.v5:hover{
            border:1px;
             background-color:red;
             }
       .v1{width:40%;}
       .v2{width:40%;}
       .v3{width:40%;}
       .v4{width:40%;}
       .v5{width:40%;}

      h1{
         background-color:none;
         font-family:arial,cursive;
         }

    }
    </style>
   <div>
         <div id="myStyle" class="style">

           <div class="style-content">
                <span class="close">&times;</span>
   <iframe id="f" width="100%" height="315" src=""
    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
          </div>

        </div>
</div>

   <script>
   // Get the style
var style = document.getElementById('myStyle');

// Get the <span> element that closes the style
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the style
    onc = function(c) {
    style.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("f").setAttribute("src",c);
}

// When the user clicks on <span> (x), close the style
    span.onclick = function() {
        style.style.display = "none";
}
// When the user clicks anywhere outside of the style, close it
   window.onclick = function(event) {
       if (event.target == style) {
          style.style.display = "none";
    }
}
span.onclick = function(){
            console.log("hello");
            var iframe = document.getElementById("f");
            iframe.src = iframe.src;
            style.style.display = "none";
        }

</script>
</head>
'''
main_page_content = '''
<body style="text-align:center">
   <em><h1 style="color:black">MOVIE TRAILERS</h1></em>
   <p style="color:white">Click on the below images to play trailers</p>
   <div class="container">
   <div class="box v1" onclick="onc('97h9fBWltBM')"> <img vspace="30"
    src="https://bit.ly/2rXfjO0"style="width:60%" height="300"
    hspace="30"> <h2 style="color:white;">Agnatavasi</h2></div>
   <div class="box v2" onclick="onc('sueMmTm-M4Y')"> <img vspace="30"
   src="https://bit.ly/2IyLI8z" style="width:60%" height="300" hspace="30">
  <h2 style="color:white;">Rangastalam</h2></div>
  <div class="box v3" onclick="onc('KMWS5y2gZ6E')"> <img vspace="30"
   src="https://bit.ly/2s0hosm" style="width:60%" height="300" hspace="30">
   <h2 style="color:white;">Bharat ane nenu</h2></div>
   <div class="box v4" onclick="onc('vWD6kUP9RTY')">
   <img vspace="30" src="https://bit.ly/2IZxA85"style="width:60%"
    height="300"hspace="30">
    <h2 style = "color:white; ">Gang</h2></div>
    <div class="box v5" onclick="onc('W5MZevEH5Ns')"> <img vspace="30"
   src="https://bit.ly/2IRCCTZ" style="width:60%" height="300"  hspace="30">
  <h2 style = "color:white;">Jab harry met segal</h2></div>
</body>

</html>
'''
movie_tiles_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center"
data-trailer-youtbe-id="{trailer_youtube_id}"
data-toggle="style" data-target="#trailer">
     <img src="{poster_image_url}" width="220" height="342">
     <h2 style="color:white;">{movie_title}</h2>
    </div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        content+= movie_tiles_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
         )
        return content


def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')

    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    output_file.write(main_page_head+rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
