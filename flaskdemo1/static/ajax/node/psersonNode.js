function myIsNaN(value) {
    return typeof value === 'number' && !isNaN(value);
  }
function checkInfo(idcard , phone){
    if (idcard.length != 18){
        layer.msg('身份证长度错误，请重新输入!', {icon: 5});
        return false;
    }
    if (phone.length != 11){
        layer.msg('手机号长度错误，请重新输入!', {icon: 5});
        return false;
    }
}

function search() {
    var idcard = document.getElementById('idcard').value;
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var sex = document.getElementById("gender").value;
    var birthday = document.getElementById('birthday').value
    var education = document.getElementById("degree").value;
    var work = document.getElementById("work").value;
    var company = document.getElementById('company').value
    var province = document.getElementById("province").value;
    var city = document.getElementById("city").value;
    var district = document.getElementById("district").value;
    var home = document.getElementById("home").value;
    var phone = document.getElementById("phone").value;
    var financialSit = document.getElementById('financialSit').value;

    $.ajax({
        url: "/node/psearch",
        type: "POST",
        dataType: "json",
        data: {
            idcard:idcard,
            name: name,
            age: age,
            sex: sex,
            birthday:birthday,
            education: education,
            work: work,
            company:company,
            province:province,
            city:city,
            district:district,
            home: home,
            phone:phone,
            financialSit:financialSit
        },
        success: function (data) {
            //console.log(data);
            if (data['nodes'] == 0) {
                layer.msg('未查到该数据!', {icon: 5});
            } else {
                mychart.setOption(option, true);
                //console.log(data);
                mychart.setOption({
                    series: [{
                        data: data['nodes'],
                        links: data['links'],
                    },
                    ]
                });
            }


        }
    })
}

function add() {
    var idcard = document.getElementById('idcard').value;
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var sex = document.getElementById("gender").value;
    var birthday = document.getElementById('birthday').value
    var education = document.getElementById("degree").value;
    var work = document.getElementById("work").value;
    var company = document.getElementById('company').value
    var province = document.getElementById("province").value;
    var city = document.getElementById("city").value;
    var district = document.getElementById("district").value;
    var home = document.getElementById("home").value;
    var phone = document.getElementById("phone").value;
    var financialSit = document.getElementById('financialSit').value;

    if (idcard == "" || name == "" || age == "" || sex == "" || birthday == "" ||  education == "" || work == "" || company == "" || province == "" || city == "" || district == "" || home == "" || phone == "" || financialSit == "") {
        layer.msg('请完善信息,添加时所有信息不能为空!', {icon: 5});
        return false;
    }
    // if (!checkInfo(idcard.trim(),phone.trim())){
    //     return false;
    // }

    $.ajax({
        url: "/node/padd",
        type: "POST",
        data: {
            idcard:idcard,
            name: name,
            age: age,
            sex: sex,
            birthday:birthday,
            education: education,
            work: work,
            company:company,
            province:province,
            city:city,
            district:district,
            home: home,
            phone:phone,
            financialSit:financialSit
        },
        success: function (data) {
            if (data == "hasPerson") {
                layer.msg('该身份证号已被使用，请检查输入的身份证号!', {icon: 5});
                return false;
            }
            if (data == "noCompany") {
                layer.msg('未查到该公司，请先添加公司信息后重试!', {icon: 5});
                return false;
            }
            if (data == "noAddress") {
                layer.msg('未查到该地址，请先添加地址信息后重试!', {icon: 5});
                return false;
            }
            else {
                layer.msg('创建成功!', {icon: 1});
                search();
            }
        }
    })
}

function del() {
    var idcard = document.getElementById('idcard').value;
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var sex = document.getElementById("gender").value;
    var birthday = document.getElementById('birthday').value
    var education = document.getElementById("degree").value;
    var work = document.getElementById("work").value;
    var company = document.getElementById('company').value
    var province = document.getElementById("province").value;
    var city = document.getElementById("city").value;
    var district = document.getElementById("district").value;
    var home = document.getElementById("home").value;
    var phone = document.getElementById("phone").value;
    var financialSit = document.getElementById('financialSit').value;

    $.ajax({
        url: "/node/pdelete",
        type: "POST",
        //dataType:"json",
        data: {
            idcard:idcard,
            name: name,
            age: age,
            sex: sex,
            birthday:birthday,
            education: education,
            work: work,
            company:company,
            province:province,
            city:city,
            district:district,
            home: home,
            phone:phone,
            financialSit:financialSit
        },
        success: function (data) {
            console.log(data);
            if (data == "fail") {
                layer.msg('删除失败!', {icon: 5});
                //location.replace(document.referrer);
            } else {
                layer.msg('删除成功!', {icon: 1});
                //location.replace(document.referrer);
            }
        }
    })
}

function update() {
    var id = document.getElementById('nid').title;
    // var fkind = document.getElementById('fkind').title;
    // var kind = document.getElementById("kind").value;
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var gender = document.getElementById("gender").value;
    var degree = document.getElementById("degree").value;
    var work = document.getElementById("work").value;
    var home = document.getElementById("home").value;

    if (name == "" || age == "" || gender == "" || degree == "" || work == "" || home == "") {
        layer.msg('请完善要修改的信息!', {icon: 5});
        return false;
    }
    $.ajax({
        url: '/node/pupdate',
        type: 'POST',
        data: {
            id: id,
            // fkind:fkind,
            // kind:kind,
            name: name,
            age: age,
            gender: gender,
            degree: degree,
            work: work,
            home: home,
        },
        success: function (data) {
            console.log(data);
            if (data == "fail") {
                layer.msg('修改失败!', {icon: 5});
            } else {
                layer.msg('修改成功!', {icon: 1});
                search();
            }
        }
    })

}

function setpcr() {

}

