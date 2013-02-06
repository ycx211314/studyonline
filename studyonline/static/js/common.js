function importValidate(){
    $.extend($.validator.defaults,{
        errorElement:"span",
        errorClass:"help-inline",
        highlight:function(el){
            $(el).closest('.control-group').addClass('error');
        },
        unhighlight:function(el){
            $(el).closest('.control-group').removeClass("error").addClass('success');
        }
    });
    $.extend($.validator.messages,{
        email:"邮箱错误",
        required: "不能为空",
        remote: "已存在",
        url: "URL格式错误",
        date: "日期格式错误",
        dateISO: "Please enter a valid date (ISO).",
        number: "只能为数字",
        digits: "Please enter only digits.",
        creditcard: "Please enter a valid credit card number.",
        equalTo: "两次密码不一致",
        accept: "Please enter a value with a valid extension.",
        maxlength: $.validator.format("最多{0}字符"),
        minlength: $.validator.format("最少{0}字符"),
        rangelength: $.validator.format("只能输入{0}到{1}个字符"),
        range: $.validator.format("只能介于{0}~{1}"),
        max: $.validator.format("超过最大值{0}"),
        min: $.validator.format("小于最小值{0}")

    });
}