# Web アプリケーションサーバ構築用 Ansible

## 準備

hosts ファイルに、以下の内容を記載する:

```
[<ロール名>]
<IPアドレス or ドメイン名>:<SSHポート番号>
```

## 実行

### 全実行

$ ansible-playbook webapp.yml --private-key=~/.ssh/ml_av_actress.pem

### 一部タスクのみ

$ ansible-playbook webapp.yml --private-key=~/.ssh/ml_av_actress.pem --tags <タグ>

### 実行されるタスクの確認

$ ansible-playbook webapp.yml --private-key=~/.ssh/ml_av_actress.pem --list-tasks

### Dry run

$ ansible-playbook webapp.yml --private-key=~/.ssh/ml_av_actress.pem --check
