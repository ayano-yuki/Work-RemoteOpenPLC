# Front
## main
- [【完全解説】create-vueでVue3プロジェクト作成〜Vite爆速開発〜][003]
  - viteを使ったプロジェクト生成
  - 最大限の解説があるので、初めての開発では良きな情報がある
- [SVG REPO][015]
  - 無料でDLできるSVGサイト
## index.html
- [画像の保存を禁止する方法とその回避方法][001]
  - 背景画像を選択出来なくする(ドラッグ、右クリック)
  - bodyに「onselectstart="return false;" onmousedown="return false;"」をつけると目的の達成ができるが、「inputタグのテキストエリア系」に入力ができなくなる。
## HomeButton.vue
- [シンプルで使いやすいHTML・CSSボタンデザイン集11選 - ICS MEDIA][002]
  - アイコンとテキストが横並ぶボタン
  - 可愛くて、ボタンの意味が分かりやすいので採用した
## SettingView.vue
- [AxiosでPOSTリクエストの送信｜パラメータ渡し方も解説][006]
  - axiosのpostの仕方
  - 1年ぶりの開発なので、覚えていない個所が多い...
- [【簡単】inputタグで入力した内容の履歴・入力候補を出さない方法【属性を設定すれば解決】][008]
  - 履歴・入力候補がウザイので抹消
  - cssのアビスを覗きたい
## RunningView.vue
- [【CSS】おしゃれなボックスデザイン（囲み枠）のサンプル30][010]
  - 11. スマートなデザインに
  - グラフの表示がおしゃれに！！
## LineGraph.vue
- [Line chart Demo | Highcharts.com][011]
  - Line chart
  - Time series, zoomable
  - いい感じのグラフを書ける
## GaugeGraph.vue
- [Error while loading solid gauge module][012]
  - ゲージのエラーを無くす
- [Highcharts Vue Solid Gauge - CodeSandbox][013]
  - hoghchartsのgageの書き方(サブ)
- [Solid gauge Demo | Highcharts.com][014]
  - hoghchartsのgageの書き方(メイン)
## GeneratorGraph.vue
- [window.open()で開いたウィンドウにデータを渡す][016]
  - ミニウィンドウの開き方
  - 普通にすると、別タブになる
- [JavaScriptのwindow.openでウィンドウのサイズを指定して表示][017]
  - graphの描画が目的なのでコマイほうが良い
- [vue.js モーダルウィンドウ実装でコンポーネント理解][018]
  - ボツ
  - モーダルウィンドウでもいいが、z-indexの設定が大変なので...
## GeneratorView.vue
- [CSSで中央寄せする9つの方法（縦・横にセンタリング）][020]
  - 3.ど真ん中（中心）に配置する方法
  - graphのセンターリング 
## ScatterPlot.vue
- [Create Scatter Chart and Graph | Highcharts][021]
  - 任意のデータの描画

# API
## main
- [CORS (オリジン間リソース共有) - FastAPI][004]
  - CORSのエラーを無くす
  - starletteでも良いけど、純正（FastAPI）を採用した
- [【FastAPI】APIドキュメントに説明を追加する【入門】][005]
  - /docsをより充実にできる
  - APIドキュメントに説明書きがあると、エンジニアぽくて映える
- [FastAPIでPOSTされたJSONのレスポンスbodyを受け取る][007]
  - postされたデータの受け取り方
  - ZOZOさん、パネー
- [PythonでJSONファイル・文字列の読み込み・書き込み][009]
  - 設定を保存する仕組み
  - セキュリティに問題がありそうなので、要改善
- [Background Tasks - FastAPI][019]
  - バックグラウンドタスクの使い方

[001]:https://qiita.com/shisama/items/be0e432711de359598ed
[002]:https://ics.media/entry/230629/
[003]:https://reffect.co.jp/vue/create-vue
[004]:https://fastapi.tiangolo.com/ja/tutorial/cors/
[005]:https://self-methods.com/fastapiapi-tag-docstring/
[006]:https://apidog.com/jp/blog/send-post-request-with-axios/
[007]:https://qiita.com/satto_sann/items/8a458a8952f50b73f420
[008]:https://kasumiblog.org/input-autocomplete-no
[009]:https://note.nkmk.me/python-json-load-dump/
[010]:https://saruwakakun.com/html-css/reference/box
[011]:https://www.highcharts.com/demo/highcharts/line-chart
[012]:https://www.highcharts.com/forum/viewtopic.php?t=48659
[013]:https://codesandbox.io/p/sandbox/highcharts-vue-solid-gauge-oyeppq?file=%2Fsrc%2Fmain.js%3A18%2C1
[014]:https://www.highcharts.com/demo/highcharts/gauge-solid
[015]:https://www.svgrepo.com/
[016]:https://www.l08084.com/entry/2020/05/11/204230
[017]:https://dubdesign.net/javascript/windowopen-tab/
[018]:https://reffect.co.jp/vue/understand-component-by-moda-window
[019]:https://fastapi.tiangolo.com/tutorial/background-tasks/
[020]:https://saruwakakun.com/html-css/basic/centering
[021]:https://www.highcharts.com/demo/highcharts/scatter





