# JQuery

> JQuery 是一个免费,开元的JavaScript库,也是目前使用最广泛的JavaScript函数库.
JQuery极大的方便你完成web前端的相关操作,比如节点操作,时间绑定,ajax操作,且解决了大多数兼容性问题.
JQuery的版本分别为1.x系列和2.x,3.x系列,1.x系列兼容低版本的浏览器,2.x,3.x系列放弃支持低版本浏览器,目前使用最多的事1.x系列的.
官方网站

JQuery是一个函数库,一个js文件,页面用script标签引入这个js文件就可以使用.
`<script type="text/jacascript" src=js/jquery-1.8.3.min.js></script>`

## JQuery选择器

**JQuery用法思想**
选择某个网页元素,然后对他进行某种操作
**JQuery**
JQuery选择器可以快速的选择元素,选择规则和CSS样式相同
## 基础选择器
```javascript
// 通过id来获取元素document.getElementById();
// $('#logo').css('border',solid 2px red');
//通过标签名来获取元素
$('li').css('background','#369');
//通过class类名获取元素
$('.w').css('background','#369');
//逗号 并列获取
$('#logo,#menu').css('background','#369');
// 空格 层级获取
$('#img li').css('background','#369');
```
## 过滤选择器
```javascript
// 获取第一个和最后一个元素
$('li:first').css('background','#369');
$('li:last').css('background','#369');
//获取指定的索引元素,索引从0开始
$('li:eq(7)').css('background','#369');
$('li').eq(7).css('background','#369');
// 获取包含指定文本的元素
$('li:contains(国)').css('background','#369')
//通过包韩指定属性的元素 通过属性来获取
$('li[name=yl]').css('background','#369');
```
## 父子关系获取
```javascript
//获取所有的子元素
$('#img').children().css('background','#369');
// 获取第一个子元素
$('ul li:first-child').css('background','#369');
// 获取最后一个子元素
$('ul li:last-child').css('background','#369');
// 获取指定索引的子元素 索引从1开始
$('ul li:nth-child(3)').css('background','#369');
// 获取元素上个同级元素
$('#f').prev().css('background','#369');
// 获取元素下一个同级元素
$('#f').next().css('background','#369');
// 获取同辈元素(同辈元素不包括自己)
$('#f').siblings().css('background','#369');
// 在父级元素中查找指定的子元素
$('#img').find('.w').css('background','#369');

```
# JQuery 元素操作
通过JQuery可以操作控制元素的样式,文本,属性等
## JQuery样式操作
** CSS操作行内样式 **
```javascript
// 获取div的样式
$('div').css('width');
$('div').css('color');

//设置div的样式
$('div').css('width','30px');
$('div').css('width','30px');
$('div').css('height','30px');
```
** 特别注意 ** 
选择器获取的多个元素,获取信息获取的第一个,比如:$('div').css('width'),获取的事第一个div的样式.
## 类名class操作
** 操作样式类名 **
```javascript
$('#div').addClass('divClass2')//将id为div1的对象追加样式divClass2
$('#div').removeClass('divClass')//移除id是div1的对象的Class名为divClass的样式
$('#div').remove('divClass divClass2')//移除多个样式
$('#div').toggleClass('anotherClass')//重复切换anotherClass样式
```
## 文本操作
** 1. html() 去除或设置html内容**
```javascript
//去除html内容
var $htm = $('#div1').html();
// 设置html内容
var div = $('#div1').html('<h1>123</h1>'); 
```
## 属性操作
** 1. attr 取出或设置某个属性的值 **
```javascript
//取出图片的地址
var $src = $('#img').attr('src');
//设置图片的地址和alt属性
$('img').attr({src:'test.jpeg ',alt:'test image'});
//也可以用户设置class属性
$('#abc').attr('love','i love you')
```
** 2. removeattr() **
```javascript
$('#abc').removeattr('class')
 
```