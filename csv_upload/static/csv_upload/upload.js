document.querySelector('#id_file').addEventListener('change', function () {
    var filename = document.querySelector("#id_file").value;
    if (/^s*$/.test(filename)) {
        document.querySelector(".file-upload").classList.remove('active');
        document.querySelector("#noFile").text("No file chosen...");
    } else {
        document.querySelector(".file-upload").classList.add('active');
        document.querySelector("#noFile").textContent = filename.replace("C:\\fakepath\\", "");
    }
});
