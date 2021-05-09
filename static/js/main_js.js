$(document).ready(function () {

    // AOS
    AOS.init({
        duration: 700,
        easing: 'ease',
    });

    // HIDE THE MESSAGES ALERT
    $(".alert").delay(4000).slideUp(1000, function () {
        $(this).alert('close');
        $(this).removeClass('messagesModale');
    });
    

    // LANGUAGES SWICHER
    // URL
    var pathname = window.location.pathname; // Returns path only (/path/example.html)
    // var url = window.location.href;     // Returns full URL (https://example.com/path/example.html)
    var origin = window.location.origin; // Returns base URL (https://example.com)

    function removeCharacter(str) {
        let tmp = str.split("");
        return tmp.slice(3).join("");
    }

    // LANGE SWICHER
    $("#chnage-lange").change(function () {
        let lan_sel = $("#chnage-lange").val();
        switch (lan_sel) {
            case "fr":
                document.location.href = origin + removeCharacter(pathname);
                // console.log('ar pathname', pathname)
                break;
            case "ar":
                if (pathname.includes('/ar')) {
                    document.location.href = origin + "/ar" + removeCharacter(pathname);
                } else {
                    document.location.href = origin + "/ar" + pathname;
                }
                break;
        }
    });



    // DATE FIELDS
    $('#id_org_changed, #id_org_created').attr('type', 'date');

    // MODAL 
    $('#exampleModal.show').modal('show');
    $('#btn_accepted').on('click', function () {
        $('#exampleModal').removeClass('show');
        
    });
    

    // $("form#form_accept").submit(function () {
    //     $("form.confirm").find("#accept").attr("checked", true);
    // });



});