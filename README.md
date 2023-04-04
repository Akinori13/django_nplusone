# django_nplusone
## セットアップ
### 仮想環境
パッケージにパスが通っていない場合に以下を付与してコマンドを実行する。
```bash
python -m 
```

### 仮想環境の立ち上げ
```bash
poetry install
```

#### 仮想環境の立ち上げ（developmentの依存関係が不要な場合）
```bash
poetry install --no-dev
```

#### 仮想環境の実行
```bash
poetry shell
```

#### 依存パッケージの追加
```bash
poetry add <package-name>
```