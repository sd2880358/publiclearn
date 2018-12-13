# CSS
``` 
为了让网络元素的样式更加丰富
也为了让网页的内容和样式能拆分开
css由此思想而诞生
css 是Cascading Style Sheels 的首字母缩写
意思是层叠样式表
有了CSS, HTML中大部分表现样式的标签就废弃不用了
html只负责文档的结构和内容,表现形式完全交给CSS, HTML文档变得更加简洁
```

# CSS的基本语法及引用
>CSS的定义方法是:选择器{属性:值;属性:值;属性:值;}   选择器是将样式和页面元素关联起来的名称,属性是希望设置样式属性,每个属性有一个或多个值

示例:  
```div{widht:200;height:200;background-color:red;}```

# CSS选择器

基本三种选择选择器的优先级问题,影响范围越大,优先级越低id>class>元素选择器

常用的选择器有以下几种:
1. 标签选择器
> 标签选择器: 此证选择器影响范围大,建议尽量在层级选择器中 

示例:
``` html
{margin:0; padding:0}
div{color:red;}
<div>...</div> <!-- 对应以上两条样式-->
<div class=box> ... </div> <!-- 对应以上两条样式-->
```
2. id选择器
> 通过id名来选择元素, 元素的id不能重复, 所以一个样式设置项只能对应页面上一个元素,不能重复,id一般给程序使用,所以不推荐使用id选择器

示例:
```
#box{color:red;}
<div id="box">...</div> <!--对应以上一条,其他元素不允许应用此样式-->

```
3. 类选择器
> 通过类名来选择元素, 一个类可应用与多个元素, 一个元素上也可以使用多个类, 应用灵活,可重复,是css中应用最多的选择器

示例:
```
.red{color:red}
.big{font -size:20px}
<div class="red"> ... </div>


```
4. 层级选择器
> 主要应用在选择父元素下的子元素,或者子元素下面的子元素,可与标签元素结合使用,减少命名,同时也可以通过层级,防止命名冲突

示例:  
```
.box span{color: red}
.box .red{color: pink}
. red {color:red}
<div class= "box">
    <span> ... </span>
    <a href="#" class="red"> ... </a>
</div>
<h3 class="red"> ... </h3>

```
5. 组选择器
> 多个选择器, 如果有同样的样式设置,可以使用组选择器,也称为并列选择器

示例:  
```
.box1,.box2,.box3{width:100px; height:100px;}
.box1{background:red}
.box2{background:pink}
.box2{background:gold}
<div class="box1"> ... </div>
<div class="box2"> ... </div>

```
6. 伪类选择器
> 常用的伪类选择器有hover, 表示鼠标悬浮在元素上时的状态, 伪元素选择器有before和after,它们可以通过样式在元素中插入内容

示例:
```
.box1:hover{color:red}
<div class="box1"> ...</div>
a:hover {color: green; text-decoration:underline} 鼠标在该元素上时的样式 
a: before{content:"hello"} 在每个<a>元素插入前
a:after{content:world} 在每个<a> 元素之后插入的内容

```
# CSS页面引入
- 优先级:
    因为HTML代码从上往下加载,因此与元素最近的一个生效
1. 外链式: 通过link标签, 连接到外部样式表到页面中
`link rel="stylesheet" type="text/css" hre="css/main.css"`
2. 嵌入式: 通过style标签, 在网页上创建嵌入的样式表
```<style type="text/css">
    div{ width:100px; height:100px; color:red;}
 </style>
 ```

3.内链式: 通过标签的style属性,在标签上直接写样式
 ```
 <div style="width:100px; height:100px;
 color:red"</div>
 ```
 # CSS颜色,文本字体
 
 ## CSS颜色表示法
 1. 颜色名表示,比如:red红色,gold金色
 2. 16进制数值表示,如#ff0000 表示红色,可以简写成#f00
 3. RGB颜色:红(R),绿(G),蓝(B)三个颜色的通道变化background-color:rgb(200,100,0);
 4. RGBA颜色:(A) 表示透明度,取值范围0-1:background-color:rgba(0,0,0,1); 
 ```
 16进制 0-9 a-f
 rgb的值:0-255
```

## CSS文本设置
常用的应用文本的css样式:
```
color 设置文职的颜色, 如:color:red;
font-size 设置文字的大小, 如:font-size:12px;
font-family 设置文字的字体,如 font-family:"微软硬黑";
font-style: 设置字体是否倾斜, 如:font-style:"normal"; 设置不斜体. font-style:"italic" 设置斜体
font- weight 设置字体是否加粗, 如: font-weight:bold; 设置加粗. 
line-height 设置文字的行高, 如:line-height:1px;
text-decoration 设置文字的下划线, 如text-decoration:underline;
text-indent 设置文字首行缩进, 如:text-indent:24px; 设置文字首行缩进24个像素
text-align, 设置文字的对齐方式, 如text-align:center; 设置居中


```

## CSS边框属性
```
border: (宽度) (样式) (颜色);
border-color;
coder-style; 边框样式: solid实线; dotted点状线; dashed虚线;
border-width;
border-left-color;
boder-left-style;
border-left-width;
CSS3样式:
border-radius: 圆角处理
box-shadow: x轴偏移,y轴偏移,模糊度,扩散程度,颜色,inset内阴影, 设置或检索对象阴影
```

# 背景属性
```
*background-color:背景颜色
*background-img: 背景图片
*background-repeat: 是否重复,如何重复
*background-position:定位
CSS3属性:
*background-size:背景大小,如background-size:100px 140px
```