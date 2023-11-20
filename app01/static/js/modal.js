$(document).ready(function() {
    $('#myModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var title = button.closest('tr').find('.title').text();
        var answer = button.closest('tr').find('.answer').text();
        var modal = $(this)
        modal.find('.modal-title').text(title);
        modal.find('.modal-body p').text(answer);
    });
});