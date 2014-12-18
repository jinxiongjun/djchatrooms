/**
 * Created with PyCharm.
 * User: mzh
 * Date: 14-12-8
 * Time: 下午3:50
 * To change this template use File | Settings | File Templates.
 */

;
(function () {
    function login() {
        $.ajax({
            url: "/chat/login/",
            type: "post",
            dataType: 'json',
            data: $("#loginForm").serialize(),
            success: function (data) {
//                var jsonObject = $.jsonToObject(data);
//                var tt = '';
//                $.each(jsonObject, function (k, v) {
//                    tt += k + "：" + v + "<br/>";
//                });
                if (data == "login_failed") {
                    $("#login_message").hide("fast");
                    $("#login_message").show("slow");
                } else if (data == "login_success") {
                    location.href = "/chat/rooms"
                }
            },
            cache: false,
            timeout: 5000,
            error: function () {
                alert("timeout");
            }
        });
    }

    $("#loginForm").bind("keypress", function (e) {
        if (13 == e.keyCode) {
            login();
        }
    });
    $("#login").bind("click", login)


    function register() {
        $.ajax({
            url: "/chat/register/",
            type: "post",
            dataType: 'json',
            data: $("#registerForm").serialize(),
            success: function (data) {
//                var jsonObject = $.jsonToObject(data);
//                var tt = '';
//                $.each(jsonObject, function (k, v) {
//                    tt += k + "：" + v + "<br/>";
//                });
                if (data == "user_exist") {
                    $("#register_message").hide("fast");
                    $("#register_message").show("slow");
                } else if (data == "login_success") {
                    location.href = "/chat/rooms"
                }
            },
            cache: false,
            timeout: 5000,
            error: function () {
                alert("timeout");
            }
        });
    }

    $("#registerForm").bind("keypress", function (e) {
        if (13 == e.keyCode) {
            register();
        }
    });
    $("#register").bind("click", register);

    $(window).resize(function () {
         $("#rooms-list").height(document.body.clientHeight - 52);
    });
    $("#rooms-list").height(document.body.clientHeight - 52);
})();
