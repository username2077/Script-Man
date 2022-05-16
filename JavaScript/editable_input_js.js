function editable(iptidx) {
    // select
    //$('input[id="'+iptidx+'"]').prop("checked",true);
    //change
    var tmpval=$('input[sid="'+iptidx+'"]').val();
    $('input[id="'+iptidx+'"]').val(tmpval);
}

function checkipt(iptidx) {
        // select
    $('input[id="'+iptidx+'"]').prop("checked",true);
    }

function input_reset(iptsid) {
    var tmpval = $('input[sid="'+iptsid+'"]').attr("dft_value");
    // alert(tmpval);
    $('input[sid="'+iptsid+'"]').val(tmpval);
    $('input[id="'+iptsid+'"]').val(tmpval);
}