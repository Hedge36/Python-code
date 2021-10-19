# Chapter1 Introductory

## 1.1 Composition

Now, let's have a deeper look at the components of a Matplotlib figure.

<img src="E:/工具/Typora/Temp/anatomy.png" alt="../../_images/anatomy.png" style="zoom:80%;" />

### `Figure`

> The **whole** figure. The figure keeps track of all the child `Axes`, a smattering of 'special' artists (titles, figure legends, etc), and the **canvas**. (Don't worry too much about the canvas, it is crucial as it is the object that actually does the drawing to get you your plot, but as the user it is more-or-less invisible to you). A figure can contain any number of `Axes`, but will typically have at least one.
>
> The easiest way to create a new figure is with pyplot:
>
> ```python
> fig = plt.figure()  # an empty figure with no Axes
> fig, ax = plt.subplots()  # a figure with a single Axes
> fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
> ```
>
> It's convenient to create the axes together with the figure, but you can also add axes later on, allowing for more complex axes layouts.

### `Axes`

> This is what you think of as 'a plot', it is the region of the image with the data space. A given figure can contain many Axes, but a given `Axes` object can only be in one `Figure`. The Axes contains two (or three in the case of 3D) `Axis` objects (be aware of the difference between **Axes** and **Axis**) which take care of the data limits (the data limits can also be controlled via the `axes.Axes.set_xlim()` and `axes.Axes.set_ylim()` methods). Each `Axes` has a title (set via `set_title()`), an x-label (set via `set_xlabel()`), and a y-label set via `set_ylabel()`).
>
> The `Axes` class and its member functions are the primary entry point to working with the OO interface.

### `Axis`

> These are the number-line-like objects. They take care of setting the graph limits and generating the ticks (the marks on the axis) and ticklabels (strings labeling the ticks). The location of the ticks is determined by a `Locator` object and the ticklabel strings are formatted by a `Formatter`. The combination of the correct `Locator` and `Formatter` gives very fine control over the tick locations and labels.

### `Artist`

> Basically, everything you can see on the figure is an artist (even the `Figure`, `Axes`, and `Axis` objects). This includes `Text` objects, `Line2D` objects, `collections` objects, `Patch` objects ... (you get the idea). When the figure is rendered, all of the artists are drawn to the **canvas**. Most Artists are tied to an Axes; such an Artist cannot be shared by multiple Axes, or moved from one to another.

---

## 1.2 Types of inputs

All of plotting functions expect `numpy.array` or `numpy.ma.masked_array` as input. <u>Classes that are 'array-like' such as `pandas` data objects and `numpy.matrix` may or may not work as intended. It is best to convert these to `numpy.array` objects prior to plotting.</u>

For example, to convert a `pandas.DataFrame`

```python
a = pandas.DataFrame(np.random.rand(4, 5), columns = list('abcde'))
a_asarray = a.values
```

and to convert a `numpy.matrix`

```python
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
```

---

## 1.3 The object-oriented interface and the pyplot interface

As noted above, there are essentially **two ways** to use Matplotlib:

> - Explicitly create figures and axes, and call methods on them (the "object-oriented (OO) style").
> - Rely on pyplot to automatically create and manage the figures and axes, and use pyplot functions for plotting.

So one can do (OO-style)

```python
x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
```

![Simple Plot](E:/工具/Typora/Temp/sphx_glr_usage_003.png)

Out:

```python
<matplotlib.legend.Legend object at 0x7f1c6b1537f0>
```

or (pyplot-style)

```python
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
```

![Simple Plot](E:/工具/Typora/Temp/sphx_glr_usage_004.png)

Out:

```python
<matplotlib.legend.Legend object at 0x7f1c6be86bb0>
```

In addition, there is a third approach, for the case when embedding Matplotlib in a GUI application, which completely drops pyplot, even for figure creation. We won't discuss it here; see the corresponding section in the gallery for more info **(Embedding Matplotlib in graphical user interfaces)**.

Matplotlib's documentation and examples use both the OO and the pyplot approaches (which are equally powerful), and you should feel free to use either (however, it is preferable pick one of them and stick to it, instead of mixing them). In general, we suggest to restrict pyplot to interactive plotting (e.g., in a Jupyter notebook), and to prefer the OO-style for non-interactive plotting (in functions and scripts that are intended to be reused as part of a larger project).

> **Note**
>
> In older examples, you may find examples that instead used the so-called `pylab` interface, via `from pylab import *`. This star-import imports everything both from pyplot and from `numpy`, so that one could do
>
> ```python
> x = linspace(0, 2, 100)
> plot(x, x, label='linear')
> ```
>
> for an even more MATLAB-like style. This approach is strongly discouraged nowadays and deprecated. It is only mentioned here because you may still encounter it in the wild.

Typically one finds oneself making the same plots over and over again, but with different data sets, which leads to needing to write specialized functions to do the plotting. The recommended function signature is something like:

```python
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
```

which you would then use as:

```python
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})
```

!usage

Out:

```python
[<matplotlib.lines.Line2D object at 0x7f1c6c06dd30>]
```

or if you wanted to have 2 sub-plots:

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
```

!usage

Out:

```python
[<matplotlib.lines.Line2D object at 0x7f1c6c1ada00>]
```

For these simple examples this style seems like overkill, however once the graphs get slightly more complex it pays off.

## 1.4 Backends

### What is a backend?

A lot of documentation on the website and in the mailing lists refers to the "backend" and many new users are confused by this term. Matplotlib targets many different use cases and output formats. Some people use Matplotlib interactively from the python shell and have plotting windows pop up when they type commands. Some people run Jupyter notebooks and draw inline plots for quick data analysis. Others embed Matplotlib into graphical user interfaces like PyQt or PyGObject to build rich applications. Some people use Matplotlib in batch scripts to generate postscript images from numerical simulations, and still others run web application servers to dynamically serve up graphs.

To support all of these use cases, Matplotlib can target different outputs, and each of these capabilities is called a backend; the "frontend" is the user facing code, i.e., the plotting code, whereas the "backend" does all the hard work behind-the-scenes to make the figure. There are two types of backends: user interface backends (for use in PyQt/PySide, PyGObject, Tkinter, wxPython, or macOS/Cocoa); also referred to as "interactive backends") and hardcopy backends to make image files (PNG, SVG, PDF, PS; also referred to as "non-interactive backends").

### Selecting a backend

There are three ways to configure your backend:

> 1. The `rcParams["backend"]` parameter in your `matplotlibrc` file
> 2. The `MPLBACKEND` environment variable
> 3. The function `matplotlib.use()`

A more detailed description is given below.

If multiple of these are configurations are present, the last one from the list takes precedence; e.g. calling `matplotlib.use()` will override the setting in your `matplotlibrc`.

If no backend is explicitly set, Matplotlib automatically detects a usable backend based on what is available on your system and on whether a GUI event loop is already running. On Linux, if the environment variable `DISPLAY` is unset, the "event loop" is identified as "headless", which causes a fallback to a noninteractive backend (agg); in all other cases, an interactive backend is preferred (usually, at least tkagg will be available).

Here is a detailed description of the configuration methods:

1. Setting `rcParams["backend"]` in your `matplotlibrc` file:

   ```
   backend : qt5agg   # use pyqt5 with antigrain (agg) rendering
   ```

   See also Customizing Matplotlib with style sheets and rcParams.

2. Setting the `MPLBACKEND` environment variable:

   You can set the environment variable either for your current shell or for a single script.

   On Unix:

   ```
   > export MPLBACKEND=qt5agg
   > python simple_plot.py

   > MPLBACKEND=qt5agg python simple_plot.py
   ```

   On Windows, only the former is possible:

   ```
   > set MPLBACKEND=qt5agg
   > python simple_plot.py
   ```

   Setting this environment variable will override the `backend` parameter in _any_ `matplotlibrc`, even if there is a `matplotlibrc` in your current working directory. Therefore, setting `MPLBACKEND` globally, e.g. in your `.bashrc` or `.profile`, is discouraged as it might lead to counter-intuitive behavior.

3. If your script depends on a specific backend you can use the function `matplotlib.use()`:

   ```python
   import matplotlib
   matplotlib.use('qt5agg')
   ```

   This should be done before any figure is created, otherwise Matplotlib may fail to switch the backend and raise an ImportError.

   Using `use` will require changes in your code if users want to use a different backend. Therefore, you should avoid explicitly calling `use` unless absolutely necessary.

### The builtin backends

By default, Matplotlib should automatically select a default backend which allows both interactive work and plotting from scripts, with output to the screen and/or to a file, so at least initially, you will not need to worry about the backend. <u>The most common exception is if your Python distribution comes without `tkinter` and you have no other GUI toolkit installed. This happens on certain Linux distributions, where you need to install a Linux package named `python-tk` (or similar).</u>

If, however, you want to write graphical user interfaces, or a web application server (Embedding in a web application server (Flask)), or need a better understanding of what is going on, read on. To make things a little more customizable for graphical user interfaces, Matplotlib separates the concept of the renderer (the thing that actually does the drawing) from the canvas (the place where the drawing goes). The canonical renderer for user interfaces is `Agg` which uses the Anti-Grain Geometry C++ library to make a raster (pixel) image of the figure; it is used by the `Qt5Agg`, `Qt4Agg`, `GTK3Agg`, `wxAgg`, `TkAgg`, and `macosx` backends. An alternative renderer is based on the Cairo library, used by `Qt5Cairo`, `Qt4Cairo`, etc.

For the rendering engines, one can also distinguish between vector or raster renderers. Vector graphics languages issue drawing commands like "draw a line from this point to this point" and hence are scale free, and raster backends generate a pixel representation of the line whose accuracy depends on a DPI setting.

Here is a summary of the Matplotlib renderers (there is an eponymous backend for each; these are _non-interactive backends_, capable of writing to a file):

| Renderer | Filetypes         | Description                                                                 |
| -------- | ----------------- | --------------------------------------------------------------------------- |
| AGG      | png               | raster graphics -- high quality images using the Anti-Grain Geometry engine |
| PDF      | pdf               | vector graphics -- Portable Document Format                                 |
| PS       | ps, eps           | vector graphics -- Postscript output                                        |
| SVG      | svg               | vector graphics -- Scalable Vector Graphics                                 |
| PGF      | pgf, pdf          | vector graphics -- using the pgf package                                    |
| Cairo    | png, ps, pdf, svg | raster or vector graphics -- using the Cairo library                        |

To save plots using the non-interactive backends, use the `matplotlib.pyplot.savefig('filename')` method.

And here are the user interfaces and renderer combinations supported; these are _interactive backends_, capable of displaying to the screen and of using appropriate renderers from the table above to write to a file:

| Backend   | Description                                                                                                                                         |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Qt5Agg    | Agg rendering in a Qt5 canvas (requires PyQt5). This backend can be activated in IPython with `%matplotlib qt5`.                                    |
| ipympl    | Agg rendering embedded in a Jupyter widget. (requires ipympl). This backend can be enabled in a Jupyter notebook with `%matplotlib ipympl`.         |
| GTK3Agg   | Agg rendering to a GTK 3.x canvas (requires PyGObject, and pycairo or cairocffi). This backend can be activated in IPython with `%matplotlib gtk3`. |
| macosx    | Agg rendering into a Cocoa canvas in OSX. This backend can be activated in IPython with `%matplotlib osx`.                                          |
| TkAgg     | Agg rendering to a Tk canvas (requires TkInter). This backend can be activated in IPython with `%matplotlib tk`.                                    |
| nbAgg     | Embed an interactive figure in a Jupyter classic notebook. This backend can be enabled in Jupyter notebooks via `%matplotlib notebook`.             |
| WebAgg    | On `show()` will start a tornado server with an interactive figure.                                                                                 |
| GTK3Cairo | Cairo rendering to a GTK 3.x canvas (requires PyGObject, and pycairo or cairocffi).                                                                 |
| Qt4Agg    | Agg rendering to a Qt4 canvas (requires PyQt4 or `pyside`). This backend can be activated in IPython with `%matplotlib qt4`.                        |
| wxAgg     | Agg rendering to a wxWidgets canvas (requires wxPython 4). This backend can be activated in IPython with `%matplotlib wx`.                          |

**Note**

> The names of builtin backends case-insensitive; e.g., 'Qt5Agg' and 'qt5agg' are equivalent.

#### ipympl

The Jupyter widget ecosystem is moving too fast to support directly in Matplotlib. To install ipympl

```shell
pip install ipympl
jupyter nbextension enable --py --sys-prefix ipympl
```

or

```shell
conda install ipympl -c conda-forge
```

See jupyter-matplotlib for more details.

#### How do I select PyQt4 or PySide?

The `QT_API` environment variable can be set to either `pyqt` or `pyside` to use `PyQt4` or `PySide`, respectively.

Since the default value for the bindings to be used is `PyQt4`, Matplotlib first tries to import it. If the import fails, it tries to import `PySide`.

### Using non-builtin backends

More generally, any importable backend can be selected by using any of the methods above. If `name.of.the.backend` is the module containing the backend, use `module://name.of.the.backend` as the backend name, e.g. `matplotlib.use('module://name.of.the.backend')`.

## 1.5 Interactive Mode

Use of an interactive backend (see What is a backend?) permits--but does not by itself require or ensure--plotting to the screen. Whether and when plotting to the screen occurs, and whether a script or shell session continues after a plot is drawn on the screen, depends on the functions and methods that are called, and on a state variable that determines whether Matplotlib is in "interactive mode". The default Boolean value is set by the `matplotlibrc` file, and may be customized like any other configuration parameter (see Customizing Matplotlib with style sheets and rcParams). It may also be set via `matplotlib.interactive()`, and its value may be queried via `matplotlib.is_interactive()`. Turning interactive mode on and off in the middle of a stream of plotting commands, whether in a script or in a shell, is rarely needed and potentially confusing. In the following, we will assume all plotting is done with interactive mode either on or off.

**Note**

> Major changes related to interactivity, and in particular the role and behavior of `show()`, were made in the transition to Matplotlib version 1.0, and bugs were fixed in 1.0.1. Here we describe the version 1.0.1 behavior for the primary interactive backends, with the partial exception of _macosx_.
>
> Interactive mode may also be turned on via `matplotlib.pyplot.ion()`, and turned off via `matplotlib.pyplot.ioff()`.

**Note**

> Interactive mode works with suitable backends in ipython and in the ordinary python shell, but it does _not_ work in the IDLE IDE. If the default backend does not support interactivity, an interactive backend can be explicitly activated using any of the methods discussed in What is a backend?

### Interactive example

From an ordinary python prompt, or after invoking ipython with no options, try this:

```python
import matplotlib.pyplot as plt
plt.ion()
plt.plot([1.6, 2.7])
```

This will pop up a plot window. Your terminal prompt will remain active, so that you can type additional commands such as:

```python
plt.title("interactive test")
plt.xlabel("index")
```

On most interactive backends, the figure window will also be updated if you change it via the object-oriented interface. E.g. get a reference to the `Axes` instance, and call a method of that instance:

```python
ax = plt.gca()
ax.plot([3.1, 2.2])
```

If you are using certain backends (like `macosx`), or an older version of Matplotlib, you may not see the new line added to the plot immediately. In this case, you need to explicitly call `draw()` in order to update the plot:

```python
plt.draw()
```

### Non-interactive example

Start a fresh session as in the previous example, but now turn interactive mode off:

```python
import matplotlib.pyplot as plt
plt.ioff()
plt.plot([1.6, 2.7])
```

Nothing happened--or at least nothing has shown up on the screen (unless you are using _macosx_ backend, which is anomalous). To make the plot appear, you need to do this:

```python
plt.show()
```

Now you see the plot, but your terminal command line is unresponsive; `pyplot.show()` _blocks_ the input of additional commands until you manually kill the plot window.

What good is this--being forced to use a blocking function? Suppose you need a script that plots the contents of a file to the screen. You want to look at that plot, and then end the script. Without some blocking command such as `show()`, the script would flash up the plot and then end immediately, leaving nothing on the screen.

In addition, non-interactive mode delays all drawing until `show()` is called; this is more efficient than redrawing the plot each time a line in the script adds a new feature.

Prior to version 1.0, `show()` generally could not be called more than once in a single script (although sometimes one could get away with it); for version 1.0.1 and above, this restriction is lifted, so one can write a script like this:

```python
import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
```

This makes three plots, one at a time. I.e., the second plot will show up once the first plot is closed.

### Summary

> In interactive mode, pyplot functions automatically draw to the screen.
>
> When plotting interactively, if using object method calls in addition to pyplot functions, then call `draw()` whenever you want to refresh the plot.
>
> Use non-interactive mode in scripts in which you want to generate one or more figures and display them before ending or generating a new set of figures. In that case, use `show()` to display the figure(s) and to block execution until you have manually destroyed them.

---

## 1.6 Performance

Whether exploring data in interactive mode or programmatically saving lots of plots, rendering performance can be a painful bottleneck in your pipeline. Matplotlib provides a couple ways to greatly reduce rendering time at the cost of a slight change (to a settable tolerance) in your plot's appearance. The methods available to reduce rendering time depend on the type of plot that is being created.

### Line segment simplification

For plots that have line segments (e.g. typical line plots, outlines of polygons, etc.), rendering performance can be controlled by `rcParams"path.simplify"]` (default: `True`) and `rcParams["path.simplify_threshold"]` (default: `0.111111111111`), which can be defined e.g. in the `matplotlibrc` file (see [Customizing Matplotlib with style sheets and rcParams for more information about the `matplotlibrc` file). `rcParams["path.simplify"]` (default: `True`) is a boolean indicating whether or not line segments are simplified at all. `rcParams["path.simplify_threshold"]` (default: `0.111111111111`) controls how much line segments are simplified; higher thresholds result in quicker rendering.

The following script will first display the data without any simplification, and then display the same data with simplification. Try interacting with both of them:

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()
```

Matplotlib currently defaults to a conservative simplification threshold of `1/9`. If you want to change your default settings to use a different value, you can change your `matplotlibrc` file. Alternatively, you could create a new style for interactive plotting (with maximal simplification) and another style for publication quality plotting (with minimal simplification) and activate them as necessary. See Customizing Matplotlib with style sheets and rcParams for instructions on how to perform these actions.

The simplification works by iteratively merging line segments into a single vector until the next line segment's perpendicular distance to the vector (measured in display-coordinate space) is greater than the `path.simplify_threshold` parameter.

**Note**

> Changes related to how line segments are simplified were made in version 2.1. Rendering time will still be improved by these parameters prior to 2.1, but rendering time for some kinds of data will be vastly improved in versions 2.1 and greater.

### Marker simplification

Markers can also be simplified, albeit less robustly than line segments. Marker simplification is only available to `Line2D` objects (through the `markevery` property). Wherever `Line2D` construction parameters are passed through, such as `matplotlib.pyplot.plot()` and `matplotlib.axes.Axes.plot()`, the `markevery` parameter can be used:

```python
plt.plot(x, y, markevery=10)
```

The `markevery` argument allows for naive subsampling, or an attempt at evenly spaced (along the _x_ axis) sampling. See the Markevery Demo for more information.

### Splitting lines into smaller chunks

If you are using the Agg backend (see What is a backend?), then you can make use of `rcParams["agg.path.chunksize"]` (default: `0`) This allows you to specify a chunk size, and any lines with greater than that many vertices will be split into multiple lines, each of which has no more than `agg.path.chunksize` many vertices. (Unless `agg.path.chunksize` is zero, in which case there is no chunking.) For some kind of data, chunking the line up into reasonable sizes can greatly decrease rendering time.

The following script will first display the data without any chunk size restriction, and then display the same data with a chunk size of 10,000. The difference can best be seen when the figures are large, try maximizing the GUI and then interacting with them:

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['path.simplify_threshold'] = 1.0

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()
```

### Legends

The default legend behavior for axes attempts to find the location that covers the fewest data points (`loc='best'`). _This can be <u>a very expensive computation</u> if there are lots of data points. In this case, you may want to provide a specific location._

### Using the _fast_ style

The _fast_ style can be used to automatically set simplification and chunking parameters to reasonable settings to speed up plotting large amounts of data. It can be used simply by running:

```python
import matplotlib.style as mplstyle
mplstyle.use('fast')
```

It is very lightweight, so it plays nicely with other styles, just make sure the fast style is applied last so that other styles do not overwrite the settings:

```python
mplstyle.use(['dark_background', 'ggplot', 'fast'])
```

# Chapter2 Pyplot

## Intro to pyplot

`matplotlib.pyplot` is a collection of functions that make matplotlib work like MATLAB. Each `pyplot` function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that "axes" here and in most places in the documentation refers to the _axes_ part of a figure and not the strict mathematical term for more than one axis).

**Note**

> the pyplot API is generally less-flexible than the object-oriented API. Most of the function calls you see here can also be called as methods from an `Axes` object. We recommend browsing the tutorials and examples to see how this works.

Generating visualizations with pyplot is very quick:

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

![pyplot](E:/工具/Typora/Temp/sphx_glr_pyplot_001.png)

You may be wondering why the x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single list or array to `plot`, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, the default x vector has the same length as y but starts with 0. Hence the x data are `[0, 1, 2, 3]`.

`plot` is a versatile function, and will take an arbitrary number of arguments. For example, to plot x versus y, you can write:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
```

![pyplot](E:/工具/Typora/Temp/sphx_glr_pyplot_002.png)

Out:

```python
[<matplotlib.lines.Line2D object at 0x7f1c6bee4940>]
```

### Formatting the style of your plot

For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. For example, to plot the above with red circles, you would issue

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

![pyplot](E:/工具/Typora/Temp/sphx_glr_pyplot_003.png)

See the `plot` documentation for a complete list of line styles and format strings. The `axis` function in the example above takes a list of `[xmin, xmax, ymin, ymax]` and specifies the viewport of the axes.

If matplotlib were limited to working with lists, it would be fairly useless for numeric processing. Generally, you will use numpy arrays. In fact, all sequences are converted to numpy arrays internally. The example below illustrates plotting several lines with different format styles in one function call using arrays.

```python
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

![pyplot](E:/工具/Typora/Temp/sphx_glr_pyplot_004.png)

## Plotting with keyword strings

There are some instances where you have data in a format that lets you access particular variables with strings. For example, with `numpy.recarray` or `pandas.DataFrame`.

Matplotlib allows you provide such an object with the `data` keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
```

![pyplot](E:/工具/Typora/Temp/sphx_glr_pyplot_005.png)

## Plotting with categorical variables

It is also possible to create a plot using categorical variables. Matplotlib allows you to pass categorical variables directly to many plotting functions. For example:

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```

![Categorical Plotting](E:/工具/Typora/Temp/sphx_glr_pyplot_006.png)

## Controlling line properties

Lines have many attributes that you can set: linewidth, dash style, antialiased, etc; see [matplotlib.lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D). There are several ways to set line properties

- Use keyword args:

  ```python
  plt.plot(x, y, linewidth=2.0)
  ```

- Use the setter methods of a `Line2D` instance. `plot` returns a list of `Line2D` objects; e.g., `line1, line2 = plot(x1, y1, x2, y2)`. In the code below we will suppose that we have only one line so that the list returned is of length 1. We use tuple unpacking with `line,` to get the first element of that list:

  ```python
  line, = plt.plot(x, y, '-')
  line.set_antialiased(False) # turn off antialiasing
  ```

- Use `setp`. The example below uses a MATLAB-style function to set multiple properties on a list of lines. `setp` works transparently with a list of objects or a single object. You can either use python keyword arguments or MATLAB-style string/value pairs:

  ```python
  lines = plt.plot(x1, y1, x2, y2)
  # use keyword args
  plt.setp(lines, color='r', linewidth=2.0)
  # or MATLAB style string value pairs
  plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
  ```

Here are the available `Line2D` properties.

| Property               | Value Type                                        |
| ---------------------- | ------------------------------------------------- | --------- | --------------- | ----- | ---------------- | ----- | ------- |
| alpha                  | float                                             |
| animated               | [True \| False]                                   |
| antialiased or aa      | [True \| False]                                   |
| clip_box               | a matplotlib.transform.Bbox instance              |
| clip_on                | [True \| False]                                   |
| clip_path              | a Path instance and a Transform instance, a Patch |
| color or c             | any matplotlib color                              |
| contains               | the hit testing function                          |
| dash_capstyle          | [`'butt'`                                         | `'round'` | `'projecting'`] |
| dash_joinstyle         | [`'miter'`                                        | `'round'` | `'bevel'`]      |
| dashes                 | sequence of on/off ink in points                  |
| data                   | (np.array xdata, np.array ydata)                  |
| figure                 | a matplotlib.figure.Figure instance               |
| label                  | any string                                        |
| linestyle or ls        | [ `'-'`                                           | `'--'`    | `'-.'`          | `':'` | `'steps'` \|...] |
| linewidth or lw        | float value in points                             |
| marker                 | [ `'+'`                                           | `','`     | `'.'`           | `'1'` | `'2'`            | `'3'` | `'4'` ] |
| markeredgecolor or mec | any matplotlib color                              |
| markeredgewidth or mew | float value in points                             |
| markerfacecolor or mfc | any matplotlib color                              |
| markersize or ms       | float                                             |
| markevery              | [ None \| integer \| (startind, stride) ]         |
| picker                 | used in interactive line selection                |
| pickradius             | the line pick selection radius                    |
| solid_capstyle         | [`'butt'`                                         | `'round'` | `'projecting'`] |
| solid_joinstyle        | [`'miter'`                                        | `'round'` | `'bevel'`]      |
| transform              | a matplotlib.transforms.Transform instance        |
| visible                | [True \| False]                                   |
| xdata                  | np.array                                          |
| ydata                  | np.array                                          |
| zorder                 | any number                                        |

> To get a list of settable line properties, call the `setp` function with a line or lines as argument.

```python
In [69]: lines = plt.plot([1, 2, 3])

In [70]: plt.setp(lines)
  alpha: float
  animated: [True | False]
  antialiased or aa: [True | False]
  ...snip
```

## Working with multiple figures and axes

MATLAB, and `pyplot`, have the concept of the current figure and the current axes. All plotting functions apply to the current axes. The function `gca` returns the current axes (a `matplotlib.axes.Axes` instance), and `gcf` returns the current figure (a `matplotlib.figure.Figure` instance). Normally, you don't have to worry about this, because it is all taken care of behind the scenes. Below is a script to create two subplots.

```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```

![pyplot](E:/工具/Typora/Temp/sphx_glr_pyplot_007.png)

The `figure` call here is optional because a figure will be created if none exists, just as an axes will be created (equivalent to an explicit `subplot()` call) if none exists. The `subplot` call specifies `numrows, numcols, plot_number` where `plot_number` ranges from 1 to `numrows*numcols`. ***The commas in the subplot call are optional if `numrows*numcols<10`\*.** So `subplot(211)` is identical to `subplot(2, 1, 1)`.

You can create an arbitrary number of subplots and axes. If you want to place an axes manually, i.e., not on a rectangular grid, use `axes`, which allows you to specify the location as `axes(left, bottom, width, height])` where all values are in fractional (0 to 1) coordinates. See [Axes Demo for an example of placing axes manually and Basic Subplot Demo for an example with lots of subplots.

You can create multiple figures by using multiple `figure` calls with an increasing figure number. Of course, each figure can contain as many axes and subplots as your heart desires:

```python
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot() by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
```

You can clear the current figure with `clf` and the current axes with `cla`. If you find it annoying that states (specifically the current image, figure and axes) are being maintained for you behind the scenes, don't despair: this is just a thin stateful wrapper around an object oriented API, which you can use instead (see Artist tutorial)

If you are making lots of figures, you need to be aware of one more thing: the memory required for a figure is not completely released until the figure is explicitly closed with `close`. Deleting all references to the figure, and/or using the window manager to kill the window in which the figure appears on the screen, is not enough, because pyplot maintains internal references until `close` is called.

## Working with text

`text` can be used to add text in an arbitrary location, and `xlabel`, `ylabel` and `title` are used to add text in the indicated locations (see Text in Matplotlib Plots for a more detailed example)

```python
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

![Histogram of IQ](E:/工具/Typora/Temp/sphx_glr_pyplot_008.png)

All of the `text` functions return a `matplotlib.text.Text` instance. Just as with lines above, you can customize the properties by passing keyword arguments into the text functions or using `setp`:

```python
t = plt.xlabel('my data', fontsize=14, color='red')
```

These properties are covered in more detail in Text properties and layout.

### Using mathematical expressions in text

> matplotlib accepts LaTeX equation expressions in any text expression. For example to write the expression σi=15σi=15 in the title, you can write a TeX expression surrounded by dollar signs.

```python
plt.title(r'$\sigma_i=15$')
```

The `r` preceding the title string is important -- it signifies that the string is a _raw_ string and not to treat backslashes as python escapes. matplotlib has a built-in TeX expression parser and layout engine, and ships its own math fonts -- for details see Writing mathematical expressions. Thus you can use mathematical text across platforms without requiring a TeX installation. For those who have LaTeX and dvipng installed, you can also use LaTeX to format your text and incorporate the output directly into your display figures or saved postscript -- see Text rendering With LaTeX.

### Annotating text

> The uses of the basic `text` function above place text at an arbitrary position on the Axes. A common use for text is to annotate some feature of the plot, and the `annotate` method provides helper functionality to make annotations easy. In an annotation, there are two points to consider: the location being annotated represented by the argument `xy` and the location of the text `xytext`. Both of these arguments are `(x, y)` tuples.

```python
ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()
```

![pyplot](E:/工具/Typora/Temp/sphx_glr_pyplot_009.png)

In this basic example, both the `xy` (arrow tip) and `xytext` locations (text location) are in data coordinates. There are a variety of other coordinate systems one can choose -- see Basic annotation and Advanced Annotations for details. More examples can be found in Annotating Plots.

## Logarithmic and other nonlinear axes

> `matplotlib.pyplot` supports not only linear axis scales, but also logarithmic and logit scales. This is commonly used if data spans many orders of magnitude. Changing the scale of an axis is easy:

```python
plt.xscale('log')
```

An example of four plots with the same data and different scales for the y axis is shown below.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
```

![linear, log, symlog, logit](E:/工具/Typora/Temp/sphx_glr_pyplot_010.png)

It is also possible to add your own scale, see Developer's guide for creating scales and transformations for details.

# Chapter3 Sample

## Sample plots in Matplotlib

> Here you'll find a host of example plots with the code that generated them.
>
> You can find the source code in UsageGuide/Demo3.ipnb.

## Line Plot

Here's how to create a line plot with text labels using `plot()`.

[![../../_images/sphx_glr_simple_plot_0011.png](E:/工具/Typora/Temp/sphx_glr_simple_plot_0011.png)](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)

Simple Plot

## Multiple subplots in one figure

Multiple axes (i.e. subplots) are created with the `subplot()` function:

[![../../_images/sphx_glr_subplot_0011.png](E:/工具/Typora/Temp/sphx_glr_subplot_0011.png)](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Subplot

## Images

Matplotlib can display images (assuming equally spaced horizontal dimensions) using the `imshow()` function.

[![../../_images/sphx_glr_image_demo_0031.png](E:/工具/Typora/Temp/sphx_glr_image_demo_0031.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html)

Example of using `imshow()` to display a CT scan

## Contouring and pseudocolor

The `pcolormesh()` function can make a colored representation of a two-dimensional array, even if the horizontal dimensions are unevenly spaced. The `contour()` function is another way to represent the same data:

[![../../_images/sphx_glr_pcolormesh_levels_0011.png](E:/工具/Typora/Temp/sphx_glr_pcolormesh_levels_0011.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

Example comparing `pcolormesh()` and `contour()` for plotting two-dimensional data

## Histograms

The `hist()` function automatically generates histograms and returns the bin counts or probabilities:

[![../../_images/sphx_glr_histogram_features_0011.png](E:/工具/Typora/Temp/sphx_glr_histogram_features_0011.png)](https://matplotlib.org/stable/gallery/statistics/histogram_features.html)

Histogram Features

## Paths

You can add arbitrary paths in Matplotlib using the `matplotlib.path` module:

[![../../_images/sphx_glr_path_patch_0011.png](E:/工具/Typora/Temp/sphx_glr_path_patch_0011.png)](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html)

Path Patch

## Three-dimensional plotting

The mplot3d toolkit (see Getting started and 3D plotting has support for simple 3D graphs including surface, wireframe, scatter, and bar charts.

[![../../_images/sphx_glr_surface3d_0011.png](E:/工具/Typora/Temp/sphx_glr_surface3d_0011.png)](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)

Surface3d

Thanks to John Porter, Jonathon Taylor, Reinier Heeres, and Ben Root for the `mplot3d` toolkit. This toolkit is included with all standard Matplotlib installs.

## Streamplot

The `streamplot()` function plots the streamlines of a vector field. In addition to simply plotting the streamlines, it allows you to map the colors and/or line widths of streamlines to a separate parameter, such as the speed or local intensity of the vector field.

[![../../_images/sphx_glr_plot_streamplot_0011.png](E:/工具/Typora/Temp/sphx_glr_plot_streamplot_0011.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot with various plotting options.

This feature complements the `quiver()` function for plotting vector fields. Thanks to Tom Flannaghan and Tony Yu for adding the streamplot function.

## Ellipses

In support of the Phoenix mission to Mars (which used Matplotlib to display ground tracking of spacecraft), Michael Droettboom built on work by Charlie Moad to provide an extremely accurate 8-spline approximation to elliptical arcs (see `Arc`, which are insensitive to zoom level.

[![../../_images/sphx_glr_ellipse_demo_0011.png](E:/工具/Typora/Temp/sphx_glr_ellipse_demo_0011.png)](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html)

Ellipse Demo

## Bar charts

Use the `bar()` function to make bar charts, which includes customizations such as error bars:

[![../../_images/sphx_glr_barchart_demo_0011.png](E:/工具/Typora/Temp/sphx_glr_barchart_demo_0011.png)](https://matplotlib.org/stable/gallery/statistics/barchart_demo.html)

Barchart Demo

You can also create stacked bars (bar_stacked.py, or horizontal bar charts (barh.py.

## Pie charts

The `pie()` function allows you to create pie charts. Optional features include auto-labeling the percentage of area, exploding one or more wedges from the center of the pie, and a shadow effect. Take a close look at the attached code, which generates this figure in just a few lines of code.

[![../../_images/sphx_glr_pie_features_0011.png](E:/工具/Typora/Temp/sphx_glr_pie_features_0011.png)](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html)

Pie Features

## Tables

The `table()` function adds a text table to an axes.

[![../../_images/sphx_glr_table_demo_0011.png](E:/工具/Typora/Temp/sphx_glr_table_demo_0011.png)](https://matplotlib.org/stable/gallery/misc/table_demo.html)

Table Demo

## Scatter plots

The `scatter()` function makes a scatter plot with (optional) size and color arguments. This example plots changes in Google's stock price, with marker sizes reflecting the trading volume and colors varying with time. Here, the alpha attribute is used to make semitransparent circle markers.

[![../../_images/sphx_glr_scatter_demo2_0011.png](E:/工具/Typora/Temp/sphx_glr_scatter_demo2_0011.png)](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html)

Scatter Demo2

## GUI widgets

Matplotlib has basic GUI widgets that are independent of the graphical user interface you are using, allowing you to write cross GUI figures and widgets. See `matplotlib.widgets` and the widget examples.

[![../../_images/sphx_glr_slider_demo_0011.png](E:/工具/Typora/Temp/sphx_glr_slider_demo_0011.png)](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider and radio-button GUI.

## Filled curves

The `fill()` function lets you plot filled curves and polygons:

[![../../_images/sphx_glr_fill_0011.png](E:/工具/Typora/Temp/sphx_glr_fill_0011.png)](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html)

Fill

Thanks to Andrew Straw for adding this function.

## Date handling

You can plot timeseries data with major and minor ticks and custom tick formatters for both.

[![../../_images/sphx_glr_date_0011.png](E:/工具/Typora/Temp/sphx_glr_date_0011.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html)

Date

See `matplotlib.ticker` and `matplotlib.dates` for details and usage.

## Log plots

The `semilogx()`, `semilogy()` and `loglog()` functions simplify the creation of logarithmic plots.

[![../../_images/sphx_glr_log_demo_0011.png](E:/工具/Typora/Temp/sphx_glr_log_demo_0011.png)](https://matplotlib.org/stable/gallery/scales/log_demo.html)

Log Demo

Thanks to Andrew Straw, Darren Dale and Gregory Lielens for contributions log-scaling infrastructure.

## Polar plots

The `polar()` function generates polar plots.

[![../../_images/sphx_glr_polar_demo_0011.png](E:/工具/Typora/Temp/sphx_glr_polar_demo_0011.png)](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)

Polar Demo

## Legends

The `legend()` function automatically generates figure legends, with MATLAB-compatible legend-placement functions.

[![../../_images/sphx_glr_legend_0011.png](E:/工具/Typora/Temp/sphx_glr_legend_0011.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend.html)

Legend

Thanks to Charles Twardy for input on the legend function.

## TeX-notation for text objects

Below is a sampling of the many TeX expressions now supported by Matplotlib's internal mathtext engine. The mathtext module provides TeX style mathematical expressions using FreeType and the DejaVu, BaKoMa computer modern, or STIX fonts. See the `matplotlib.mathtext` module for additional details.

[![../../_images/sphx_glr_mathtext_examples_0011.png](E:/工具/Typora/Temp/sphx_glr_mathtext_examples_0011.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_examples.html)

Mathtext Examples

Matplotlib's mathtext infrastructure is an independent implementation and does not require TeX or any external packages installed on your computer. See the tutorial at Writing mathematical expressions.

## Native TeX rendering

Although Matplotlib's internal math rendering engine is quite powerful, sometimes you need TeX. Matplotlib supports external TeX rendering of strings with the _usetex_ option.[![../../_images/sphx_glr_tex_demo_0011.png](E:/工具/Typora/Temp/sphx_glr_tex_demo_0011.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Tex Demo

## EEG GUI

You can embed Matplotlib into Qt, GTK, Tk, or wxWidgets applications. Here is a screenshot of an EEG viewer called pbrain.

![../../_images/eeg_small.png](E:/工具/Typora/Temp/eeg_small.png)

The lower axes uses `specgram()` to plot the spectrogram of one of the EEG channels.

For examples of how to embed Matplotlib in different toolkits, see:

> - Embedding in GTK3
> - Embedding in wx #2
> - Matplotlib With Glade 3
> - Embedding in Qt
> - Embedding in Tk

## XKCD-style sketch plots

Just for fun, Matplotlib supports plotting in the style of xkcd.[![](E:/工具/Typora/Temp/sphx_glr_xkcd_0011.png)](https://matplotlib.org/stable/gallery/showcase/xkcd.html)



## Subplot example

Many plot types can be combined in one figure to create powerful and flexible representations of data.![sample plots](E:/工具/Typora/Temp/sphx_glr_sample_plots_001.png)

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()
```

