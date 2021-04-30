# Matplotlib

##   All before

> **Docs url : https://matplotlib.org/3.1.1/contents.html**



## plt

### hist

```python
matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, 
                       cumulative=False, bottom=None, histtype='bar', align='mid', 
                       orientation='vertical', rwidth=None, log=False, color=None, 
                       label=None, stacked=False, data=None, **kwargs)
```

**Parameters:**

**x**				(n,) array or sequence of (n,) arrays

Input values, this takes either a single array or a sequence of arrays which are not required to be of the same length.

**bins**			int or sequence or str, default: `rcParams["hist.bins"]` (default: `10`)

If *bins* is an integer, it defines the number of equal-width bins in the range.

If *bins* is a sequence, it defines the bin edges, including the left edge of the first bin and the right edge of the last bin; in this case, bins may be unequally spaced. All but the last (righthand-most) bin is half-open. In other words, if *bins* is:

```
[1, 2, 3, 4]
```



then the first bin is `[1, 2)` (including 1, but excluding 2) and the second `[2, 3)`. The last bin, however, is `[3, 4]`, which *includes* 4.

If *bins* is a string, it is one of the binning strategies supported by [`numpy.histogram_bin_edges`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges): 'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', or 'sqrt'.

**range**			tuple or None, default: None

The lower and upper range of the bins. Lower and upper outliers are ignored. If not provided, *range* is `(x.min(), x.max())`. Range has no effect if *bins* is a sequence.

If *bins* is a sequence or *range* is specified, autoscaling is based on the specified bin range instead of the range of x.

**density**			bool, default: False(old attribute: normed)

If `True`, draw and return a probability density: each bin will display the bin's raw count divided by the total number of counts *and the bin width* (`density = counts / (sum(counts) * np.diff(bins))`), so that the area under the histogram integrates to 1 (`np.sum(density * np.diff(bins)) == 1`).

If *stacked* is also `True`, the sum of the histograms is normalized to 1.

**weights**			(n,) array-like or None, default: None

An array of weights, of the same shape as *x*. Each value in *x* only contributes its associated weight towards the bin count (instead of 1). If *density* is `True`, the weights are normalized, so that the integral of the density over the range remains 1.

This parameter can be used to draw a histogram of data that has already been binned, e.g. using [`numpy.histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram) (by treating each bin as a single point with a weight equal to its count)

```
counts, bins = np.histogram(data)
plt.hist(bins[:-1], bins, weights=counts)
```

(or you may alternatively use [`bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar)).

**cumulative**			bool or -1, default: False

If `True`, then a histogram is computed where each bin gives the counts in that bin plus all bins for smaller values. The last bin gives the total number of datapoints.

If *density* is also `True` then the histogram is normalized such that the last bin equals 1.

If *cumulative* is a number less than 0 (e.g., -1), the direction of accumulation is reversed. In this case, if *density* is also `True`, then the histogram is normalized such that the first bin equals 1.

**bottom	**			array-like, scalar, or None, default: None

Location of the bottom of each bin, ie. bins are drawn from `bottom` to `bottom + hist(x, bins)` If a scalar, the bottom of each bin is shifted by the same amount. If an array, each bin is shifted independently and the length of bottom must match the number of bins. If None, defaults to 0.

**histtype	**			{'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'

The type of histogram to draw.

- 'bar' is a traditional bar-type histogram. If multiple data are given the bars are arranged side by side.

- 'barstacked' is a bar-type histogram where multiple data are stacked on top of each other.

- 'step' generates a lineplot that is by default unfilled.

- 'stepfilled' generates a lineplot that is by default filled.

  **align**				{'left', 'mid', 'right'}, default: 'mid'

The horizontal alignment of the histogram bars.

- 'left': bars are centered on the left bin edges.

- 'mid': bars are centered between the bin edges.

- 'right': bars are centered on the right bin edges.

  **orientation**		{'vertical', 'horizontal'}, default: 'vertical'

If 'horizontal', [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh) will be used for bar-type histograms and the *bottom* kwarg will be the left edges.

**rwidth**						float or None, default: None

The relative width of the bars as a fraction of the bin width. If `None`, automatically compute the width.

Ignored if *histtype* is 'step' or 'stepfilled'.

**log	**						bool, default: False

If `True`, the histogram axis will be set to a log scale.

**color**						color or array-like of colors or None, default: None

Color or sequence of colors, one per dataset. Default (`None`) uses the standard line color sequence.

**label**						str or None, default: None

String, or sequence of strings to match multiple datasets. Bar charts yield multiple patches per dataset, but only the first gets the label, so that [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend) will work as expected.

**stacked	**				bool, default: False

If `True`, multiple data are stacked on top of each other If `False` multiple data are arranged side by side if histtype is 'bar' or on top of each other if histtype is 'step'



## Add text

### annotate

(1)annotate语法说明 ：

```
annotate(s='str' ,xy=(x,y) ,xytext=(l1,l2) ,..)
```

`s` 为注释文本内容 

`xy` 为被注释的坐标点

`xytext` 为注释文字的坐标位置

`xycoords` 参数如下:

> figure points          points from the lower left of the figure 点在图左下方
>
> figure pixels          pixels from the lower left of the figure 图左下角的像素
>
> figure fraction       fraction of figure from lower left 左下角数字部分
>
> axes points           points from lower left corner of axes 从左下角点的坐标
>
> axes pixels           pixels from lower left corner of axes 从左下角的像素坐标
>
> axes fraction        fraction of axes from lower left 左下角部分

`data`                     

use the coordinate system of the object being annotated(default) 使用的坐标系统被注释的对象（默认）

polar(theta,r)       if not native ‘data’ coordinates t

`extcoords` 设置注释文字偏移量

| 参数 | 坐标系 |
|----|----|
| 'figure points' | 距离图形左下角的点数量 |
| 'figure pixels' | 距离图形左下角的像素数量 |
| 'figure fraction' | 0,0 是图形左下角，1,1 是右上角 |
| 'axes points' | 距离轴域左下角的点数量 |
| 'axes pixels' | 距离轴域左下角的像素数量 |
| 'axes fraction' | 0,0 是轴域左下角，1,1 是右上角 |
| 'data' | 使用轴域数据坐标系 |

`arrowprops`  #箭头参数,参数类型为字典dict

> width           the width of the arrow in points                              点箭头的宽度
>
> headwidth   the width of the base of the arrow head in points  在点的箭头底座的宽度
>
> headlength  the length of the arrow head in points                   点箭头的长度

`shrink`          fraction of total length to ‘shrink’ from both ends  总长度为分数“缩水”从两端

`facecolor`     箭头颜色

bbox给标题增加外框 ，常用参数如下：

>   boxstyle方框外形
>
> facecolor(简写fc)背景颜色
>
> edgecolor(简写ec)边框线条颜色
>
> edgewidth边框线条大小





### text

语法说明

```python
text(x,y,string,fontsize=15,verticalalignment="top",horizontalalignment="right")
```

`x,y` : 表示坐标值上的值

`string` : 表示说明文字

`fontsize` : 表示字体大小

`verticalalignment` ：垂直对齐方式 ，参数：[ ‘center’ | ‘top’ | ‘bottom’ | ‘baseline’ ]

`horizontalalignment` ：水平对齐方式 ，参数：[ ‘center’ | ‘right’ | ‘left’ ]

`xycoords`选择指定的坐标轴系统:

> figure points          points from the lower left of the figure 点在图左下方
>
> figure pixels          pixels from the lower left of the figure 图左下角的像素
>
> figure fraction       fraction of figure from lower left 左下角数字部分
>
> axes points           points from lower left corner of axes 从左下角点的坐标
>
> axes pixels           pixels from lower left corner of axes 从左下角的像素坐标
>
> axes fraction        fraction of axes from lower left 左下角部分
>
> data                     use the coordinate system of the object being annotated(default) 使用的坐标系统被注释的对象（默认）
>
> polar(theta,r)       if not native ‘data’ coordinates t

`arrowprops`  #箭头参数,参数类型为字典dict

> width           the width of the arrow in points                              点箭头的宽度
>
> headwidth   the width of the base of the arrow head in points  在点的箭头底座的宽度
>
> headlength  the length of the arrow head in points                   点箭头的长度
>
> shrink          fraction of total length to ‘shrink’ from both ends  总长度为分数“缩水”从两端
>
> facecolor     箭头颜色

`bbox`给标题增加外框 ，常用参数如下：

> boxstyle方框外形
>
> facecolor(简写fc)背景颜色
>
> edgecolor(简写ec)边框线条颜色
>
> edgewidth边框线条大小