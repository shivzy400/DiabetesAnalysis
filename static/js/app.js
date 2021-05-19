$(function() {

    ("#portfolio img").click(function() {

        var src = $(this).attr("src");
        $("#frame img").attr("src" , src);
        $("#frame").fadeIn();
        $("#overlay").fadeIn();
    });

    $("#overlay").click(function() {
        $(this).fadeOut();
        $("#frame").fadeOut();
    });
});