# 试卷解答（深度学习 / 人工智能）

> 说明：图片为试卷扫描件。本文按题号给出推导与最终答案。

---

## 一、填空题（每空 2 分，共 30 分）

**1. 电影、动画等技术使用了人的认知机理中的 ______ 现象。**

**答：视觉暂留**（persistence of vision）

---

**2. 卷积核**
```
 0  0 -1  0  0
 0 -1  2 -1  0
-1  2  6  2 -1
 0 -1  2 -1  0
 0  0 -1  0  0
```
**模拟了生物视觉中的 ______ 感受野。**

该核为典型的 **中心–周围（on-center / off-surround）** 拮抗结构（中心正、四周负，与 LoG / DoG 类似），对应视网膜神经节细胞和外侧膝状体的同心圆拮抗式感受野。

**答：中心–周围（同心圆拮抗式）感受野**

---

**3. 含 softmax 的交叉熵损失**

3 类，真值标号 0,1,2；样本真实类别为 2，分类器输出 logits 为 $z=(2,-1,3)$。

$$
L = -\log\frac{e^{z_2}}{\sum_i e^{z_i}}
   = -z_2 + \log\!\Big(e^{2}+e^{-1}+e^{3}\Big)
$$

$e^{2}\!\approx\!7.389,\; e^{-1}\!\approx\!0.368,\; e^{3}\!\approx\!20.086,\; \sum\!\approx\!27.843$

$$
L = -3 + \ln(27.843) \approx -3 + 3.327 \approx \boxed{0.327}
$$

（等价表达 $L=\ln(1+e^{-1}+e^{-5})\approx 0.327$。）

---

**4. CNN、Transformer 的流派是 ______，强化学习的流派是 ______。**

- CNN / Transformer：**连接主义**（Connectionism）
- 强化学习：**行为主义**（Behaviorism / Actionism）

---

**5. 使用 softmax 函数在隐含层层数较多时存在 ______ 的问题。**

**答：梯度消失**（vanishing gradient）。softmax 输出位于 (0,1) 且容易饱和，多层堆叠时反向传播的梯度连乘后迅速趋于 0。

---

**6. 输入 H×W×C，padding=2，stride=1，卷积核 7×7，输入/输出通道均为 C。求输出尺寸。**

$$
H_{\text{out}} = \frac{H + 2\cdot 2 - 7}{1}+1 = H-2,\quad W_{\text{out}} = W-2
$$

**答：$(H-2)\times(W-2)\times C$**

---

**7. 原始卷积核尺寸 $K\!\times\!K\!\times\!C_{in}\!\times\!C_{out}$，换用深度可分离卷积，总参数量为 ______。**

- Depth-wise：$K\!\times\!K\!\times\!C_{in}$
- Point-wise（1×1 卷积）：$1\!\times\!1\!\times\!C_{in}\!\times\!C_{out}=C_{in}\!\cdot\!C_{out}$

**答：$K^{2}C_{in}+C_{in}C_{out}$**

---

**8. GPT 的结构是 ______，BERT 的结构是 ______。**

- GPT：**② Decoder-only**
- BERT：**① Encoder-only**

---

**9. SVM 是 ______，朴素贝叶斯是 ______。**

- SVM：**① 鉴别类**（discriminative，直接学习决策边界 $p(y|x)$）
- 朴素贝叶斯：**② 生成类**（generative，建模 $p(x,y)=p(x|y)p(y)$）

---

**10. 模型扩展到一定规模时性能突然显著跃升，远超随机水平的现象。**

**答：涌现（emergence / 涌现能力）**

---

**11. 深度增加导致训练效果反而变差（非欠拟合），加入 ______ 连接可解决；当输入与输出维度不一致时，通过 ______ 技术可解决。**

- 加入 **残差（skip / residual）** 连接（ResNet）
- 通过 **1×1 卷积（线性投影）** 调整维度

---

## 二、简答题（每题 5 分，共 20 分）

### 1. 单层 sigmoid 逻辑回归两种情况分析

**(1) 训练集 & 测试集准确率都较低**  
→ **欠拟合（Underfitting）**。

可能原因：
- 模型容量过低：单神经元 + sigmoid 只能表达线性分类边界，无法刻画复杂模式；
- 特征工程不足、输入特征区分度差；
- 训练不充分（学习率不当、迭代不够、初始化不好）；
- 损失函数选择不合理。

改进：
- 增加模型容量（多层 MLP/CNN、加宽网络）；
- 引入非线性特征或更强的特征工程；
- 更换/调整优化器、学习率、训练轮数；
- 减小正则化强度。

**(2) 训练集高、测试集低**  
→ **过拟合（Overfitting）**。

改进措施（≥3 种）：
1. **正则化**：L1/L2 权重惩罚、权重衰减；
2. **Dropout**；
3. **数据增强 / 增加训练数据**；
4. **早停（early stopping）**；
5. **降低模型复杂度**（减少参数 / 层数）；
6. **批归一化、加噪声、集成学习**等。

---

### 2. 混淆矩阵（200 张图片，A=正常，B=肺癌，C=另一种肺病）

|        | 预测 A | 预测 B | 预测 C |
|--------|--------|--------|--------|
| 真实 A |   97   |   2    |   3    |
| 真实 B |   5    |   72   |   3    |
| 真实 C |   6    |   1    |   13   |

（C 行中间一格按 200 总数补 1；如取其它值同理。）

**(1) accuracy 与 B 类 precision**

$$
\text{accuracy}=\frac{97+72+13}{200}=\frac{182}{200}=0.91
$$

$$
\text{precision}(B)=\frac{\text{TP}_B}{\text{TP}_B+\text{FP}_B}=\frac{72}{2+72+1}=\frac{72}{75}=0.96
$$

**(2) B、C 类 recall 及问题分析**

$$
\text{recall}(B)=\frac{72}{5+72+3}=\frac{72}{80}=0.90
$$
$$
\text{recall}(C)=\frac{13}{6+1+13}=\frac{13}{20}=0.65
$$

**问题分析**：
- B 类（肺癌）召回率 0.90，尚可；但仍有 5 例肺癌被误判为正常 A，属于**漏诊**——在医疗场景中代价极高。
- C 类（另一种肺病）召回率只有 0.65，且 6 例被判为正常 A——同样存在严重的漏诊问题。
- 总体上系统对**异常类（B、C）的敏感性不足**，尤其对 C 容易漏诊；且 B、C 两种肺病间存在互相混淆。
- 数据可能存在**类别不平衡**（C 类样本仅 20 例），训练时建议采用类别加权损失 / 过采样 / Focal Loss；医学场景中可调整决策阈值，使漏诊率（FN）下降而非追求总体准确率。

---

### 3. PCA

5 个样本（按列读取）：

$$
X=\begin{pmatrix}0&0&1&3&1\\-2&0&0&1&1\end{pmatrix}
$$

**(1) 均值**

$$
\bar{\mathbf{x}}=\Big(\tfrac{0+0+1+3+1}{5},\ \tfrac{-2+0+0+1+1}{5}\Big)=(1,\ 0)
$$

**中心化样本**：$(-1,-2),(-1,0),(0,0),(2,1),(0,1)$

**(2) 协方差矩阵**（用 $\frac{1}{n}$ 估计）

$$
\sigma_{xx}=\tfrac{1+1+0+4+0}{5}=1.2,\quad
\sigma_{yy}=\tfrac{4+0+0+1+1}{5}=1.2,\quad
\sigma_{xy}=\tfrac{2+0+0+2+0}{5}=0.8
$$

$$
\Sigma=\begin{pmatrix}1.2 & 0.8\\0.8 & 1.2\end{pmatrix}
$$

**(3) 求主成分方向**

特征方程 $\det(\Sigma-\lambda I)=(1.2-\lambda)^2-0.64=0\Rightarrow 1.2-\lambda=\pm 0.8$

$$
\lambda_1=2.0,\quad \lambda_2=0.4
$$

对应 $\lambda_1=2$：$(1.2-2)v_1+0.8v_2=0\Rightarrow v_1=v_2$，单位化得

$$
\mathbf{u}_1=\frac{1}{\sqrt{2}}(1,1)^{\!\top}
$$

**(4) 含义**

- PCA 选择数据方差最大的方向作为投影方向。这里方差比 $\lambda_1:\lambda_2=2.0:0.4=5:1$，即 (1,1)/√2 方向上数据方差占总方差的 $\frac{2}{2.4}\approx 83.3\%$。
- 投影到 (1,1)/√2 方向 ≡ 计算 $(x+y)/\sqrt{2}$，相当于"x 与 y 同时增大或同时减小"的综合度量。
- 几何上：5 个样本沿 45° 斜线分布，PCA 找到了这条主轴；$x$ 与 $y$ 呈**正相关**（协方差 0.8 > 0）。投影后能用 1 维数值保留绝大部分原始信息。

---

### 4. LoRA 两阶段可训练参数量

**① 预训练**：$Q=XW_q,\;K=XW_k,\;V=XW_v$，$W_q,W_k,W_v\in\mathbb{R}^{d\times d}$

$$
\#\text{params}=3d^{2}
$$

**② LoRA 微调**：原 $W_q,W_k,W_v$ **冻结**；新增低秩矩阵 $Q_A,K_A,V_A\in\mathbb{R}^{d\times r}$，$Q_B,K_B,V_B\in\mathbb{R}^{r\times d}$。

$$
\#\text{trainable}=3\cdot(dr+rd)=6\,d\,r
$$

由于 $r\!\ll\!d$，LoRA 把可训练参数量从 $3d^2$ 降到 $6dr$，压缩比 $\approx \tfrac{2r}{d}$。

---

## 三、计算题（每题 10 分，共 50 分）

### 1. SVM

**点表**：
| 点      | (0,0) | (3,0) | (2,5) | (1,2) | (4,3) |
|---------|-------|-------|-------|-------|-------|
| 类别    | −1    | −1    | +1    | −1    | +1    |

**(1) 观察找支持向量与分界面**

考察函数 $g(x,y)=x+y$：

| 点 | (0,0) | (3,0) | (1,2) | (2,5) | (4,3) |
|----|-------|-------|-------|-------|-------|
| 类别 | −1 | −1 | −1 | +1 | +1 |
| $x+y$ | 0 | 3 | 3 | 7 | 7 |

取分界面 $x+y=5$，记 $w=(1,1),\;b=-5$。归一化使 $|w^{\!\top}x_i+b|=1$ 在支持向量处成立：

$$
w=\tfrac{1}{2}(1,1),\qquad b=-\tfrac{5}{2}
$$

则 (3,0)、(1,2) 对应 $w^{\!\top}x+b=-1$，(2,5)、(4,3) 对应 $w^{\!\top}x+b=+1$。

- **支持向量**：$(3,0),(1,2),(2,5),(4,3)$（四个）
- **分界面**：$x_1+x_2-5=0$
- 间隔 $\dfrac{2}{\|w\|}=\dfrac{2}{\sqrt{1/2}}=2\sqrt{2}$

（点 $(0,0)$ 处 $x+y=0$，离分界面更远，不是支持向量。）

**(2) 增加点 $(-4,-3)$，标签 +1，用核 $z_1=x_1+x_2,\;z_2=x_1^{2}+x_2^{2}$ 映射**

映射后：

| 原点 | 类别 | $(z_1,z_2)$ |
|------|------|-------------|
| (0,0)   | −1 | (0, 0) |
| (3,0)   | −1 | (3, 9) |
| (1,2)   | −1 | (3, 5) |
| (2,5)   | +1 | (7, 29) |
| (4,3)   | +1 | (7, 25) |
| (−4,−3) | +1 | (−7, 25) |

观察 $z_2$：负类 $z_2\in\{0,5,9\}$，正类 $z_2\in\{25,25,29\}$。

显然取 $z_2 = c$ 即可线性可分。最大间隔取中点：

$$
c=\frac{9+25}{2}=17
$$

**新空间分界面**：$z_2 = 17$  
**支持向量**：负类 $(3,9)$（即原 $(3,0)$）；正类 $(7,25),(-7,25)$（即原 $(4,3),(-4,-3)$）。  
间隔 $=\dfrac{25-9}{2}=8$。

**原空间分界面**：$x_1^{2}+x_2^{2}=17$，即半径 $\sqrt{17}$ 的圆。

- 圆内（$x_1^2+x_2^2<17$）：判 **−1**
- 圆外（$x_1^2+x_2^2>17$）：判 **+1**

---

### 2. 双层网络前向与一次反向更新

给定
$$
x=\begin{pmatrix}1\\-2\end{pmatrix},\;
k_1=\begin{pmatrix}0.5 & -1\\ 0 & 1\end{pmatrix},\;
b_1=\begin{pmatrix}0\\0\end{pmatrix},\;
k_2=\begin{pmatrix}1 & 0.5\\ -0.5 & 1\end{pmatrix},\;
b_2=\begin{pmatrix}0\\0\end{pmatrix},\;
y=\begin{pmatrix}0\\1\end{pmatrix}
$$
$\hat y = k_2\,\mathrm{ReLU}(k_1 x+b_1)+b_2$，$L=\tfrac12\|y-\hat y\|^2$。

**(1) 前向**

$$
z^{(1)}=k_1 x+b_1=\begin{pmatrix}0.5\!\cdot\!1+(-1)\!\cdot\!(-2)\\ 0\!\cdot\!1+1\!\cdot\!(-2)\end{pmatrix}
=\begin{pmatrix}2.5\\-2\end{pmatrix}
$$

$$
h=\mathrm{ReLU}(z^{(1)})=\begin{pmatrix}2.5\\0\end{pmatrix}
$$

$$
\hat y=k_2 h+b_2=
\begin{pmatrix}1\!\cdot\!2.5+0.5\!\cdot\!0\\ -0.5\!\cdot\!2.5+1\!\cdot\!0\end{pmatrix}
=\boxed{\begin{pmatrix}2.5\\-1.25\end{pmatrix}}
$$

损失 $L=\tfrac12\big((0-2.5)^2+(1-(-1.25))^2\big)=\tfrac12(6.25+5.0625)=\mathbf{5.65625}$。

**(2) 反向传播（学习率 η=0.1）**

设 $\delta^{(2)}=\partial L/\partial \hat y=\hat y - y=(2.5,\ -2.25)^{\!\top}$。

- 第 2 层：
  $$
  \frac{\partial L}{\partial k_2}=\delta^{(2)} h^{\!\top}
  =\begin{pmatrix}2.5\\-2.25\end{pmatrix}(2.5\ 0)
  =\begin{pmatrix}6.25 & 0\\ -5.625 & 0\end{pmatrix},\quad
  \frac{\partial L}{\partial b_2}=\delta^{(2)}=\begin{pmatrix}2.5\\-2.25\end{pmatrix}
  $$

- 回传到 $h$：$\partial L/\partial h=k_2^{\!\top}\delta^{(2)}
  =\begin{pmatrix}1 & -0.5\\ 0.5 & 1\end{pmatrix}\!\begin{pmatrix}2.5\\-2.25\end{pmatrix}
  =\begin{pmatrix}2.5+1.125\\ 1.25-2.25\end{pmatrix}
  =\begin{pmatrix}3.625\\-1\end{pmatrix}$

- 经过 ReLU：$z^{(1)}=(2.5,-2)$，导数 $(1,0)$，故 $\delta^{(1)}=\begin{pmatrix}3.625\\0\end{pmatrix}$。

- 第 1 层：
  $$
  \frac{\partial L}{\partial k_1}=\delta^{(1)} x^{\!\top}
  =\begin{pmatrix}3.625\\0\end{pmatrix}(1\ -2)
  =\begin{pmatrix}3.625 & -7.25\\ 0 & 0\end{pmatrix},\quad
  \frac{\partial L}{\partial b_1}=\begin{pmatrix}3.625\\0\end{pmatrix}
  $$

**参数更新**（$\theta\leftarrow\theta-\eta\nabla_\theta L$）：

$$
k_1^{\text{new}}=\begin{pmatrix}0.5 & -1\\0 & 1\end{pmatrix}-0.1\begin{pmatrix}3.625 & -7.25\\0 & 0\end{pmatrix}
=\boxed{\begin{pmatrix}0.1375 & -0.275\\ 0 & 1\end{pmatrix}}
$$

$$
b_1^{\text{new}}=\begin{pmatrix}-0.3625\\0\end{pmatrix}
$$

$$
k_2^{\text{new}}=\begin{pmatrix}1 & 0.5\\ -0.5 & 1\end{pmatrix}-0.1\begin{pmatrix}6.25 & 0\\ -5.625 & 0\end{pmatrix}
=\boxed{\begin{pmatrix}0.375 & 0.5\\ 0.0625 & 1\end{pmatrix}}
$$

$$
b_2^{\text{new}}=\begin{pmatrix}0\\0\end{pmatrix}-0.1\begin{pmatrix}2.5\\-2.25\end{pmatrix}=\begin{pmatrix}-0.25\\0.225\end{pmatrix}
$$

---

### 3. 朴素贝叶斯（高斯，等协方差）

$\Sigma=2I,\;\mu_1=(1,2),\;\mu_2=(-1,1)$。

由于 $\Sigma$ 相同，类条件密度的对数比是线性函数；判决边界为：

$$
\ln\frac{P(\omega_1)p(x|\omega_1)}{P(\omega_2)p(x|\omega_2)}=0
\;\Leftrightarrow\;
\ln\frac{P(\omega_1)}{P(\omega_2)}-\tfrac{1}{2\cdot2}\big(\|x-\mu_1\|^2-\|x-\mu_2\|^2\big)=0
$$

即 $\|x-\mu_2\|^2-\|x-\mu_1\|^2 = 4\ln\dfrac{P(\omega_2)}{P(\omega_1)}$。

展开（设 $x=(x_1,x_2)$）：
$$
\|x-\mu_2\|^2-\|x-\mu_1\|^2
=(x_1+1)^2+(x_2-1)^2-\big[(x_1-1)^2+(x_2-2)^2\big]=4x_1+2x_2-3
$$

故判决边界（一般形式）：

$$
\boxed{\;4x_1+2x_2-3=4\ln\frac{P(\omega_2)}{P(\omega_1)}\;}
$$

**(1) $P(\omega_1)=P(\omega_2)$**

$$
4x_1+2x_2-3=0\;\Longleftrightarrow\; 2x_1+x_2=\tfrac{3}{2}
$$

即点 $\big(\tfrac{3}{4},0\big),\big(0,\tfrac{3}{2}\big)$ 连线，恰为 $\mu_1,\mu_2$ 的**垂直平分线**（因等先验、等协方差、各向同性）。
- $\mu_1$ 侧（$4x_1+2x_2-3>0$）→ 判为 $\omega_1$。

**(2) $2P(\omega_1)=P(\omega_2)\Rightarrow P(\omega_2)/P(\omega_1)=2$**

$$
\boxed{\;4x_1+2x_2-3=4\ln 2\;}\quad\Rightarrow\quad
4x_1+2x_2 = 3+4\ln 2 \approx 5.773
$$

**分界面如何移动？** 
分界面法向 $(4,2)$ 指向 $\mu_1=(1,2)$（验证 $4\cdot1+2\cdot2-3=5>0$）。常数项变大意味着分界面沿法向**向 $\mu_1$ 平移**，$\omega_1$ 的判决区域**缩小**，$\omega_2$ 的判决区域**扩大**——与 $\omega_2$ 先验更大（更倾向于判为 $\omega_2$）一致。  
平移距离 $=\dfrac{4\ln 2}{\|(4,2)\|}=\dfrac{4\ln 2}{\sqrt{20}}=\dfrac{2\ln 2}{\sqrt{5}}\approx 0.62$。

**分类某样本 $x_0$**：计算 $g(x_0)=4x_{0,1}+2x_{0,2}-3-4\ln 2$。
- 若 $g(x_0)>0$ → 判 $\omega_1$；否则 → 判 $\omega_2$。

> 例如取 $x_0=(0,0)$：$g=-3-4\ln 2\approx -5.77<0$ → 判 $\omega_2$；  
> 取 $x_0=(2,2)$：$g=8+4-3-4\ln 2=9-4\ln 2\approx 6.23>0$ → 判 $\omega_1$。

---

### 4. 隐马尔可夫模型（HMM）

隐状态 $\{F,D,T\}$；观测 $\{H,M,L\}$。

$$
\pi=(0.6,\ 0.4,\ 0),\quad
A=\begin{pmatrix}0.8 & 0.1 & 0.1\\ 0.2 & 0.6 & 0.2\\ 0.1 & 0.1 & 0.8\end{pmatrix},\quad
B=\begin{pmatrix}0.8 & 0.1 & 0.1\\ 0.1 & 0.8 & 0.1\\ 0.1 & 0.1 & 0.8\end{pmatrix}
$$

行：$F,D,T$；$A$ 列：$F,D,T$；$B$ 列：$H,M,L$。
观测序列 $O=(H,M,L)$。

**(1) 前向算法求 $P(O)$**

$\alpha_1$（观测 $H$）：
$$
\alpha_1(F)=0.6\cdot 0.8=0.48,\quad \alpha_1(D)=0.4\cdot 0.1=0.04,\quad \alpha_1(T)=0
$$

$\alpha_2$（观测 $M$）：
$$
\alpha_2(F)=(0.48\!\cdot\!0.8+0.04\!\cdot\!0.2+0)\cdot 0.1=0.392\cdot 0.1=0.0392
$$
$$
\alpha_2(D)=(0.48\!\cdot\!0.1+0.04\!\cdot\!0.6+0)\cdot 0.8=0.072\cdot 0.8=0.0576
$$
$$
\alpha_2(T)=(0.48\!\cdot\!0.1+0.04\!\cdot\!0.2+0)\cdot 0.1=0.056\cdot 0.1=0.0056
$$

$\alpha_3$（观测 $L$）：
$$
\alpha_3(F)=(0.0392\!\cdot\!0.8+0.0576\!\cdot\!0.2+0.0056\!\cdot\!0.1)\cdot 0.1=0.04344\!\cdot\!0.1=0.004344
$$
$$
\alpha_3(D)=(0.0392\!\cdot\!0.1+0.0576\!\cdot\!0.6+0.0056\!\cdot\!0.1)\cdot 0.1=0.03904\!\cdot\!0.1=0.003904
$$
$$
\alpha_3(T)=(0.0392\!\cdot\!0.1+0.0576\!\cdot\!0.2+0.0056\!\cdot\!0.8)\cdot 0.8=0.01992\!\cdot\!0.8=0.015936
$$

$$
\boxed{P(H\!\to\!M\!\to\!L)=0.004344+0.003904+0.015936=0.024184}
$$

**(2) Viterbi 求最可能状态序列**

$\delta_1$ 同 $\alpha_1$：$\delta_1(F)=0.48,\;\delta_1(D)=0.04,\;\delta_1(T)=0$。

**$t=2$**（观测 M）：

| 到 | 来自 F | 来自 D | 来自 T | max | × B(·,M) |
|----|--------|--------|--------|-----|----------|
| F  | 0.48·0.8=0.384 | 0.04·0.2=0.008 | 0 | 0.384 (来自 F) | ×0.1 = 0.0384 |
| D  | 0.48·0.1=0.048 | 0.04·0.6=0.024 | 0 | 0.048 (来自 F) | ×0.8 = 0.0384 |
| T  | 0.48·0.1=0.048 | 0.04·0.2=0.008 | 0 | 0.048 (来自 F) | ×0.1 = 0.0048 |

**$t=3$**（观测 L）：

| 到 | 来自 F | 来自 D | 来自 T | max | × B(·,L) |
|----|--------|--------|--------|-----|----------|
| F  | 0.0384·0.8=0.03072 | 0.0384·0.2=0.00768 | 0.0048·0.1=0.00048 | 0.03072 (F) | ×0.1 = 0.003072 |
| D  | 0.0384·0.1=0.00384 | 0.0384·0.6=0.02304 | 0.0048·0.1=0.00048 | 0.02304 (D) | ×0.1 = 0.002304 |
| T  | 0.0384·0.1=0.00384 | 0.0384·0.2=0.00768 | 0.0048·0.8=0.00384 | 0.00768 (D) | ×0.8 = **0.006144** |

最大 $\delta_3=0.006144$ 在 $T$，由 $D$ 转入；$\delta_2(D)$ 由 $F$ 转入；$\delta_1(F)$。

**最可能状态序列**：$\boxed{F \to D \to T}$，联合概率 $0.006144$。

> 学期初专注 → 期中走神 → 期末疲惫，与观测 H→M→L 一致。

---

### 5. MoE（Mixture of Experts）

两个专家结构相同：
$$
y_k = Wx+\mathbf b,\quad
W=\begin{pmatrix}\ln 9 & 0.5\\ 0.5 & 0.5\end{pmatrix},\;
\mathbf b=\begin{pmatrix}1\\2\end{pmatrix},\quad k=1,2
$$

门控（可变路由）：$w_1=\mathbf c^{\!\top}x+0.5,\;w_2=\mathbf c^{\!\top}x-0.5$，其中 $\mathbf c=(-1,1)$。

输出：$z = \mathrm{SiLU}(w\,y)$，$\mathrm{SiLU}(x)=x\odot\mathrm{softmax}(x)$。

> 题面未给具体的 $x$ 值，下面以符号形式给出。

**(1) 两个专家的前向输出**

由于两专家参数完全相同，故 $y_1=y_2=y$：

$$
y = \begin{pmatrix}\ln 9 & 0.5\\ 0.5 & 0.5\end{pmatrix}\begin{pmatrix}x_1\\ x_2\end{pmatrix}+\begin{pmatrix}1\\2\end{pmatrix}
=\begin{pmatrix}(\ln 9)\,x_1+0.5\,x_2+1\\ 0.5\,x_1+0.5\,x_2+2\end{pmatrix}
$$

**(2) 门控加权 + SiLU**

门控权重（softmax 归一化）：

$$
g_k=\frac{e^{w_k}}{e^{w_1}+e^{w_2}},\quad k=1,2
$$

由 $w_1-w_2=1$，故 $g_1=\frac{e}{e+1}\approx 0.731,\;g_2=\frac{1}{e+1}\approx 0.269$（与 $x$ 无关，因为两个偏置之差恒为 1）。

混合：$\tilde y = g_1 y_1 + g_2 y_2 = y$（因两专家相同）。

最终：

$$
z = \mathrm{SiLU}(\tilde y)=\tilde y\odot\mathrm{softmax}(\tilde y)
$$

即逐元素 $z_i = \tilde y_i\cdot\dfrac{e^{\tilde y_i}}{e^{\tilde y_1}+e^{\tilde y_2}}$。

**(3) 训练中部分专家被频繁调用、部分几乎不被调用的危害与改进**

**危害（Expert Collapse / 负载不均衡）**：
1. **模型容量浪费**：闲置专家的参数无法被有效训练，相当于把多专家系统退化为少数几个专家；
2. **正反馈坍缩**：被频繁选用的专家更新更快，门控更倾向于继续选它们，少数专家被永远忽略；
3. **泛化下降**：少数过载专家容易过拟合，且无法处理不同子分布的数据；
4. **计算/显存利用率低**：在分布式/稀疏 MoE 上引起负载倾斜，慢的专家成为瓶颈；
5. **训练不稳定**：门控输出几乎确定性，softmax 梯度极小，难以从坍缩中恢复。

**改进措施**：
1. **负载均衡辅助损失（Load-Balancing Loss）**：例如 Switch Transformer 的
   $L_{\text{aux}}=N\sum_i f_i\cdot P_i$（$f_i$ 为分配给专家 $i$ 的 token 比例，$P_i$ 为 softmax 概率均值）；
2. **加噪 Top-k 路由（Noisy Top-k Gating）**：在 logits 上加可学习高斯噪声，鼓励探索；
3. **Importance Loss**：限制各专家被选概率方差；
4. **Expert Capacity（容量限制）**：每个专家有 token 数上限，溢出 token 被 dropout 或路由到次优专家；
5. **预热阶段使用随机/均匀路由**，让所有专家先得到训练；
6. **温度退火**：训练初期 softmax 温度高，后期再降低；
7. **正则化门控权重熵**，惩罚过度集中。

---

> （Q5 因题图中 SiLU、$w$、$x$ 的具体取值表述存在歧义，已按最自然的 MoE+softmax-gate 解释推导；如给定具体 $x$，把数值代入上式即可。）
