
var Url = document.getElementById('urlcopied').href;
console.log(Url);
document.getElementById("inputUrl").value = Url;
function copyURL() {
    var inputUrl = document.getElementById("inputUrl");
    inputUrl.select();
    document.execCommand("copy");
}

