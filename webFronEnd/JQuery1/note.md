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
