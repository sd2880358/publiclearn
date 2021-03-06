# CSS 间距

## 内补白(内补丁)
```
padding: 检索或设置对象四边的内部边距:如padding:10px; padding:5px 10px;
padding-top : 检索或设置对象顶边的内部边距
padding-right: 检索或设置对象右边的内部边距
padding-bottom: 检索或设置对象下边的内部边距
padding-left: 检索或设置对象左边的内部边距
```

## 外补白(外补丁)
```
margin: 检索或设置对象四边的外延边距,如 margin:10px; margin:5px auto;
margin-top : 检索或设置对象顶边的外延边距
margin-bottom: 检索或设置对象下边的外延边距
margin-right: 检索或设置对象右边的外延边距
margin-left: 检索或设置对象左边的外延边距

```
### margin相关小技巧
```
1.设置元素水平居中: margin:x auto;
2. margin 赋值让元素唯一及边框合并
```
# 盒子模型
元素在页面显示成一个方形,类似一个盒子,css盒子模型就是使用现实中的盒子来做比喻,帮助我们设置元素对应的样式
> 把元素叫做盒子,设置对应的样式分别为:盒子的边框border, 盒子内的内容和边框之间的间距(padding),盒子与盒子之间的间距margin

```
盒子的真实尺寸
盒子的宽度:width-padding左右,border左右
盒子的高度: height-padding上下,border上下
```
在布居中,如果想增大内容和边框的距离,又不想改变盒子显示的尺寸
```
box-sizing:content-box|border-box
```
# 块元素,内链元素,内链块元素
> 元素就是标签,不居中常用的有三种标签,块元素,内链元素,内联块元素,了解这三种元素的特性,才能熟练的进行页面布局

## 块元素
块元素,也可以成为航元素, 常用的标签有: div, p, ul, li, h1-h6, dl, dt, dd等都是块元素,它在不居中的行为:
    - 支持全部样式
    - 如果没有设置宽高,默认的宽高为父级元素的100%
    - 盒子占一行,即使设置了宽高
## 内联元素
内链元素,亦可以成为内元素, 布局中常用标签有: a, span, em, b, strong, i 等等都是内链元素,他们在布局中的行为:
    - 支持部分样式(不支持宽, 高)
    - 宽高由内容决定
    - 盒子并在一行
    - 代码换行,盒子之间会产生间距
    - 子元素是内联元素, 父元素可以用text-align属性来设置子元素的对齐方式, 用line-height属性来设置垂直对齐方式
## 内链块元素

内联块元素,也叫内块元素,是新增的元素类型,现有元素没有归于此类别,img和input元素的行为类似于这种元素,但是也归类于内联元素,他们在不居中表现的行为
    - 支持全部样式
    - 如果没有设置宽高,宽高由内容决定
    - 盒子并在一行
    - 代码换行, 盒子会产生间距
    - 子元素是内联块元素,父元素可以用用text-align蛇形设置子元素水平对齐方式,用line-height属性设置子元素垂直对齐方式
    
# 块元素,内联元素,内联块元素之间的转换

display属性是用来设置元素的类型及隐藏的,常用的属性有:
    - none元素隐藏且不占位置
    - block元素以块元素显示
    - inline 元素以内联元素显示
    - inline-block元素以内联块元素显示