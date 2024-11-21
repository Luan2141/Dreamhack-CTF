document.addEventListener("DOMContentLoaded", function() {
    crack();
});
function crack() {
    alert("Running");
    var currentIndex = 0;
    var currentIndexDisplay = document.getElementById("currentIndexDisplay");
    while (currentIndex <=311299) {
        var paddedPassword = String(currentIndex).padStart(6, "0");
        
       // _0x9a220(paddedPassword);
        if (check) {
            alert(currentIndex);
            break;
        }
        currentIndex++;
        // Update the display with the current index value
        currentIndexDisplay.textContent = "Current Index: " + currentIndex;
    }
    alert("Exit");
}

// Assuming _0x9a220() and check are defined elsewhere
