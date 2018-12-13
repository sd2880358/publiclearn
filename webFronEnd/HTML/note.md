# 前端课程课件

# 1. HTML (常用标签  网络的基本结构)
 
 - HTML 是用来描述网页的一种语言
 
    - 超文本标记语言(HyperTextMarkupLanguage)
    - HTML不是一种编程语言,而是一种标记语言
    - 标记语言是一套标记标签(MarkupTags)
    - HTML 文档包含了HTML 标签及文本内容
    - HTML文档也叫做web页面
# 1.1 HTML的作用

- 可以使用HTML来建立自己的web站点,HTML运行在浏览器上,由浏览器来解析

# 1.2 建立HTML文件

-  .html
- .htm

# 1.3 HTML注释

- <!--注释内容-->

# 1.4 HTML网页的基本结构
- <!DOCTYPE HTML> 声明HTML5 文件
- <html> 元素是网页的根元素
- <head> 元素包含了文档的元(meta)数据
- <body> 元素包含了课件的页面内容

# 1.5 HTML标签结构
- HTML标记标签通常被称为HTML标签(HTML tag)
    - HTML 标签是由尖括号包围的关键词
    - HTML 标签通常是成对出现的
    - 标签对中的第一个标签是开始标签,第二个标签是结束标签

<开始标签> 内容 </结束标签>

# 1.6 HTML的元素
- 'HTML标签'和'HTML元素'通常描述同样的意思,一个HTML元素包含了开始标签和结束标签

# 1.7 HTML 属性
- HTML元素可以设置属性
- 属性一般添加开始标签
- 属性一般以命名/值对的形式出现, 比如name='value'
    注意:
        - 属性用双引号引起来
        - 标签必须用小写字母
        - 双标签必须要有闭合标签
# 1.8 HTML常用标签
- HTML常用的块级标签(块级元素)
    `独占一行`
- 有语义的HTML的块级标记
    `有默认样式`
- 标题(heading)
    `通过h1-h6`
- 段落
    `通过p来定义
    br表示强制换行`
- 列表
    - 无序列表ul,li
        - 是一个项目的列表,列表项目使用粗体远点(典型的小黑点)进行标记
    - 有序列表 ol,li
        -也是一个项目的列表,列表项目使用数字进行标记
    - 自定义列表 dl, dt, dd (了解)
    注意:列表内部可以使用段落,换行符,图片,连接以及其他列表等等
- 表格常用属性
    - border 表框
    - cellpadding 内容举例表框的距离
    - cellspacing
    - rowspan 垂直合并(跨行显示)
    - colspan 水平合并(跨列显示)
    - align 内容水平对齐方式
    - valign 内容垂直对齐方式
- 无意义的块级元素div
    - 块元素独占一行

# 2. HTML常用的行级标签(行内元素)
- 不独占一行
## 有语义的函内元素
- HTML 链接 a标签
    -<a href="链接地址"> </a>
- HTML图像
    -<'img src=" 图片地址" alt=""">
- 文本标签
    - b标签 加粗
    - i标签 倾斜
## 无语意的行内元素
- span 标签 配合css使用

# 3 常用的实体字符
` gt; lt; copy; &nbsp;`
- &gt;大于号
- &lt; 小于号
- &copy;版权符号

# 4 表单标签
- 表单是一个包含表单的区域,通过form来定义
- 通过type属性定义不同类型的表单控件
    - text 普通文本输入框
    - password 密码输入框
    - radio 单选按钮
    - checked 多选按钮
    - select 下拉框
    - file 文件上传选框
    - textarea 文本区域
    - submit 提交按钮
    - reset 重置按钮
    - hidden 隐藏区域, 要和表单单一其提交的信息
- 常用属性
    `name 属性:表单项名, 用于存储内容
    value 属性: 输入的值
    disabled属性:禁用的属性
    readonly属性: 禁用的属性
    check.ed :选择指定默认选项
    placeholder: 提示`
- 注意:
    `form有两个必须存在的属性, action提交地址,method提交方式
    post: 通过request body 传参数, 参数不可见,参数没有大小限制
    get: 通过url进行传参,参数课件,不安全,有大小设置
    `
# 端口
- http 采用80 端口
-https 采用443端口