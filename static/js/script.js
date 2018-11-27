let openForm = function (id) {
    $(`#${id}`).show()
};

let closeForm = function (id) {
    $(`#${id}`).hide()
};

let like = function (id, csrf_token) {
    $.ajax({
        url: "http://127.0.0.1:8000/like/",
        type: "POST",
        data: {
            pk: id,
            csrfmiddelwaretoken: csrf_token,
        },
        success: (response) => {

        }
    })
};