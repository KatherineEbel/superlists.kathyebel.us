const initialize = () => {
    $('input[name="text"]').on('keypress', () => {
        console.log('in keypress handler');
        $('.alert-danger').hide()
    });
};
