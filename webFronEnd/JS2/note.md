# JavaScript基本数据类型

## typeof函数获取一个变量的类型
```
- boolean - 如果变量是boolean类型的
- number - 如果变量是NUMBER类型的(整数,浮点数)
- string - 如果变量时string类型的(采用"",'')
- object - 如果变量时一种引用类型的或Null类型的
    如: newArray()/new string()...
- function -- 函数类型
- underfined - 如果变量时undefined类型的
```

# js数据类型转换

使用: Number() , parseInt和parseFloat() 做类型转换

```
Number()强转一个数值(包含整数和浮点数)
parseInt()强转整数
parseFloat()强转浮点数
```
函数isNaN()检测参数是否不是一个数字.结果返回布尔值.
 
 ## 可用的3中强制转换类型如下:
 ```
 Boolean(value) - 把给定的值转换成布尔值类型;
 数值转换布尔值为false:0,0.0,NaN;
 字符串转换为布尔值为false:"";
 对象转布尔值为false:null;
 Number(value) - 把给定的值转换成数字;
 String(value) - 把给定的值转换成数字;
 ```
 
# JS运算符
算数运算符
```
++,--,+,-
```
字符串连接
`+`
赋值运算
```
= += -= %+
```
比较运算符
```
< > >= <= == === != !==
```
逻辑运算符
`&& ,||, !`
位运算符
`^,&,|,<<,>>`
其他运算符
`?, :, 三元运算符`