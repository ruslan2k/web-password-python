$( document ).ready(function () {
  $(".del").click(function (event) {
    var id = $(this).data("id");
    console.log(id);
    console.log(event.target);
    $.ajax({
      url: "/item/" + id,
      type: "DELETE",
      success: function (response) {
        $(event.target).parent().remove();
      },
    });
  });
});
