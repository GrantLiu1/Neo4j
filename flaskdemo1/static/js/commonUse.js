document.write("<script src='/static/js/echarts.js\'></script>");

//颜色
function colors(data) {

    //address节点颜色
    if(data.data['label']=='address')
    {
         return '#00BFFF';
    }
    //company节点颜色
    else if(data.data['label']=='company'){
        return '#12bd96';
    }
    //province节点颜色
    else if(data.data['label']=='province'){
        return '#4ea3ec';
    }
    //city节点颜色
    else if(data.data['label']=='city'){
        return '#31adc4';
    }
    //district节点颜色
    else if(data.data['label']=='area'){
        return '#608ea3';
    }
    //department节点颜色
    else if(data.data['label']=='department'){
        return '#85bba9';
    }
    //person节点颜色
    else {
        return '#FAAC58';
    }
}

function nodetip(a) {
    var colo=a.color;
    var htmlstr='<span style="margin-right:5px;display:inline-block;width:10px;height:10px;border-radius:5px;background-color:'+colo+';"></span>'+
                a.data['label']+'<br>';


     for (var b in a.data) {
        if (b=='id' || b=='emphasis'|| b=='province'|| b=='city'|| b=='area')
            continue;
        var str1=''
        str1 += b;
        str1 += ':'
        str1 += a.data[b.toString()];
        str1 += '<br>';
        htmlstr += str1;
    }
     return htmlstr;

    // for (var datumKey in a.data['label']) {
    //
    //         // if ('person'==a.data['label'][datumKey]){
    //         //     for (var b in a.data) {
    //         //         if (b=='id' || b=='emphasis')
    //         //             continue;
    //         //         var str1=''
    //         //         str1 += b;
    //         //         str1 += ':'
    //         //         str1 += a.data[b.toString()];
    //         //         str1 += '<br>';
    //         //         htmlstr += str1;
    //         //     }
    //         //     // console.log(htmlstr);
    //         //
    //         //     return  htmlstr;
    //         //     // return htmlstr+
    //         //     //     'name:'+a.data['name']+'<br>'+
    //         //     //     'sex:'+a.data['sex']+'<br>'+
    //         //     //     'age:'+a.data['age']+'<br>'+
    //         //     //     'degree:'+a.data['degree']+'<br>'+
    //         //     //     'work:'+a.data['work']+'<br>'+
    //         //     //     'home:'+a.data['home']+'<br>';
    //         // }
    //         // else if ('company'==a.data['label'][datumKey]){
    //         //     return htmlstr +
    //         //         'name:'+a.data['name']+'<br>';
    //         // }
    //         // else if ('address'==a.data['label'][datumKey]){
    //         //     return htmlstr +
    //         //         'name:'+a.data['name']+'<br>';
    //         // }
    // }
    //
    //
    //     return htmlstr +
    //         'name:'+a.data['name'];


}

function nodetip1(params) {
     console.log(params[0].color());
    // console.log(params['name']);
          var htmlStr = '';
          for(var i=0;i<params.length;i++){
                var param = params['nodes'][i];
                console.log(1);
                console.log(param['name']);
                // var xName = param.name;//x轴的名称
                // var seriesName = param.seriesName;//图例名称
                // var value = param.value;//y轴值
                // var color = param.color;//图例颜色
                //
                // if(i===0){
                //   htmlStr += xName + '<br/>';//x轴的名称
                // }
                // htmlStr +='<div>';
                //
                // // 具体显示的数据【字段名称：seriesName，值：value】
                // // 这里判断一下name，如果是我们需要特殊处理的，就处理
                // if(seriesName === '额外信息'){
                //     // 前面一条线，后面一条线【具体样式自己写】
                //     htmlStr += '<div style="border: 1px solid #FFEB3B"></div>';
                //     htmlStr += 'XXXXX：' + value;
                //     htmlStr += '<div style="border: 1px solid #FFEB3B"></div>';
                // }else{
                //     // 正常显示的数据，走默认
                //     htmlStr += '<span style="margin-right:5px;display:inline-block;width:10px;height:10px;border-radius:5px;background-color:'+color+';"></span>';
                //     htmlStr += seriesName + '：' + value + 'W';
                // }
                //
                // htmlStr += '</div>';
          }


          return htmlStr;

}

function pca(ele,value) {
    ele.find("option").remove();
    var optionStar = "<option value=" + value + " >" + value + "</option>";
    ele.append(optionStar);
}

function reset1() {

    document.getElementById("myform").reset();
    layui.use([ 'form'], function() {
        function removeEle(ele) {
            ele.find("option").remove();
            var optionStar = "<option value=''>" + "请选择" + "</option>";
            ele.append(optionStar);
            layui.form.render();
        }
        removeEle($(".province"));
        removeEle($(".city"));
        removeEle($(".district"));


            var form = layui.form;
            var provinceList=[]

            $.ajax({
                url: "/general/selectAdd",
                type: "GET",
                dataType: "json",
                success:function (data) {
                    provinceList=data['provinceList'];
                    var province = $(".province");

                    //初始将省份数据赋予
                    for (var i = 0; i < provinceList.length; i++) {
                        addEle(province, provinceList[i].name);
                    }

                    //向select中 追加内容
                    function addEle(ele, value) {
                        var optionStr = "";
                        optionStr = "<option value=" + value + " >" + value + "</option>";
                        ele.append(optionStr);
                    }
                    //重新渲染select
                    form.render('select');

                    //移除select中所有项
                    function removeEle(ele) {
                        ele.find("option").remove();
                        var optionStar = "<option value=''>" + "请选择" + "</option>";
                        ele.append(optionStar);
                    }

                    var provinceText,
                        cityText,
                        cityItem;
                    //选定省份后 将该省份的数据读取追加上
                    form.on('select(province)', function(data) {
                        var city = $(data.elem).parents(".layui-form-item").find(".city")
                        var district = $(data.elem).parents(".layui-form-item").find(".district");
                        provinceText = data.value;
                        $.each(provinceList, function(i, item) {
                            if (provinceText == item.name) {
                                cityItem = i;
                                return cityItem;
                            }
                        });
                        removeEle(city);
                        removeEle(district);
                        $.each(provinceList[cityItem].cityList, function(i, item) {
                            addEle(city, item.name);
                        })
                        form.render('select');
                    })

                    //选定后 将对应的数据读取追加上
                    form.on('select(city)', function(data) {
                        var district = $(data.elem).parents(".layui-form-item").find(".district");
                        cityText = data.value;
                        removeEle(district);
                        $.each(provinceList, function(i, item) {
                            if (provinceText == item.name) {
                                cityItem = i;
                                return cityItem;
                            }
                        });
                        $.each(provinceList[cityItem].cityList, function(i, item) {
                            if (cityText == item.name) {
                                for (var n = 0; n < item.areaList.length; n++) {
                                    addEle(district, item.areaList[n]);
                                }
                            }
                        })
                        form.render('select');
                    })
                }
            })
        })

}