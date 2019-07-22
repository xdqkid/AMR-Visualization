# AMR-Visualization
AMR-Visualization Tools, show AMR graph strcucture

Abstract Meaning Representation Visualization 

## Quickstart

```python
python amr-slide-simple.py AMR-file.txt
or
python amr-slide-single-line.py AMR-file-with-single-line-format.txt
```

- Python3.5+

- Your input should be raw AMR format (likes [JAMR](https://github.com/jflanigan/jamr)).

- Install [graphviz](https://pypi.org/project/graphviz/)

  Remember to configure environment variables after installing graphviz

- Output is PDF, it is easy to convert 2 picture

## Example

AMR-file.txt

```
# ::snt export of high-tech products has frequently been in the spotlight , making a significant contribution to the growth of foreign trade in guangdong .
# ::tok export of high - tech products has frequently been in the spotlight , making a significant contribution to the growth of foreign trade in guangdong .
# ::alignments 24-25|0 22-23|0.0 21-22|0.0.1.0.1.0 19-20|0.0.1 16-17|0.0.1.0 15-16|0.0.1.0.1 11-12|0.0.0.0 7-8|0.0.0 5-6|0.0.1.0.0.0 4-5|0.0.1.0.0.0.0 2-3|0.0.1.0.0.0.0.0 0-1|0.0.1.0.0 ::annotator JAMR dev v0.3 ::date 2019-07-08T23:42:17.243
(g / guangdong
      :ARG2-of (t / trade-01
            :ARG1 (f2 / frequent-02
                  :ARG1 (s2 / spotlight))
            :ARG1-of (g2 / grow-01
                  :ARG2-of (c / contribute-01
                        :ARG1 (e / export-01
                              :ARG1 (p / product
                                    :mod (t2 / tech
                                          :ARG1-of (h / high-02))))
                        :ARG1-of (s / significant-02
                              :compared-to (f / foreign))))))

```

AMR-file-with-single-line-format.txt

```
gold :op1 interrogative
know :arg0 you :arg1 it :beneficiary interrogative :mod ( country :name ( name :op1 wouldn )  )  :polarity -
(g / guangdong :ARG2-of (t / trade-01 :ARG1 (f2 / frequent-02 :ARG1 (s2 / spotlight)) :ARG1-of (g2 / grow-01 :ARG2-of (c / contribute-01 :ARG1 (e / export-01 :ARG1 (p / product :mod (t2 / tech :ARG1-of (h / high-02)))) :ARG1-of (s / significant-02 :compared-to (f / foreign))))))
```



Visualization(Demo Only Show Multi-line)

```
digraph "AMR-Graph" {
	rankdir=TB
	"frequent-02" -> spotlight [label=":ARG1"]
	"trade-01" -> "frequent-02" [label=":ARG1"]
	tech -> "high-02" [label=":ARG1-of"]
	product -> tech [label=":mod"]
	"export-01" -> product [label=":ARG1"]
	"contribute-01" -> "export-01" [label=":ARG1"]
	"significant-02" -> foreign [label=":compared-to"]
	"contribute-01" -> "significant-02" [label=":ARG1-of"]
	"grow-01" -> "contribute-01" [label=":ARG2-of"]
	"trade-01" -> "grow-01" [label=":ARG1-of"]
	guangdong -> "trade-01" [label=":ARG2-of"]
}

```

![Demo](./demo.jpg)

## Citation

If you would like to cite this work, please cite the following: 
AMR-Visualization,xdqkid, https://github.com/xdqkid/AMR-Visualization

---

# 抽象语义表示可视化工具
## 快速入门

```python
python amr-slide-simple.py AMR-file.txt
or
python amr-slide-single-line.py AMR-file-with-single-line-format.txt
```

- Python3.5+

- AMR格式参考[JAMR](https://github.com/jflanigan/jamr)，

- 安装[graphviz](https://pypi.org/project/graphviz/)

  根据平台下载graphviz安装包，配置环境变量，然后pip

- 输出是PDF。如果需要图片格式，那你肯定不是在写论文（逃

## 示例

AMR-file.txt样例文件示意

```
# ::snt export of high-tech products has frequently been in the spotlight , making a significant contribution to the growth of foreign trade in guangdong .
# ::tok export of high - tech products has frequently been in the spotlight , making a significant contribution to the growth of foreign trade in guangdong .
# ::alignments 24-25|0 22-23|0.0 21-22|0.0.1.0.1.0 19-20|0.0.1 16-17|0.0.1.0 15-16|0.0.1.0.1 11-12|0.0.0.0 7-8|0.0.0 5-6|0.0.1.0.0.0 4-5|0.0.1.0.0.0.0 2-3|0.0.1.0.0.0.0.0 0-1|0.0.1.0.0 ::annotator JAMR dev v0.3 ::date 2019-07-08T23:42:17.243
# 前面有#号都可以忽略，重要的是下面的AMR图，AMR图之间用空行分隔开。
(g / guangdong
      :ARG2-of (t / trade-01
            :ARG1 (f2 / frequent-02
                  :ARG1 (s2 / spotlight))
            :ARG1-of (g2 / grow-01
                  :ARG2-of (c / contribute-01
                        :ARG1 (e / export-01
                              :ARG1 (p / product
                                    :mod (t2 / tech
                                          :ARG1-of (h / high-02))))
                        :ARG1-of (s / significant-02
                              :compared-to (f / foreign))))))

```

AMR-file-with-single-line-format.txt样例文件示意，即单行简化的AMR图。

```
gold :op1 interrogative
know :arg0 you :arg1 it :beneficiary interrogative :mod ( country :name ( name :op1 wouldn )  )  :polarity -
(g / guangdong :ARG2-of (t / trade-01 :ARG1 (f2 / frequent-02 :ARG1 (s2 / spotlight)) :ARG1-of (g2 / grow-01 :ARG2-of (c / contribute-01 :ARG1 (e / export-01 :ARG1 (p / product :mod (t2 / tech :ARG1-of (h / high-02)))) :ARG1-of (s / significant-02 :compared-to (f / foreign))))))
```

可视化（这里仅展示多行，单行效果相同）

```
digraph "AMR-Graph" {
	rankdir=TB
	"frequent-02" -> spotlight [label=":ARG1"]
	"trade-01" -> "frequent-02" [label=":ARG1"]
	tech -> "high-02" [label=":ARG1-of"]
	product -> tech [label=":mod"]
	"export-01" -> product [label=":ARG1"]
	"contribute-01" -> "export-01" [label=":ARG1"]
	"significant-02" -> foreign [label=":compared-to"]
	"contribute-01" -> "significant-02" [label=":ARG1-of"]
	"grow-01" -> "contribute-01" [label=":ARG2-of"]
	"trade-01" -> "grow-01" [label=":ARG1-of"]
	guangdong -> "trade-01" [label=":ARG2-of"]
}

```

![Demo](./demo.jpg)

## 引用

如果你用了本工具，请引用如下文字

AMR-Visualization，xdqkid,  https://github.com/xdqkid/AMR-Visualization