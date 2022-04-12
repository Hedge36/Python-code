# python-docx

一，docx模块

Python可以利用python-docx模块处理word文档，处理方式是面向对象的。也就是说python-docx模块会把word文档，文档中的段落、文本、字体等都看做对象，对对象进行处理就是对word文档的内容处理。

二，相关概念

如果需要读取word文档中的文字（一般来说，程序也只需要认识word文档中的文字信息），需要先了解python-docx模块的几个概念。

1，Document对象，表示一个word文档。

2，Paragraph对象，表示word文档中的一个段落

3，Paragraph对象的text属性，表示段落中的文本内容。

三，模块的安装和导入

需要注意，python-docx模块安装需要在cmd命令行中输入pip install python-docx，如下图表示安装成功（最后那句英文Successfully installed，成功地安装完成）

注意在导入模块时，用的是import docx。

```
from` `docx ``import` `Document``from` `docx.enum.text ``import` `WD_ALIGN_PARAGRAPH ``#设置对象居中、对齐等。``from` `docx.enum.text ``import` `WD_TAB_ALIGNMENT,WD_TAB_LEADER ``#设置制表符等``from` `docx.shared ``import` `Inches ``#设置图像大小``from` `docx.shared ``import` `Pt ``#设置像素、缩进等``from` `docx.shared ``import` `RGBColor ``#设置字体颜色``from` `docx.shared ``import` `Length ``#设置宽度
```

四，读取word文本

```
#-*- conding:utf-8 -*-` `import` `docx` `file``=``docx.Document(r``"F:\python从入门到放弃\7\2\wenjian.docx"``)` `print``(``'段落:'``+``str``(``len``(``file``.paragraphs)))``# ``# for para in file.paragraphs:``# print(para.text)`` ` `for` `i ``in` `range``(``len``(``file``.paragraphs)): `` ``print``(``"第"``+``str``(i)``+``"段的内容是："``+``file``.paragraphs[i].text)
```

五，写word文本

```
#-*- conding:utf-8 -*-` `import` `sys` `from` `docx ``import` `Document``from` `docx.shared ``import` `Inches` `def` `main():``# reload(sys)``# sys.setdefaultencoding('utf-8')`` ` ` ``# 创建文档对象`` ``document ``=` `Document()`` ` ` ``# 设置文档标题，中文要用unicode字符串`` ``document.add_heading(u``'我的一个新文档'``,``0``)`` ` ` ``# 往文档中添加段落`` ``p ``=` `document.add_paragraph(``'This is a paragraph having some '``)`` ``p.add_run(``'bold '``).bold ``=` `True`` ``p.add_run(``'and some '``)`` ``p.add_run(``'italic.'``).italic ``=` `True`` ` ` ``# 添加一级标题`` ``document.add_heading(u``'一级标题, level = 1'``,level ``=` `1``)`` ``document.add_paragraph(``'Intense quote'``,style ``=` `'IntenseQuote'``)`` ` ` ``# 添加无序列表`` ``document.add_paragraph(``'first item in unordered list'``,style ``=` `'ListBullet'``)`` ` ` ``# 添加有序列表`` ``document.add_paragraph(``'first item in ordered list'``,style ``=` `'ListNumber'``)`` ``document.add_paragraph(``'second item in ordered list'``,style ``=` `'ListNumber'``)`` ``document.add_paragraph(``'third item in ordered list'``,style ``=` `'ListNumber'``)`` ` ` ``# 添加图片，并指定宽度`` ``document.add_picture(``'cat.png'``,width ``=` `Inches(``2.25``))`` ` ` ``# 添加表格: 1行3列`` ``table ``=` `document.add_table(rows ``=` `1``,cols ``=` `3``)`` ``# 获取第一行的单元格列表对象`` ``hdr_cells ``=` `table.rows[``0``].cells`` ``# 为每一个单元格赋值`` ``# 注：值都要为字符串类型`` ``hdr_cells[``0``].text ``=` `'Name'`` ``hdr_cells[``1``].text ``=` `'Age'`` ``hdr_cells[``2``].text ``=` `'Tel'`` ``# 为表格添加一行`` ``new_cells ``=` `table.add_row().cells`` ``new_cells[``0``].text ``=` `'Tom'`` ``new_cells[``1``].text ``=` `'19'`` ``new_cells[``2``].text ``=` `'12345678'`` ` ` ``# 添加分页符`` ``document.add_page_break()`` ` ` ``# 往新的一页中添加段落`` ``p ``=` `document.add_paragraph(``'This is a paragraph in new page.'``)`` ` ` ``# 保存文档`` ``document.save(``'demo1.doc'``)`` ` `if` `__name__ ``=``=` `'__main__'``:`` ``main()
```

六，读取表格

```
#-*- conding:utf-8 -*-` `import` `docx` `doc ``=` `docx.Document(``'wenjian.docx'``)``for` `table ``in` `doc.tables: ``# 遍历所有表格`` ``print``(``'----table------'``)`` ``for` `row ``in` `table.rows: ``# 遍历表格的所有行`` ``# row_str = '\t'.join([cell.text for cell in row.cells]) # 一行数据`` ``# print row_str`` ``for` `cell ``in` `row.cells:``  ``print``(cell.text, ``'\t'``,)`` ``print``() ``#换行
```

七，添加段落

```
document``=``docx.Document() ``# 创建一个空白文档``document.styles[``'Normal'``].font.name ``=` `'宋体'` `# 设置西文字体``document.styles[``'Normal'``]._element.rPr.rFonts.``set``(qn(``'w:eastAsia'``), ``'宋体'``) ``# 设置中文字体 ``p ``=` `document.add_paragraph()  ``# 添加一个段落``p.paragraph_format.alignment ``=` `WD_ALIGN_PARAGRAPH.JUSTIFY  ``#  设置对齐方式``p.paragraph_format.line_spacing_rule ``=` `WD_LINE_SPACING.ONE_POINT_FIVE  ``#  设置行间距``p.paragraph_format.space_after ``=` `Pt(``0``) ``#  设置段后间距 ``run ``=` `p.add_run(``'content'``) ``#  延长段落``run.font.color.rgb ``=` `RGBColor(``255``, ``0``, ``0``)  ``#  设置字体颜色``run.font.size ``=` `Pt(``22``) ``# 设置字号``run.font.bold ``=` `True` `# 设置下划线
```

八，docx模块其它常用方法

字号与磅值的关系

| 字号 | 磅值 |
| :--- | :--- |
| 八号 | 5    |
| 七号 | 5.5  |
| 小六 | 6.5  |
| 六号 | 7.5  |
| 小五 | 9    |
| 五号 | 10.5 |
| 小四 | 12   |
| 四号 | 14   |
| 小三 | 15   |
| 三号 | 16   |
| 小二 | 18   |
| 二号 | 22   |
| 小一 | 24   |
| 一号 | 26   |
| 小初 | 36   |
| 初号 | 42   |

新增页眉

```
section``=``document.sections[``0``]``header``=``section.header``bt1``=``header.paragraphs[``0``]``bt1.text``=``'此处是页眉1'
```

新增头信息

```
t1``=``document.add_paragraph(``'此处Tetle信息'``,``'Title'``)
```

新增段落 及 向前插入段落

```
p1``=``document.add_paragraph(``'新增段落P1'``)``pin1``=``p1.insert_paragraph_before(``'在p1前插入段落pin1'``)
```

段落里设置参数样式 或 指定.style来设置参数

```
p2``=``document.add_paragraph(``'新增段落p2并设置style类型'``,style``=``'ListBullet'``)``p3``=``document.add_paragraph(``'新增段落p3并指定style类型'``)``p3.style``=``'ListBullet'
```

添加标题 可设置标题级别1-9

```
h1``=``document.add_heading(``'此处默认标题1'``)``h2``=``document.add_heading(``'此处添加标题2'``,level``=``2``)``h3``=``document.add_heading(``'此处添加标题3'``,level``=``3``)
```

设置字体

通过.add_run来设置字体: 加粗、斜体、大小、颜色、下划线

```
paragraph``=``document.add_paragraph()``r1``=``paragraph.add_run(``'通过.bold=True来设置粗体'``)``r1.bold``=``True``r1.style``=``'Emphasis'``r2``=``paragraph.add_run(``'也可以'``)``r3``=``paragraph.add_run(``'\n通过.italic=True来设置斜体，\n通过.font.size来设置字体大小,\n通过.font.color.rgb=RGBColor来设置字体颜色'``)``r3.italic``=``True``r3.font.size``=``Pt(``20``)``r3.font.color.rgb``=``RGBColor(``200``,``77``,``150``)
```

| 方法           | 作用                     |
| :------------- | :----------------------- |
| all_caps       | 全部大写字母             |
| bold           | 加粗                     |
| color          | 字体颜色                 |
| complex_script | 是否为“复杂代码”         |
| cs_bold        | “复杂代码”加粗           |
| cs_italic      | “复杂代码”斜体           |
| double_strike  | 双删除线                 |
| emboss         | 文本以凸出页面的方式出现 |
| hidden         | 隐藏                     |
| imprint        | 印记                     |
| italic         | 斜体                     |
| name           | 字体                     |
| no_proof       | 不验证语法错误           |
| outline        | 显示字符的轮廓           |
| shadow         | 阴影                     |
| small_caps     | 小型大写字母             |
| snap_to_grid   | 定义文档网格时对齐网络   |
| strike         | 删除线                   |
| subscript      | 下标                     |
| superscript    | 上标                     |
| underline      | 下划线                   |

设置居中、左右对齐、缩进、制表符

```
p4``=``document.add_paragraph(``'准备开始设置居中、左右对齐、缩进等'``)``p4.paragraph_format.alignment``=``WD_ALIGN_PARAGRAPH.CENTER
```

| 方法    | 作用       |
| :------ | :--------- |
| LEFT    | 左对齐     |
| CENTER  | 文字居中   |
| RIGHT   | 右对齐     |
| JUSTIFY | 本两端对齐 |

设置缩进

默认Inches(0.5)等于四个空格

```
p5``=``document.add_paragraph(``'content'``)``p5.paragraph_format.left_indent``=``Inches(``0.5``)
```

设置首行缩进

```
p5.paragraph_format.first_line_indent``=``Inches(``0.5``)
```

设置段落间距 分为段落前 和 段落后

```
p5.paragraph_format.space_before``=``Pt(``30``)``p5.paragraph_format.space_after``=``Pt(``12``)
```

设置段落行距当行距为最小值和固定值时，设置值单位是磅，用Pt；当行间距为多倍行距时，设置值为数值。

```
p5.paragraph_format.line_spacing``=``Pt(``30``)
```

| 方法           | 作用             |
| :------------- | :--------------- |
| SINGLE         | 单倍行距（默认） |
| ONE_POINT_FIVE | 1.5倍行距        |
| DOUBLE         | 2倍行距          |
| AT_LEAST       | 最小值           |
| EXACTLY        | 固定值           |
| MULTIPLE       | 多倍行距         |

```
paragraph.line_spacing_rule ``=` `WD_LINE_SPACING.EXACTLY ``#固定值``paragraph_format.line_spacing ``=` `Pt(``18``)   ``# 固定值18磅``paragraph.line_spacing_rule ``=` `WD_LINE_SPACING.MULTIPLE ``#多倍行距``paragraph_format.line_spacing ``=` `1.75
```

分页属性

```
p5.paragraph_format.keep_with_next ``=` `True
```

| 方法              | 作用       | 说明                                                       |
| :---------------- | :--------- | :--------------------------------------------------------- |
| widow_control     | 孤行控制   | 防止在页面顶端单独打印段落末行或在页面底端单独打印段落首行 |
| keep_with_next    | 与下段同页 | 防止在选中段落与后面一段间插入分页符                       |
| page_break_before | 段前分页   | 在选中段落前插入分页符                                     |
| keep_together     | 段中不分页 | 防止在段落中出现分页符                                     |

添加分页符

```
document.add_page_break()``p5``=``document.add_paragraph(``'.add_page_break()硬分页，即使文本未满'``)
```

添加表格、设置表格样式

```
table``=``document.add_table(rows``=``2``,cols``=``2``) ``table.style``=``'LightShading-Accent1'
```

选择表格内单元格、单元格赋值添加和改变内容

```
cell``=``table.cell(``0``,``1``)``cell.text``=``'通过cell.text()来添加内容'
```

选择表格的行，通过索引，然后索引单元格

```
row``=``table.rows[``1``]``row.cells[``0``].text``=``'通过.add_table（,）来添加表格'``row.cells[``1``].text``=``'通过for row in table.rows内嵌套 for cell in row.cells来循环输出表格内容'
```

for循环逐行输出表格内容

```
for` `row ``in` `table.rows: `` ``for` `cell ``in` `row.cells:`` ``print``(cell.text)
```

len表格内行列数

```
row_count``=``len``(table.rows)``col_count``=``len``(table.columns)``print``(row_count,col_count,``'现表格行列数'``)``row``=``table.add_row() ``#逐步添加行``print``(``len``(table.rows),``len``(table.columns),``'添加后表格行列数'``)
```

添加另一个表格 及 指定表格样式

```
table1``=``document.add_table(``1``,``3``)``table1.style``=``'LightShading-Accent2'` `#设置表格样式
```

填充 标题行

```
heading_cells``=``table1.rows[``0``].cells ``#获取 行列标``heading_cells[``0``].text``=``'Qtx'` `#为行列表内的cell单元格 赋值``heading_cells[``1``].text``=``'Sku'``heading_cells[``2``].text``=``'Des'
```

表格数据

```
items``=``(`` ``(``7``,``'1024'``,``'plush kitens'``),`` ``(``3``,``'2042'``,``'furbees'``),`` ``(``1``,``'1288'``,``'french poodle collars,deluxe'``)`` ``)
```

为每个项目添加数据行

```
for` `item ``in` `items:`` ``cells``=``table1.add_row().cells`` ``cells[``0``].text``=``str``(item[``0``]) `` ``cells[``1``].text``=``str``(item[``1``]) `` ``cells[``2``].text``=``str``(item[``2``])
```

添加图片

```
document.add_picture(``'002592.png'``,width``=``Inches(``2``))
```

调整图片大小，如下：

```
document.add_picture(``'demo.png'``, width``=``Inches(``1.0``), height``=``Inches(``1.0``))
```

若同时定义宽度和高度，则图片会被拉伸或压缩到指定大小；若仅定义宽度或高度，则图会自适应调整大小。

保存文档

```
document.save(``'test.docx'``)
```