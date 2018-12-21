# 结构化文件存储

- xml, json
- 为了解决不同设备之间的信息交换
- xml
- json

# xml 文件
- xml, 可扩展标记语言
    - 标记语言: 语言中用< >括起来的文本字符串标记
    - 可扩展: 用户可以定义自己需要的标记
    - 例如:
        
            <Techaer>
                自定义标记Teacher
                在两个标记之间如何内容应该和Teacher有关
            </Teacher>
    - 是w3c组织制定的一个标准
    - xml描述的是数据本身,即数据的结构和语义
    - HTML 侧重点于如何显示web页面中的数据
    
- xml文档的构成
    - 处理器指令(可以认为一个文件只有一个处理指令)
        - 最多只有一行
        - 且必须在第一行
        - 内容是与xml本身处理起和相关的一些声明或者指令
        - 以xml关键字开头
            - 一般用于声明xml的版本和采用的编码
            - 版本用version 控制
            - 编码用encoding控制
    - 根元素(一个文件内只有一个根元素)
        - 在整个xml文件中,可以把ta看做一个树形结构
        - 有且只能一个
    - 子元素
    - 属性
        - 对标签本身进行说明
    - 内容
        - 表明标签所存储的信息
    - 注释
        - 起说明作用
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双横线
        - 三短横线只能出现在注释的开头而不能在结尾
        
                <name> <! -- wangdapeng -->可以
                <name <! -- wangdapeng -->> 不可以,注释在标签内
                <! -- my - name by - wang--> 可以
                <! -- my -- name -- by -- wang --> 不可以
                <! -- my - name --> 可以
                <! --- my - name --->  不可以
     - 保留字符的处理
        - xml 中使用的符号可能跟实际符号相冲突,典型的就是左右尖括号
        - 使用实体引用(EntityReference)来表示保留字符
                
                `<score> score&gt;80 </score>'
                
        - 把含有保留字符的部分放在CDATA块内部,CDATA块把内部信息视为不需要转义
                `<![CDATA[
                    select name,age
                    from Student
                    where score>80
                    ]]>`
        - 常用的转义的保留字符和应实体应用
            - & : &amp;
            - < : &lt;
            - > : &gt;
            - ' : &apos;
            - " : &quot;
            - 一共五个,每个实体应用都已&开头并且只以分好结尾
- xml标签的命名规则
    - Pascal命名法
    - 用单词表示,第一个字母大写
    - 大小写严格区分
    - 配对标签必须一致
- 命名空间
    - 为了防止命名冲突
        <Student>
            <Name> Lee </Name>
            <age> 19 </age>
        </Student>
        <Room>
            <Name> 2015 </Name>
        </Room>
    - 如果归并上述两个信息内容,会产生冲突
        <Schooler>
       
            <Name> Lee </Name>
            <age> 19 </age>
            <Name> 2015 </Name>
        </Schooler>
    - 为了避免冲突,需要给可能冲突元素添加命名空间
    - xmlns: xml name space 的缩写
        <Schooler xmlns: student='http://my_student' xmlns:room='http//my_room'>
       
            <student:Name> Lee <student/Name>
            <age> 19 </age>
            <room:Name> 2015 <room:/Name>
        </Schooler>
# xml 访问

## 读取
- xml读取分两大技术,SAX,DOM
- SAX(Simple API for XML)
    - 基于事件驱动的API
    - 利用SAX解析文档涉及到解析器和时间处理两部分
    - 特点:
        - 快
        - 流式读取
- DOM 
    - 是w3c规定的XML编程接口
    - 一个XML文件再缓存中以树形结构保存,读取
    - 用途    
        - 定位浏览xml任何一个节点信息
        - 添加删除相应内容
    - minidom
        - minidom.parse(filename):加载读取的xml文件,file也可以是xml代码
        - doc.documentElement:获取xml文档对象,一个xml文件只有一个对于的文档
    - tree
    