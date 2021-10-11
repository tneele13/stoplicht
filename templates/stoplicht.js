$(document).ready(function () {
    alert("HALLO")
    window.setInterval('refresh()', 10000);
    // Call a function every 10000 milliseconds
    // (OR 10 seconds).

    // Refresh or reload page.
    function refresh() {
        console.log("reload")
        window .location.reload();
    }

    if (document.getElementById("stoplicht").innerText == "Stoplicht hier"){
        alert("iets")
    }

    var time = new Date();
    var timeString = time.getHours()+":"+time.getMinutes()+":"+"00";
    document.getElementById("tijd").innerText = timeString;

    var beginTijden = document.getElementById("begintijd").innerText;
    var beginTijdenArray = beginTijden.split(",")

    var eindTijden = document.getElementById("eindtijd").innerText;
    var eindTijdenArray = eindTijden.split(",")

    beginTijdenArray.forEach((tijden)=>{
       if (tijden === timeString || tijden === " "+timeString){
           changeBackground("green")
       }
       console.log(tijden)
    });

    eindTijdenArray.forEach((tijden)=>{
       if (tijden === timeString || tijden === " "+timeString){
           changeBackground("red")
       }
       console.log(tijden)
    });

    function changeBackground(color){
        document.body.style.backgroundColor = color;
    }
});