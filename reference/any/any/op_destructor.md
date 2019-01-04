# デストラクタ
* any[meta header]
* std[meta namespace]
* any[meta class]
* function[meta id-type]
* cpp17[meta cpp]

```cpp
~any();
```

## 概要
`any`オブジェクトを破棄する。


## 効果
[`reset()`](reset.md)を呼び出すことと同等。


## バージョン
### 言語
- C++17

### 処理系
- [Clang, C++17 mode](/implementation.md#clang): 4.0.1
- [GCC, C++17 mode](/implementation.md#gcc): 7.3
- [Visual C++](/implementation.md#visual_cpp): ??