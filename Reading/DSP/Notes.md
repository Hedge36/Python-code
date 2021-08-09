#  第一章 声音和信号

## 综述

> **信号代表随着时间变化的量。**声音源自于空气压力的改变。声音信号代表的是空气压力随着时间的变化。
>
> 传声器是测量上述变化并产生表示所测声音的电信号的设备。扬声器是通过输入的电信号产生声音的设备。传声器和扬声器都被称为换能器，因为它们将信号从一种形式转化成另一种形式，也就是变换了能量的形式。
>
> **这套方法同样可以应用于随空间而不是时间变化的信号，或者是不止一个维度的信号**，本书着重于一维声音信号的介绍，其方法也可以用于其他各个领域的信号。

## 1. 周期信号

> 周期信号是在一段时间后重复出现的信号，对周期信号的描述，与正弦函数大致类似，但形状更加复杂。周期信号的形状称为波形。波形的形状决定了音乐的音色，也就是我们对声音品性的感受。

## 2. 频谱分析

> 本书最重要的主题是**频谱分析**。根据**离散傅里叶变换(Discrete Fourier Transform, DFT)**，任何信号都可以表示成一系列不同频率的正弦信号的叠加和，在这个意义下，DFT能将信号转换为频谱，这个集合称为**频谱**。频谱图中的纵坐标表示合成这个信号的正弦波**频率范围**，横坐标表示各个正弦波的频率元素的强度，或者说是**振幅**。
>
> 本书最重要的算法是**快速傅里叶变换(Fast Fourier Transform, FFT)**，它是计算离散傅里叶级数变换的一种高效方式。
>
> 频率最低的元素被称为**基频**，拥有最高的幅度的元素被称为**主频**。通常情况下，感知到的声音的音高是由其基频决定的，即使它不是主频。频谱中其他频率为基频的整数倍的元素被称为**谐波**，因为他们在乐理概念上跟基频和谐。

## 3. 波形的读写

> thinkdsp提供的`read_wave`可以读取WAV文件并返回一个wave对象，同时wave对象可以通过`write`方法来写入wav文件。

至于wav文件的播放，可以通过thinkdsp.play_wave实现，但是限于播放器等因素，暂无法正常使用。

```python
wave = thinkdsp.read_wave("sound.wav")
wave.write(filename="sound2.wav")
thinkdsp.play_wave(filename="sound2.wav", player="aplay")
```

## 4. 频谱

Wave提供了make_spectrum，它返回的是Spectrum对象，同时Spectrum提供了plot方法，Spectrum提供了3种修改频谱的方法。

> + **low_pass**，它加载一个低通滤波器，也就是说高于给定的截止频率的频率元素被按照一定因素衰减（也就是在大小上降低）。
> + **high_pass**，它加载了高通滤波器，也就是说低于某个截止频率的元素被衰减量。
> + **band_stop**，它让处于两个截止频率之间的波段内的频率元素衰减了。



# 第二章 谐波

> 通过观察它们的频谱来理解它们的谐波结构，也就是构成它们的三角函数集合的结构。本章还要介绍数字信号处理中最重要的现象之一：混叠。同时解释一下Spectrum类的工作原理。

## 1. 三角波

一个正弦波仅包括一个频率元素，所以其频谱只有一个尖峰。对于更加复杂的波形，如小提琴的录音，其DFT的结果中有很多尖峰。

我们可以通过`thinkdsp.TriangleSignal`来生成三角波，这个频谱的另一个特征在于谐波的幅度于频率的关系。

```python
class	TriangleSignal( Sinusoid):
  	def evaulate(self, ts):
      	cycles = self.freq * ts + self.offset / PI2
        frac, _ = np.modf(cycles)
          ys = np.abs( frac - 0.5)
          ys = normalize(unbias(ys), self.amp)
          return ys
```

![Triangle](Plot/TriangleSignal.png)

## 2. 方波

thinkdsp还提供了SquareSignal，用来处理方波。

```python
class	SquareSignal( Sinusoid):
  	def evaulate(self, ts):
      	cycles = self.freq * ts + self.offset / PI2
        frac, _ = np.modf(cycles)
          ys = np.abs( frac - 0.5)
          ys = normalize(unbias(ys), self.amp)
          return ys
```

![SquareSignal](Plot/SquareSignal.png)

## 3. 混叠

> 折叠频率

## 4. 计算频率

```python
from np.fft import rfft, rfftfreq

class	Wave:
  	def make_spectrum(self):
      	n = len(self.ys)
        d = l / self.framerate
        hs = rfft(self.ys)
        fs = rfftfreq(n, d)
          return Spectum(hs, fs, self.framerate)
```

> 参数self是一个Wave对象。n为波形的采样数，而d是采样频率的频率的倒数，也就是样本间的时间差。
>
> `np.fft`是Numpy模块，提供快速傅里叶变换(FFT)的相关函数，这是一种计算离散傅里叶变化的高效算法。
>
> make_spectrum使用了rfft，其意义是“傅里叶变换实数部分”，因为Wave只有实数值，而没有复数值。



# 第三章 非周期信号

> 目前为止我们接触的信号都是周期性的，这意味着他们一直重复，这也意味着其所包含的频率元素不随时间的变化而变化。

## 1. 线性啁啾(Chirp)

> 我们从啁啾开始，它是一种可变频率信号。thinkdsp中提供了类`Chrip`来创建扫描波，其频率线性地扫描过。

## 2. 泄露

## 3. 加窗

通过平滑段的开始和结束来缓解其不连续性，从而减少泄露的方法叫加窗。

“窗”是一个设计好的函数，被用来变换非周期片段，使得它可以作为周期信号被处理。



# 第四章 噪音

> 按照一般定义，**“噪音”是指不想要或者令人难受的声音。**在信号处理中，它有两种不同的意义。
>
> 1. 如定义一般，指任意形式不想要的信号。如果两个信号互相干扰，那么它们堆彼此都是噪音。
> 2. “噪音”也可以是指一个信号中包括很多频率，这样它就没有我们在前几章中所看到周期信号的谐波结构。
>
> 本章的噪音是指第二种。

## 1. 不相关噪音

> 理解噪音最简单的方式就是产生它，而最容易产生的一类噪音就是不相关均匀噪音（UU）。“均匀”是指信号包含的随机值服从均匀分布。“不相关”是指各个值相互独立。

thinkdsp中提供了类`UncorrelatedUniformNoise`来生成UU噪音。 

## 2. 累积频谱

> 对于UU噪音，我们可以通过查看累计频谱来更清楚地认识能量和频率之间的关系，累积频谱是频率f的函数，显示的是频谱中f处所累积的能量。

Spectrum提供了`IntegratedSpectrum`方法来计算累计频谱。

## 3. 布朗噪音

布朗噪音得名于布朗运动，指噪音值是前一个值域一个随机“步长”的和。布朗噪音又称红噪或者褐噪。

## 4. 粉噪

## 5. 高斯噪声



# 第八章 滤波与卷积

## 1. 平滑

**平滑操作的目的在于移除信号中的短时变化，从而揭示其长时间趋势。**一个通用的平滑算法时滑动平均，它计算的是前n个值得平均，n值是指定的。

## 2. 卷积

卷积是一种非常常用的操作，在numpy中，采用convolve方法，详情看官网。



# 鸽

## 原因

> 基于自己写的代码，没有普适性，介绍不够具体，也没足够的实用性。

