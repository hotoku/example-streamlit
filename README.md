# streamlitの練習

## memo

### エントリポイント

`streamlit run`は、`.py`ファイルを直接起動する。パッケージ内部のファイルを直接起動したい場合、相対importで困るケースがあると思うが、このレポジトリでは、以下の方針で対応。下記linkのギャラリーなどを見ても同様にしている。

- 主な機能を独立したパッケージとして作る（ここの例では`exst`）
- main.pyだけ、パッケージと併存する形でレポジトリに置いておく

### データフレーム

#### write

スライダーの範囲だけが描画される。

```python
st.write(df)
```

データを増やすとローカルにサーバーがある場合にも描画に時間がかかるようになった。
つまり、一度にクライアント側にデータを送っているっぽい。
巨大なデータフレームの一部を表示したい場合には、別途で考慮が必要。

ページネーションはあまり考えられていないようで、各々でwork aroundを作って対処している模様。
[これ][pagination]は、UIパーツも含めて自前実装しているパターン。

あまりに大量なデータから選択する場合には工夫が必要。

#### table

全行が描画される。

```python
st.table(df)
```

## todo

- select boxなどでinteractiveにするパーツ
- グラフを書く
- 画面内のタブ
- 画面の縦分割
- 例外処理
- 一部の処理に時間がかかる場合の扱い

## link

- [gallery][gallery]
- [prettymapp][prettymapp]

##### end

<!-- link -->
[gallery]: https://streamlit.io/gallery?category=geography-society
[prettymapp]: https://github.com/chrieke/prettymapp
[pagination]: https://medium.com/streamlit/paginating-dataframes-with-streamlit-2da29b080920
