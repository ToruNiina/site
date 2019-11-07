# operator<=>
* chrono[meta header]
* std::chrono[meta namespace]
* function[meta id-type]
* cpp20[meta cpp]

```cpp
namespace std::chrono {
  constexpr strong_ordering operator<=>(const day& x, const day& y) noexcept; // (1) C++20
}
```

## 概要
`day`同士の三方比較を行う。


## 戻り値
- (1) : `static_cast<unsigned int>(x) <=> static_cast<unsigned int>(y);`


## 例外
投げない


## 備考
- この演算子により、`operator<`、`operator<=`、`operator>`、`operator>=`が自動定義される


## 例
```cpp example
#include <cassert>
#include <chrono>

namespace chrono = std::chrono;

int main()
{
  assert((chrono::day{1} <=> chrono::day{1}) == 0);

  assert(chrono::day{1} < chrono::day{2});
  assert(chrono::day{1} <= chrono::day{2});

  assert(chrono::day{2} > chrono::day{1});
  assert(chrono::day{2} >= chrono::day{1});
}
```

### 出力
```
```

## バージョン
### 言語
- C++20

### 処理系
- [Clang](/implementation.md#clang): (9.0時点で実装なし)
- [GCC](/implementation.md#gcc): (9.2時点で実装なし)
- [Visual C++](/implementation.md#visual_cpp): (2019 Update 3時点で実装なし)