# 槽天线（无限大接地板）题解

题目给定开口面尺寸

- \(a = 1.5\lambda\)
- \(b = 2\lambda\)

开口面切向场分布为

\[
\mathbf{E}_{\tan} = \hat{\mathbf y} E_0 \cos\!\left(\frac{\pi x'}{a}\right),
\qquad
\mathbf{H}_{\tan} = -\hat{\mathbf x} E_0 \frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right)
\]

定义域

\[
-\frac{a}{2} \le x' \le \frac{a}{2},
\qquad
-\frac{b}{2} \le y' \le \frac{b}{2}.
\]

以下取开口面法向量为

\[
\hat{\mathbf n} = \hat{\mathbf z}
\]

即从接地板指向辐射半空间 \(z>0\)。

---

## 1.1 开口等效电流

Love 等效原理中，开口面的等效电流为

\[
\mathbf{J}_s = \hat{\mathbf n} \times \mathbf{H}_{\tan},
\qquad
\mathbf{M}_s = -\hat{\mathbf n} \times \mathbf{E}_{\tan}.
\]

---

### (a) 只用 E 场并结合镜像理论

对于无限大 PEC 接地板上的开口，若只保留磁流，镜像理论使磁流加倍：

\[
\mathbf{M}_s^{(E)} = -2\hat{\mathbf n}\times\mathbf{E}_{\tan}.
\]

代入 \(\hat{\mathbf n}=\hat{\mathbf z}\) 和 \(\mathbf{E}_{\tan}=\hat{\mathbf y}E_0\cos(\pi x'/a)\)：

\[
\mathbf{M}_s^{(E)}
= -2\hat{\mathbf z}\times\hat{\mathbf y}\,E_0\cos\!\left(\frac{\pi x'}{a}\right)
= 2\hat{\mathbf x}\,E_0\cos\!\left(\frac{\pi x'}{a}\right).
\]

因此

\[
\boxed{
\mathbf{M}_s^{(E)} = 2\hat{\mathbf x}\,E_0\cos\!\left(\frac{\pi x'}{a}\right),\qquad
\mathbf{J}_s^{(E)} = 0
}
\]

---

### (b) 只用 H 场并结合镜像理论

若只保留电流，镜像理论使电流加倍：

\[
\mathbf{J}_s^{(H)} = 2\hat{\mathbf n}\times\mathbf{H}_{\tan}.
\]

代入 \(\mathbf{H}_{\tan}=-\hat{\mathbf x}E_0\dfrac{k_z}{\omega\mu}\cos(\pi x'/a)\)：

\[
\mathbf{J}_s^{(H)}
= 2\hat{\mathbf z}\times\left(-\hat{\mathbf x}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right)\right)
= -2\hat{\mathbf y}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right).
\]

因此

\[
\boxed{
\mathbf{J}_s^{(H)} =
-2\hat{\mathbf y}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right),\qquad
\mathbf{M}_s^{(H)} = 0
}
\]

---

### (c) 不用镜像理论，同时使用 E、H 两个场

直接用 Love 等效：

\[
\mathbf{J}_s = \hat{\mathbf n}\times\mathbf{H}_{\tan},
\qquad
\mathbf{M}_s = -\hat{\mathbf n}\times\mathbf{E}_{\tan}.
\]

于是

\[
\mathbf{J}_s
= \hat{\mathbf z}\times\left(-\hat{\mathbf x}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right)\right)
= -\hat{\mathbf y}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right),
\]

\[
\mathbf{M}_s
= -\hat{\mathbf z}\times\hat{\mathbf y}E_0\cos\!\left(\frac{\pi x'}{a}\right)
= \hat{\mathbf x}E_0\cos\!\left(\frac{\pi x'}{a}\right).
\]

因此

\[
\boxed{
\mathbf{J}_s =
-\hat{\mathbf y}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right),\qquad
\mathbf{M}_s =
\hat{\mathbf x}E_0\cos\!\left(\frac{\pi x'}{a}\right)
}
\]

可以看到，和使用镜像理论的结果相比，幅度正好差一个 2 倍系数。

---

## 1.2 E 面与 H 面方向图

对于无限大接地板上的槽天线，使用“只保留磁流 + 镜像理论”的等效最方便：

\[
\mathbf{M}_s = 2\hat{\mathbf x}E_0\cos\!\left(\frac{\pi x'}{a}\right).
\]

其远区方向函数可写成

\[
F(\theta,\phi)=I_x(\theta,\phi)\,I_y(\theta,\phi)
\]

其中

\[
I_y(\theta,\phi)
= \int_{-b/2}^{b/2} e^{jk y'\sin\theta\sin\phi}\,dy'
= b\,\mathrm{sinc}\!\left(\frac{k b}{2}\sin\theta\sin\phi\right),
\]

\[
I_x(\theta,\phi)
= \int_{-a/2}^{a/2}
\cos\!\left(\frac{\pi x'}{a}\right)
e^{jk x'\sin\theta\cos\phi}\,dx'
\]

\[
= \frac{2a}{\pi}
\frac{
\cos\!\left(\frac{k a}{2}\sin\theta\cos\phi\right)
}{
1-\left(\frac{k a}{\pi}\sin\theta\cos\phi\right)^2
}.
\]

这里采用

\[
\mathrm{sinc}(u)=\frac{\sin u}{u},\qquad \mathrm{sinc}(0)=1.
\]

由于磁流沿 \(x\) 方向，远区场可写成

\[
E_\theta \propto \sin\phi \, F(\theta,\phi),
\qquad
E_\phi \propto \cos\theta\cos\phi \, F(\theta,\phi).
\]

---

### E-plane（\(yz\) 面，\(\phi=90^\circ\)）

此时

\[
\cos\phi=0,\qquad \sin\phi=1.
\]

故

\[
I_x = \int_{-a/2}^{a/2}\cos\!\left(\frac{\pi x'}{a}\right)dx'=\frac{2a}{\pi}
\]

为常数，方向图只由 \(y\) 方向孔径决定：

\[
F_E(\theta)\propto
\mathrm{sinc}\!\left(\frac{k b}{2}\sin\theta\right).
\]

代入 \(b=2\lambda\)、\(k=2\pi/\lambda\)：

\[
\boxed{
F_E(\theta)\propto \mathrm{sinc}\!\left(2\pi\sin\theta\right)
}
\]

归一化后，E 面 dB 图可写为

\[
P_E(\theta)_{\mathrm{dB}}
=20\log_{10}\left|\frac{F_E(\theta)}{\max|F_E|}\right|.
\]

---

### H-plane（\(xz\) 面，\(\phi=0^\circ\)）

此时

\[
\sin\phi=0,\qquad \cos\phi=1.
\]

于是 \(I_y=b\) 为常数，而角度因子给出一个 \(\cos\theta\)：

\[
F_H(\theta)\propto
\cos\theta\,
\frac{
\cos\!\left(\frac{k a}{2}\sin\theta\right)
}{
1-\left(\frac{k a}{\pi}\sin\theta\right)^2
}.
\]

代入 \(a=1.5\lambda\)、\(k=2\pi/\lambda\)：

\[
\frac{k a}{2}=1.5\pi,
\qquad
\frac{k a}{\pi}=3.
\]

因此

\[
\boxed{
F_H(\theta)\propto
\cos\theta\,
\frac{
\cos\!\left(1.5\pi\sin\theta\right)
}{
1-9\sin^2\theta
}
}
\]

对应 dB 图为

\[
P_H(\theta)_{\mathrm{dB}}
=20\log_{10}\left|\frac{F_H(\theta)}{\max|F_H|}\right|.
\]

注意在 \(\sin\theta=\pm 1/3\) 处，上式是可去奇点，数值作图时应使用极限值或做小阈值处理。

---

## 可直接交作业的最终答案

\[
\boxed{
\mathbf{M}_s^{(E)} = 2\hat{\mathbf x}E_0\cos\!\left(\frac{\pi x'}{a}\right),\quad
\mathbf{J}_s^{(E)}=0
}
\]

\[
\boxed{
\mathbf{J}_s^{(H)}=
-2\hat{\mathbf y}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right),\quad
\mathbf{M}_s^{(H)}=0
}
\]

\[
\boxed{
\mathbf{J}_s=
-\hat{\mathbf y}E_0\frac{k_z}{\omega\mu}\cos\!\left(\frac{\pi x'}{a}\right),\quad
\mathbf{M}_s=
\hat{\mathbf x}E_0\cos\!\left(\frac{\pi x'}{a}\right)
}
\]

\[
\boxed{
F_E(\theta)\propto \mathrm{sinc}\!\left(2\pi\sin\theta\right)
}
\]

\[
\boxed{
F_H(\theta)\propto
\cos\theta\,
\frac{
\cos\!\left(1.5\pi\sin\theta\right)
}{
1-9\sin^2\theta
}
}
\]

Matlab 绘图程序见同目录文件 `slot_antenna_pattern.m`。
