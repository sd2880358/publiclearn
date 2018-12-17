# JS 对象

1. 使用原始的方法创建内置对象
```javascript
var myObject = new Object();
myObject.name = "lilei";
myObject.age = 18;
myObject.say = function(){...};
```
2. 直接创建自定义对象
```javascript
var student={name:"lilei",age:18,gender:"male"};
```
3. 使用自定义构造函数创建对象
```javascript
function pen(name,color,price){
    //对象的属性
    this.name = name;
    this.color = color;
    this.price= price;
    this.say = function(){
         
    };
}
```
# this 关键字
```
在对象的方法中使用,代表当前这个对象
意味着当对象调用这个方法是,方法中的this就代表着这个对象
```
# 遍历
```
for (var i in window){
    document.write(i+'---'window[i];}
    
```
# 关于类型
```
测试类型:
1. tyoeof() //global对象的其中一个方法,typeof()
2. 对象.construction; //查看当前对象的构造函数是谁;
if(arr.constructor == Array){
    alert('数组'); //数组推荐用这种方法,因为typeof得到的事object;
```
# js数组
数组就是一组数据的组合,JavaScript中,数组里面的数据可以是不同类型的.

* 定义数组的方法
```javascript
//对象的实例创建
var alist = new Array(1,2,3);
// 直接量创建
var alist = [1,2,3,4,'abc'];
```

## 操作数组中数据的方法
1. 获取数组的长度:aList.length;
```javascript
var a = [1,2,3,4];
a.length;
```
2. 用下标操作数组的某个数据:aList[]
```javascript
var a = [1,2,3,4];
a[0]='2';

```
3. push()和pop()从数组最后增加成员或删除成员
```javascript
var aList=[1,2,3,4,5];
aList.pop(5);
aLsit.pop();
```
4. unshift()和shift()从数组前面增加成员或删除成员
```javascript
var list1 = [1,2,3,4,5];
list1.shift();
```
5. splice()在数组中增加或删除成员
```javascript
var list = [1,2,3,4,5];
list.splice(2,1,7,8);//从第二个元素开始,删除一个元素,然后在此位置增加'7,8,9'三个元素
```
** 多维数组 **
多维数组指的是数组的成员也是数组的数组
```javascript
var list = [[1,2,3,4],[5,6,7,8]];
```
# js数学对象Math
```javascript
// 四舍五入
var res = Math.round(5.921);
//获得最大值
var res = Math.max(10,23,4,5,6123,5123);
// 获取最小值
var res = Math.min(12,315,,1231,56,6674);
//获取绝对值
var res = Math.abs(-100);
//向下取整
vat res = Math.floor(2.3);
//向上取整
var res = Math.ceil(2.4);
//幂运算
var res = Math.pow(2,4);
//开方运算
var res = Math.sqrt(9);
random ()//返回0-1之间的随机数;
```
# random 返回0-1之间的随机数
random 获取一个随机数返回0-1之间的随机小数有可能到0,但不会包括1
```javascript
//封装函数()
function rand(m,n){
    return Math.floor(Math.random()*(n-m+1)+m);
}
var res = rand(20,30);
```