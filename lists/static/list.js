const initialize =

window.Superlists = {};
window.Superlists.initialize = () => {
    $('input[name="text"]').on('keypress', () => {
        console.log('in keypress handler');
        $('.alert-danger').hide()
    });
};
