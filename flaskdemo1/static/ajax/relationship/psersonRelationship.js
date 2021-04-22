function search() {
    var nod1type = document.getElementById("nod1type").value;

    var id1 = document.getElementById("id1").value;

    var l1 = document.getElementById("l1").value;

    var relanme = document.getElementById("rel").value;

    var l2 = document.getElementById("l2").value;

    var nod2type = document.getElementById("nod2type").value;

    var id2 = document.getElementById("id2").value;


    $.ajax({
        url: "/relationship/prSearch",
        type:"POST",
        // dataType: "json",
        data:{
            nod1type:nod1type,
            id1:id1,
            l1:l1,
            relanme:relanme,
            l2:l2,
            nod2type:nod2type,
            id2:id2,
        },
        success:function (data) {
            console.log(data);
            if (data=='l1lack'){
                layer.msg('请选择连接线1!', {icon: 5});
                return false;
            }
            else if (data=='l2lack'){
                layer.msg('请选择连接线2!', {icon: 5});
                return false;
            }
            else if (data=='noNode'){
                console.log(1);
                layer.msg('未查找到该关系!', {icon: 5});
                return false;
            }
            else {
                mychart.setOption(option,true);
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


    var id1 = document.getElementById("id1").value;

    var l1 = document.getElementById("l1").value;

    var relanme = document.getElementById("rel").value;

    var l2 = document.getElementById("l2").value;

    var id2 = document.getElementById("id2").value;

    if (nod1type==""||id1==""||l1==""||relanme==""||l2==""||nod2type==""||id2==""){
        layer.msg('请完善信息后再试!', {icon: 5});
        return false;
    }

    $.ajax({
        url:"/relationship/prAdd",
        type:"POST",
        data:{
            nod1type:nod1type,
            id1:id1,
            l1:l1,
            relanme:relanme,
            l2:l2,
            nod2type:nod2type,
            id2:id2,
        },
        success:function (data) {
            console.log(data);
            if (data=="noNode1"){
                layer.msg('节点一不存在，请先创建节点!', {icon: 5});
            }
            else if (data=="noNode2"){
                layer.msg('节点二不存在，请先创建节点!', {icon: 5});
            }
            else {
                layer.msg('创建成功!', {icon: 1});
                search();
                //location.replace(document.referrer);
            }
        }
    })
}

    function del() {

        //var kind = document.getElementById("kind").value;
        var name = document.getElementById("name").value;
        var age = document.getElementById("age").value;
        var gender = document.getElementById("gender").value;
        var degree = document.getElementById("degree").value;
        var work = document.getElementById("work").value;
        var home = document.getElementById("home").value;

        $.ajax({
            url:"/node/pdelete",
            type:"POST",
           //dataType:"json",
            data:{
                kind:'person',
                name:name,
                age:age,
                gender:gender,
                degree:degree,
                work:work,
                home:home,
            },
            success:function (data) {
                console.log(data);
                if (data=="fail"){
                    alert("删除失败");
                    //location.replace(document.referrer);
                }
                else {
                    alert("删除成功");
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

        if (name==""||age==""||gender==""||degree==""||work==""||home==""){
            alert("请完善要修改的信息！");``
            return false;
        }
        $.ajax({
            url:'/node/pupdate',
            type:'POST',
            data:{
                id:id,
                // fkind:fkind,
                // kind:kind,
                name:name,
                age:age,
                gender:gender,
                degree:degree,
                work:work,
                home:home,
            },
            success:function (data) {
                console.log(data);
                if (data=="fail"){
                    alert("修改失败");
                }
                else {
                    alert("修改成功");
                    search();
                }
            }
        })

    }

    function reset() {
        document.getElementById("myform").reset();
    }