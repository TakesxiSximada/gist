# Torのインストールとアクセス

## インストール

```
$ brew install tor
```

## 起動

```
$ tor
```

## 設定

### Tor越しにcURLでアクセス

```
$ curl -L https://example.com --socks5 127.0.0.1:9050
```
