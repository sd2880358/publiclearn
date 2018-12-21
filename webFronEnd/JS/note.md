# JavaScript

## 目标

学习前端脚本语言JavaScript的基本概念,页面引入方式, 获取页面元素及操作元素属性的技巧,学习函数的基本定义方法和使用方法

## 前端三大块
```
HTML页面结构
CSS 页面的表现形式
JavaScript:页面的动态效果和一些简单的特效
```

## 什么是JavaScript?

JavaScript是运行在浏览器端的脚本语言,JavaScript主要解决的是前端与用户交互的问题,包括使用交互与数据交互,JavaScript是浏览器解析和
执行的
```
1. JavaScript 是一种客户端脚本语言(脚本语言是一种轻量级的编程语言)
2. JavaScript 通常被直接嵌入HTML 页面
3. JavaScript 是一种解释性语言(就是说,代码执行不进行预编译)
```
## 特点
```
1. 弱类型
2. 基于对象(因为面向对象具有封装,继承,多态的特征)
3. 安全
4. 兼容性
```
## JavaScript嵌入页面的方式
1. 页面script标签嵌入
```
<script type="text/javascript>

    var a="你好"
    alert(a);
    
</script><input type="button" name="onclick="alert('ok!');">
```
2. 外部引入
```
<script type="text/javascript" src="js/index.js"></script>
```
3. 行间事件(主要用于事件)
<input type="button" name="" onclick="alert('ok');">

## JavaScript语句注释
1. 单条语句以";"结尾
2. 单行注释以//开头,多行以/**/注释

## JavaScript变量

JavaScript是一种弱类型语言, JavaScript的变量类型由它的值决定.
定义变量需要用关键词'var',
不使用var关键字定义全局变量,在严格模式下将会执行错误"use strict";
```
var a=123;
var b='asd';
同时定义多个变量可以用','隔开,公用一个'var'名词
var c=45,d='qwe',e='68';
```
## 变量,函数,属性命名规范
```
字母,数字,下划线,$组成
首字母不能以数字开头
严格区分大小写
不能用关键字命名
```