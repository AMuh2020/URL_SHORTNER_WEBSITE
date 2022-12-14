
function qr_toggle(id) {
    console.log("IN")
    var popup = document.getElementById("popup")
    var black = document.getElementById("blackout")
    /* gets child img tag and changes its src to the src of the qr that was clicked */
    if( id === "close"){
        popup.style.display = "none"
        console.log("close")
        black.style.display = "none"
    } else {
        console.log("open")
        black.style.display = "block"
        popup.style.display = "block"
        popup.getElementsByTagName('img')[0].src = document.getElementById(id).src;
    }
}

function copy(id) {
    if (!navigator.clipboard){
        let copyText = document.getElementById(id);
        copyText.select();
        document.execCommand("copy");
    } else{
        var short_link = document.getElementById(id).innerText;
        navigator.clipboard.writeText(short_link);
    }
}

function edit(short_code) {
    var short_code_element = document.getElementById("short-code-"+short_code)
    short_code_element.innerHTML = "<input name='edit_short' type='text' autocomplete='off' value='" + short_code + "'>"
    var short_link = document.getElementById(short_code+"_link")
    var submit_btn = document.getElementById("submit-"+short_code).style.display = "inline-block"
    var temp = short_link.href;
    short_link.removeAttribute("href")
    document.getElementById("other-btns-"+short_code).style.display = "none"
}
/* create a cancel button */
function cancel(short_code) {
    
}