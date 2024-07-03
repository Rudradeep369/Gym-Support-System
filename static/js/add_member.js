$(document).ready(function () {
    var current = 0;
    var fields = $("fieldset");

    function showField(index) {
        fields.removeClass("active").eq(index).addClass("active");
    }

    $(".next").click(function () {
        if (current < fields.length - 1) {
            current++;
            showField(current);
        }
    });

    $(".prev").click(function () {
        if (current > 0) {
            current--;
            showField(current);
        }
    });

    showField(current);
});