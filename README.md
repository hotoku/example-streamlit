# streamlitの練習

## memo

`streamlit run`は、`.py`ファイルを直接起動する。パッケージ内部のファイルを直接起動したい場合、相対importで困るケースがあると思うが、このレポジトリでは、以下の方針で対応。下記linkのギャラリーなどを見ても同様にしている。

- 主な機能を独立したパッケージとして作る（ここの例では`exst`）
- main.pyだけ、パッケージと併存する形でレポジトリに置いておく

## link

- [gallery][gallery]
- [prettymapp][prettymapp]

## todo

- dataframeを表示する
  - pagerつきで
- select boxなどでinteractiveにするパーツ
- グラフを書く
- 画面内のタブ
- 画面の縦分割
- 例外処理
- 一部の処理に時間がかかる場合の扱い

##### end

<!-- link -->
[gallery]: https://streamlit.io/gallery?category=geography-society
[prettymapp]: https://github.com/chrieke/prettymapp
