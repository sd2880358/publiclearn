# JS 元素获取与操作
> 可以是用内置对象document上的getElementById方法来获取页面上设置了id属性的元素获取的到的是一个
html对象,然后将它赋值给一个变量,比如:
```
<script type='text/jacascript'>
    var oDiv = document.getElementById('div1');
</script>
...
```
> 上面的语句,如果把JavaScript写在元素的上面,就会出错,因为页面是从上往下加载执行的,JavaScript去页面上获取元素div1的时候,元素div1还没
有加载,解决方法有两种:

第一种方法:将javascript放到页面的最下边
```
...
<div id="item1">这是一个div元素</div>
...
<script>
    var oDiv = document.getElementById('item1');
</script>
```
第二种方法
```
<script>
    window.onload=function(){
    var oDiv = document.getElementById('item1');
   }
</script>
```
# 样式操作
>标签对象.style.css属性="值"//改变标签对象的样式
示例:id.style.color="red";
注意:属性名相当于变量名,所以css属性命中含有双拼词(font-size)的减号要去掉,将后面的首字母大写
fontSize

# 文本操作
>标签对象.innerHTML="内容";//在标签对象内放置指定内容
获取一般内容用innerText

#标签中值的操作
>标签对象.value;//获取标签对象的value值
>标签对象.value='值'//设置标签对象的value值

