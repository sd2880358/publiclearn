# 相关尺寸
** 获取元素相对于文档的偏移量**
> var pos = $('#small').offset();

**获取当前元素相对于父级属性的偏移量**
> var l = $('#small').position(left);  
var t = $('small').position(.top)  

**获取文档滚动距离**
> var st = $(document).scrollTop();  
var sl = $(document).scrollLeft();  

**获取元素的宽度和高度**
> var w = $('#big').width  

**获取可视区域的宽度和高度**
> var cw = $(window).width()  
var ch = $(window).height()

**获取文档的宽度和高度**
> var cw = $(document).width()  
var ch = $(document).height()

## 关于事件对的绑定
**1.基本的绑定**
```javascript
$(element).click(function(){});
$(element).click(function(){});
//...
// 加载完毕
$(document).ready(function(){});//当页面加载完成后加载的函数;
$(function(){});
// 双击事件绑定
$(document).dblclick(function(){});
```
**方法绑定**
```javascript
$(element).bind('click',function(){});//绑定事件
$(element).unbind();//解除事件绑定,不指定则解除所有事件
$(element).unbind('dblclick');//解除指定事件
```
**动态绑定**
```javascript
$(element).live('click',function(){});
//需注意,live方法在藁本的jquery中移除了,在使用时请注意版本;
```
## 事件触发
> 当我们想要去触发某个元素的事件时,可以调用trigger, 注意需指定元素的事件类型  
`$(element).trigger('click')`
# 鼠标常用的事件
```
鼠标单击事件 click
鼠标双击事件 dblclick
鼠标移入事件 mouseover
鼠标移出事件 mouseout
鼠标按下事件 mousedown
鼠标抬起事件 mouseup
鼠标移动事件 mousemove
```
# 事件冒泡和默认行为
**事件冒泡**
> 当触发一个元素的事件时,会自动触发该元素的父级和先辈级的同类型事件,造成事件并发,导致页面混乱,我们成为事件冒泡  
此时我们可以在元素的事件处理函数中返回一个false来进行组织,注意这个方法仅限于在jquery中使用

**默认行为**
> 在页面中有些元素是具备默认行为的,例如a链接的单击,表单的提交,都会进行跳转或者提交,这些称为默认行为  
但是在绑定上事件后,他首先会执行事件,再去执行默认行为,而有时我们只想让其触发事件,但不执行默认行为是.
我们可以在该元素事件中返回一个false来组织默认行为  

```html
<a href="http://www.baidu.com">百度</a>
<script >
$('a').click(function(){
    //阻止默认行为
    return false;
});
</script>
```

**获取当前鼠标的位置和按键**
> 我们有鼠标和键盘按键的事件,在触发事件时吐过我们想要获取鼠标的位置或键盘信息时,  
首先需要在当前的事件中传入一个事件对象  
```javascript
$(element).click(function(e){
    //能够获取鼠标的x轴和Y轴的坐标,坐标位置相对浏览器窗口
    var x = e.clientX;
    var y = e.clientY;
    //能够获取鼠标x轴和y轴相对于文档的坐标位置
    var x1 = e.pageX;
    var y1 = e.pageY;
    // 能够获得鼠标相对于标签的坐标位置
    var x2 = e.offsetX;
    var y2 = e.offsetY;
});

$(element).keydown(function(e){
    //可以打印e对象,或者直接只用该对象中的keyCode属性获取按键信息
    var key = e.keyCode;
    console.log(key);
})
```
