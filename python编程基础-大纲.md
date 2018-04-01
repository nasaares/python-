**python编程基础**

> 2018.4.1最后修改

# *第一部分  基础知识*

------

## 第1章  起步

​         --snip--

## 第2章  变量和简单数据类型

​         --snip--

## 第3章  列表简介  

​         --snip--

## 第4章  操作列表

​         --snip--

## 第5章  if语句

​         --snip--

##第6章  字典  

​         --snip--

```python
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")
```



## 第7章  用户输入与while循环

​         --snip--

## 第8章  函数

​         --snip--

## 第9章  类

​         --snip--

## 第10章  文件和异常

​         --snip--

## 第11章  测试代码

​         --snip--

# *第二部分  项目*

********

> 项目1  外星人入侵

## 第12章  武装飞船

​         --snip--

## 第13章  外星人

​         --snip--

##第14章  记分

​         --snip--

> 项目2  数据可视化

## 第15章  生成数据

​         --snip--

## 第16章  下载数据

​         --snip--

## 第17章  使用API

​         --snip--

> 项目3  web应用程序

## 第18章  Django入门

​         --snip--

## 第19章  用户帐户

​         --snip--

## 第20章  设计应用程序的样式并对其进行部署

​         --snip--

##  附录