$(document).ready(function () {
    $('#filter_by').on('change', function () {
        var voucherType = $(this).val();
        if (voucherType == 'Active') {
            $('.active-voucher').show();
            $('.inactive-voucher').hide();
        }
        else if (voucherType == 'Inactive'){
            $('.active-voucher').hide();
            $('.inactive-voucher').show();
        
        }
        else {  
            $('.active-voucher').show();
            $('.inactive-voucher').show();
        }
    });
    $('#submit_search_voucher').on('click', function () {
        voucher = $('#search_voucher').val()
        if ('' != voucher) {
          $('.voucher-code').hide();
          if($('.' + voucher).length == 0) {
            window.location.href="/display?voucher=" + voucher;

            window.history.pushState('obj', 'newtitle', '/display');
          }
          else {
            $('.' + voucher).show();
          }
        } 
        else {
            $('.table').find('tr').show();
        }
    });


    $('#sendingoption').on('change', function(){
      var option = $(this).val();
      console.log(option);
      if (option == 'Email'){
        $('#email').show();
        $('#emailvoucher').show();
        $('#printvoucher').addClass('hidden');
      }
      else {
        console.log("unhidding...");
        $('#email').hide();
        $('#emailvoucher').hide();
        $('div#printvoucher').removeClass('hidden');
      }

    });

    $('#validateemail').click(function(){
        window.location.href="/validate?voucher=" + $("#voucherid").val() + "&amount=" + $("#amount").val();

        window.history.pushState('obj', 'newtitle', '/validate');

    });

    $('.deleteVoucher').click(function(){

           console.log("Pressed");
           var code = $(this).val();
           console.log(code);
           if (confirm("Delete voucher " + code + "?") == true){
            window.location.href="/delete?voucher=" + code;

            window.history.pushState('obj', 'newtitle', '/display');
           }
           else {
            console.log("Cancelled");
           }

    });

    $('#pageNumber').bind('change', function(){
          console.log($(this).val());
          window.location.href="/display?page=" + $(this).val();
          // url="/display?page=" + $(this).val();
          // $("#allvouchers").load(url);
          // window.history.pushState('obj', 'newtitle', '/display');
    });
    $('.create-copy-btn').bind('click', function(){
        // console.log("clicked.....");
        // setTimeout(1000);
        $('#myModal').show();
    });

// $("#excelbutton").click(function () {
//             $("#tblExport").btechco_excelexport({
//                 containerid: "tblExport"
//                , datatype: $datatype.Table
//             });
//         });

});
