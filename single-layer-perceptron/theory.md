# 单层感知器

具有单层计算单元的神经网络系统，称为Perceptron（感知器）。感知器的学习规则规定，**学习信号**等于**神经元期望输出**（教师信号）与**实际输出**之差：
$$ r=d\_j-o\_j$$

式中，\\(d\_j\\)为期望的输出，实际的输出为\\(o\_j=f(\mathbf{W}\_j^T\mathbf{X})\\) 。感知器采用了**符号函数**作为转移（激活）函数，其表达为：
$$f(\mathbf{W}\_j^T\mathbf{X})=sgn(\mathbf{W}\_j^T\mathbf{X})\begin{cases}1, \ \ \ \ \mathbf{W}\_j^T\mathbf{X}\geq0\\\<br>
-1,  \  \mathbf{W}\_j^T\mathbf{X}<0\\
\end{cases}$$ 

因此，权值调整公式应为：
$$\Delta\mathbf{W}\_j=\eta\left[d_j-sgn(\mathbf{W}\_j^T\mathbf{X})\right] \mathbf{X}$$
式中\\(\Delta\mathbf{W}\_j\\)为权值向量的调整量，\\(\eta\\)为学习速率。

式中，当实际输出与期望值相同时，权值不需要调整；在有误差的情况下，由于\\(d_j\\)和\\(sgn(\mathbf{W}\_j^T\mathbf{X})\in\\{-1,1\\}\\)，权值调整公式可简化为：
$$\Delta\mathbf{W}\_j=\pm2\eta\mathbf{X}$$

感知器学习规则**只适用于二进制神经元，初始权值可取任意值**。
感知器学习规则代表一种有导师学习。由于感知器理论是研究其他神经网络的基础，该规则对于神经网络的有导师学习具有极为重要的意义。
