function addCookie(name, value, expiration) {
    var i = "";
    if (expiration) {
        var date = new Date();
        date.setTime(date.getTime() + (expiration * 48 * 60 * 60 * 1000));
        i = "; expiration=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + i + "; path=/";  
}

function getCookie(name) {
    n = name + "=";
    var cookie = document.cookie.split(";");
    for (i = 0; i < cookie.length; i++) {
        var c = cookie[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(n) == 0) {
            return c.substring(n.length, c.length);
        }
    }
    return "";
}

function deleteCookie(name) {
    document.cookie = name + "=; Max-Age=-999999999999;";
}

// à ajouter à toutes les pages : redirection
// if (getCookie('login') != 'OK') {
//     window.location.href = "/";
//   }