window.Superlists = {};
window.Superlists.initialize = () => {
    $('input[name="text"]').on('keypress', () => {
        $('.alert-danger').hide()
    });
};
