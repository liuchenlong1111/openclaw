# OpenClaw CLI 配对指南

## 问题
CLI 连接 Gateway 时显示 `pairing required`，需要通过 Dashboard 完成配对。

## 解决步骤

### 1. 打开 Dashboard
在浏览器中访问：
```
http://127.0.0.1:18789/
```

### 2. 查找配对/认证选项
在 Dashboard 页面上寻找以下选项之一：
- **"Auth"** 标签页
- **"Authentication"** 
- **"Pairing"** / **"设备配对"**
- **"Settings"** → **"Security"**

### 3. 添加 CLI 配对
找到配对管理界面后：
- 点击 **"New Pairing"** / **"添加设备"**
- 或点击 **"Generate Code"** / **"生成配对码"**

### 4. 完成配对

**方式 A：使用配对码**
如果生成了数字配对码（如：`123456`），在终端运行：
```bash
openclaw pairing approve 123456
```

**方式 B：直接添加信任设备**
有些版本支持直接添加设备，找到 **"Add Trusted Device"** 或 **"Trust This CLI"** 按钮

### 5. 验证配对
配对成功后，测试连接：
```bash
openclaw gateway status
```
应该不再显示 `pairing required`

---

## 备选方案：通过配置文件直接配对

如果 Dashboard 找不到配对选项，可以尝试手动编辑配对文件：

```bash
# 查看配对列表
openclaw pairing list

# 如果有待处理的配对请求，批准它
openclaw pairing approve <request-id>
```

---

## 当前配置信息

| 项目 | 值 |
|------|-----|
| Gateway Token | `31fb05ec1046783d0a5de8c07b1c48bb04f47d895c37f140` |
| Gateway URL | `ws://127.0.0.1:18789` |
| 认证模式 | token |

---

## 如果以上都不行

可以尝试重启 Gateway 并重新配置：

```bash
# 1. 停止 Gateway
openclaw gateway stop

# 2. 禁用认证（临时）
openclaw config unset gateway.auth

# 3. 重启 Gateway
openclaw gateway start

# 4. 在 Dashboard 中重新配置认证
# 5. 然后再启用 token 认证
```

⚠️ 注意：禁用认证后任何人都可以连接你的 Gateway，请尽快重新配置
