var is_menu_visible = false

$("#small_profile_menu").click(function() {
    if (is_menu_visible == false) {
        $(".mini-profile-menu").css("display", "block");
        is_menu_visible = true
    } else {
        $(".mini-profile-menu").css("display", "none");
        is_menu_visible = false
    }
});