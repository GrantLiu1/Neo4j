function search() {
    var category = document.getElementById("category").value;
    var name = document.getElementById("name").value;
    var location = document.getElementById("detailAddress").value;
    var mainBusiness = document.getElementById("mainBusiness").value;
    $.ajax({
        url: "/node/csearch",
        type:"POST",
        dataType: "json",
        data:{
            category:category,
            name:name,
            location:location,
            mainBusiness:mainBusiness,
        },
        success:function (data) {
            //console.log(data);
            //console.log('调用了1');
            if (data['nodes']==0){
                layer.msg('没找到该数据!', {icon: 5});
            }
            else {
                mychart.setOption(option,true);
                //console.log(data);
                mychart.setOption({
                    series:[{
                        data:data['nodes'],
                        links:data['links'],
                    },
                    ]
                });
                }


        }
    })
}

function add() {
    var category = document.getElementById("category").value;
    var name = document.getElementById("name").value;
    var location = document.getElementById("detailAddress").value;
    var mainBusiness = document.getElementById("mainBusiness").value;

    if (name==""||category==''||location==''||mainBusiness==''){
        layer.msg('所有信息不能为空!', {icon: 5});
        return false;
    }

    $.ajax({
        url:"/node/cadd",
        type:"POST",
        data:{
            category:category,
            name:name,
            location:location,
            mainBusiness:mainBusiness,
        },
        success:function (data) {
            console.log(data);
            if (data=="hasNode"){
                layer.msg('已存在该节点!', {icon: 5});
                return false;
            }
            else if (data=="noLocation"){
                layer.msg('地址不存在，请检查!', {icon: 5});
                return false;
            }
            else if (data=="locationHasTaken"){
                layer.msg('地址已被其他公司注册，请检查!', {icon: 5});
                return false;
            }
            else if(data=="success"){
                layer.msg('创建成功!', {icon: 1});
                search();
                return;
            }
            else{
                layer.msg('创建失败!', {icon: 1});
                return;
            }
        }
    })
}

function del() {

    var id = document.getElementById('nid').title;
    var category = document.getElementById("category").value;
    var name = document.getElementById("name").value;
    var location = document.getElementById("detailAddress").value;
    var mainBusiness = document.getElementById("mainBusiness").value;

    $.ajax({
        url:"/node/cdelete",
        type:"POST",
        data:{
            id:id,
            category:category,
            name:name,
            location:location,
            mainBusiness:mainBusiness,
        },
        success:function (data) {
            console.log(data);
            if (data=="fail"){
                layer.msg('删除失败!', {icon: 5});
                //location.replace(document.referrer);
            }
            else {
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
    // var age = document.getElementById("age").value;
    // var gender = document.getElementById("gender").value;
    // var degree = document.getElementById("degree").value;
    // var work = document.getElementById("work").value;
    // var home = document.getElementById("home").value;||age==""||gender==""||degree==""||work==""||home==""

    if (id==''){
        layer.msg('请点击图中节点!', {icon: 5});
        return false;
    }

    if (name==""){
        layer.msg('请完善要修改的信息!', {icon: 5});
        return false;
    }

    $.ajax({
        url:'/node/cupdate',
        type:'POST',
        data:{
            id:id,
            // fkind:fkind,
            // kind:kind,
            name:name,
            // age:age,
            // gender:gender,
            // degree:degree,
            // work:work,
            // home:home,
        },
        success:function (data) {
            console.log(data);
            if (data=="fail"){
                layer.msg('修改失败!', {icon: 5});
            }
            else {
                layer.msg('修改成功!', {icon: 1});
                search();
            }
        }
    })

}
