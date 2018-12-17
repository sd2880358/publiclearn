# JS定时器

通过使用JavaScript,我们可以做到在一个设定的时间间隔之后来执行代码,而不是在函数被调用后立即执行. 我们称之为计时事件.

## 定时器在JavaScript中的作用

1. 制作动画
2. 异步操作(类似python的多线程操作)

## 定时器及类型
> setInterval()和setTimeout()是window对象的两个方法
>> setInterval() 间隔指定的毫秒不停的执行指定的代码
>> setTimeout() 暂停指定的毫秒数后执行指定的代码
```
setTimeout 只执行一次的定时器
clearTimeout 关闭只执行一次的定时器
setInterval 反复执行的定时器
cleatInterval 关闭反复执行的定时器

var time1=setTimeout(myalert,2000)
var time2=setInterval(myalert,2000)
clearTimeout(time1)
clearInterval(time2)

function myalert(){
    alert('ok!');
    }
```

# JS函数
* 第一种是function语句定义函数
```javascript
function abc() {
  
}

```
* 第二种方式在表达式重定义
```javascript

var add =function(a,b){
    return a+b;
}
//调用函数
add(3,4);

```
# arguments
```
在函数代码中,使用对象arguments,开发者无需明确指出参数名,就能访问他们.
例如,在函数sayHi()中,第一个参数是message.用arguments[0]
也可以访问这个值,即第一个参数的值(第一个参数位于0位置,第二个参数位于1位置,以此类推).
```

# 关于变量和参数问题:
```
函数外面定义的变量是全局变量,函数内部可以直接使用.
在函数内部没有使用var定义的变量则为全局标量.
*在函数内使用var关键字定义的变量是局部边变量,即出了函数外边无法获取.
js函数定义的参数没有默认值,(形参的默认值在之前只有新版火狐和google浏览器支持)

```