
function myfun(pram) {
    var pic;

    if(pram == 0)
    {
        pic="../images/0.jpg";
    }
    else if(pram == 1)
    {
        pic="../images/1.jpg";
    }
    else if(pram == 2)
    {
        pic="../images/2.jpg";
    }
    else if(pram == 3)
    {
        pic="../images/3.jpg";
    }
    else if(pram == 4)
    {
        pic="../images/4.jpg";
    }
    else if(pram == 5)
    {
        pic="../images/5.jpg";
    }
    else if(pram == 6)
    {
        pic="../images/6.jpg";
    }
    else if(pram == 7)
    {
        pic="../images/7.jpg";
    }
    else if(pram == 8)
    {
        pic="../images/8.jpg";
    }
    else {
        pic="../images/0.jpg";
    }
    document.getElementById("main-img").src=pic;
}