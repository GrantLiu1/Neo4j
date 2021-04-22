function search() {
        var province = document.getElementById("province").value;
        var city = document.getElementById("city").value;
        var area = document.getElementById("area").value;
        var detailAddress = document.getElementById("detailAddress").value;
        //console.log(province,",",city,",",area,",",detailAddress);
        $.ajax({
            url: "/node/asearch",
            type:"POST",
            dataType: "json",
            data:{
                province: province,
                city: city,
                area: area,
                detailAddress: detailAddress,
            },
            success:function (data) {
                //console.log(data);
                //console.log('调用了1');
                if (data['nodes']==0 && detailAddress==''){
                    layer.msg('该区未分配详细地址，请先添加详细地址!', {icon: 5});
                }
                else if (data['nodes']==0){
                    layer.msg('没有找到该数据!', {icon: 5});
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
        var province = document.getElementById("province").value;
        var city = document.getElementById("city").value;
        var area = document.getElementById("area").value;
        var detailAddress = document.getElementById("detailAddress").value;

        if (province=="" || city=="" || area=="" || detailAddress=="" ){
            layer.msg('不能为空!', {icon: 5});
            return false;
        }

        $.ajax({
            url:"/node/aadd",
            type:"POST",
            //dataType:"json",
            data:{
                province: province,
                city: city,
                area: area,
                detailAddress: detailAddress,
            },
            success:function (data) {
                console.log(data);
                if (data=="fail"){
                    layer.msg('已存在节点!', {icon: 5});
                    //location.replace(document.referrer);
                }
                else {
                    layer.msg('创建成功', {icon: 1});
                    search();
                    //location.replace(document.referrer);
                }
            }
        })
    }

    function del() {
        var id = document.getElementById('nid').title;


        console.log(id.toString());
        $.ajax({
            url:"/node/adelete",
            type:"POST",
           //dataType:"json",
            data:{
                id:id,
                name:name,
            },
            success:function (data) {
                console.log(data);
                if (data=="hasNodes"){
                    layer.msg('该节点下还有别的节点，请先删除这些节点!', {icon: 5});
                    return false;
                    //location.replace(document.referrer);
                }
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

    // function update() {
    //     var id = document.getElementById('nid').title;
    //     // var fkind = document.getElementById('fkind').title;
    //     // var kind = document.getElementById("kind").value;
    //     var name = document.getElementById("name").value;
    //     // var age = document.getElementById("age").value;
    //     // var gender = document.getElementById("gender").value;
    //     // var degree = document.getElementById("degree").value;
    //     // var work = document.getElementById("work").value;
    //     // var home = document.getElementById("home").value;||age==""||gender==""||degree==""||work==""||home==""
    //
    //     if (name==""){
    //         layer.msg('请完善要修改的信息!', {icon: 5});
    //         return false;
    //     }
    //     $.ajax({
    //         url:'/node/aupdate',
    //         type:'POST',
    //         data:{
    //             id:id,
    //             // fkind:fkind,
    //             // kind:kind,
    //             name:name,
    //             // age:age,
    //             // gender:gender,
    //             // degree:degree,
    //             // work:work,
    //             // home:home,
    //         },
    //         success:function (data) {
    //             console.log(data);
    //             if (data=="fail"){
    //                 layer.msg('修改失败!', {icon: 5});
    //             }
    //             else {
    //                 layer.msg('修改成功!', {icon: 1});
    //                 search();
    //             }
    //         }
    //     })
    //
    // }
