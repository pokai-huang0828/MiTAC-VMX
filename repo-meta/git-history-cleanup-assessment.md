# `.git` 歷史清理評估

> **狀態**:評估文件,**尚未執行**任何 history 改寫。
> **建立**:2026-05-06
> **決策窗口**:由 Kenny 決定要不要動手

---

## A. 現況數據(2026-05-06)

| 項目 | 值 |
|------|---|
| `.git` 大小 | **140 MB** (`du -sh .git`) |
| Pack 物件數 | 270 |
| Pack 大小 | 139.61 MiB |
| 工作樹大小 | ~31 MB |
| Commit 數 | 6 |
| 浪費比 | `.git` ≈ **4.5×** 工作樹 |

> 對一個只有 6 commit、純文件的 repo,140 MB 是異常的。clone / fetch 多花的時間都是在傳這些早就被刪除、不再需要的 binary。

---

## B. 要從歷史移除的 blob 清單

從 `git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sort -k3 -n -r` 取出 Top 15:

| Blob 路徑 | Size |
|-----------|------|
| `image_update/base/.../boot.img` | 64 MB |
| `image_update/base/.../NON-HLOS.bin` | 35 MB |
| `image_update/base/.../dspso.bin` | 32 MB |
| `image_update/base/.../persist.img` | 32 MB |
| `image_update/qpst.win.2.7_installer_00474.2/QPST.2.7.474.exe` | 26 MB |
| `image_update/{base,region}/.../adb.exe` × 2 | 17 MB × 2 = 34 MB |
| `image_update/{base,region}/.../LinuxTools/adb` × 2 | 17 MB × 2 = 34 MB |
| `image_update/qpst.../QPST_MergeModule.msm` | 14 MB |
| `image_update/qualcomm-driver/Qualcomm_USB_Driver_V1.0.exe` | 13 MB |
| `image_update/.../{fastboot, fastboot.exe}` × 4 | 11 MB × 4 = 44 MB |

**全部都在 `image_update/**` 路徑下**,而:
- 當前 `.gitignore` 已排除 `image_update/*`
- 工作樹也已不存在(`dfc2c4d` commit 已移除)
- Repo 沒有任何文件 / 連結引用這些 blob

→ **保留這些歷史的價值:零。**
→ 預估改寫後 `.git` 可降到 **~10 MB**。

---

## C. 影響範圍

### Commit hash 全變
- 改寫會重新計算所有 6 個 commit 的 SHA(`dfc2c4d` → `f91bc75`)
- 任何文件 / 連結引用舊 hash 會失效(目前掃過 repo 內無引用)
- 外部引用(Slack、Email、Jira ticket comment)若有引用 commit hash 也會壞

### 遠端
- 需 force push 到 `origin/main` 與 `origin/claude/analyze-repo-optimization-ftsx4`
- GitHub 上的 PR 若有引用舊 commit,會出現「commit not found」

### 協作者
- 任何已 clone 此 repo 的人需要重新 clone(或 `git fetch && git reset --hard origin/<branch>`)
- 目前看起來是 Kenny 單人 repo,影響低

### 進行中的 PR / branch
- `claude/analyze-repo-optimization-ftsx4` 在進行中
- **建議**:先把現有 branch 內容處理完並併入 main 再做 history 改寫,避免分支衝突

---

## D. 執行步驟(尚未執行,僅供參考)

```bash
# 1. 安裝 git-filter-repo(比 BFG 維護更積極)
pip install git-filter-repo

# 2. clone 一份 mirror(備份用)
cd /tmp
git clone --mirror http://.../MiTAC-VMX.git mitac-vmx-backup-2026XXXX.git

# 3. 在另一個 mirror clone 上做改寫
git clone --mirror http://.../MiTAC-VMX.git mitac-vmx-rewrite.git
cd mitac-vmx-rewrite.git
git filter-repo --path image_update --invert-paths

# 4. 驗證
du -sh .  # 應該降到 ~10 MB 等級
git log --all --oneline  # 確認 commit 結構保留
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sort -k3 -n -r | head -10
# Top 物件應已不再有 boot.img / NON-HLOS.bin 等

# 5. push
git push --force --all
git push --force --tags

# 6. 本地 working clone 重新 reset
cd /home/user/MiTAC-VMX
git fetch origin
git reset --hard origin/main
git gc --prune=now
```

---

## E. 風險與回滾

### 風險
1. **誤刪有用內容** — `image_update/**` 下原本有一份 `EVO image update process.md` 已被搬到 `EVO_image_update/` 並有 `.gitignore` 例外規則保留;改寫前用 `git log --all -- image_update/` 再次確認沒有要保留的文件 blob 落在 image_update/ 路徑下。
2. **Force push 衝突** — 若有他人正在 push,可能蓋掉他們的 commit。執行時段選 Kenny 自己的時間。
3. **Reflog 殘留** — 本地 working clone 在 force pull 後仍會保留舊 reflog 引用舊 hash,占空間;`git reflog expire --expire=now --all && git gc --prune=now` 清掉。

### 回滾
- 若改寫結果不正確,從備份 mirror force push 回去:
  ```bash
  cd /tmp/mitac-vmx-backup-YYYYMMDD.git
  git push --force --all origin
  git push --force --tags origin
  ```
- **不要在驗證 force push 成功前** 對 backup mirror 執行 `git gc --prune=now`,保留 reflog 直到確認。

---

## F. 決策建議

| 選項 | 適用情境 |
|------|---------|
| **執行 history 改寫** | 想要 clone / fetch 更快,且接受 force push + 重新 clone 成本 |
| **不改,只防未來** | `.gitignore` 已就位,後續若沒人再誤推大檔,140 MB 可接受 |
| **延後到評估期結束** | 評估期主力放在 PM 工作,history 清理當作期末整理 task |

> Kenny 的選擇 → 待定。本文件作為決策參考。

---

## G. 參考指令(可隨時重跑)

```bash
# 看 .git 大小
du -sh .git
git count-objects -vH

# 看歷史最大 blob
git rev-list --objects --all \
  | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
  | sort -k3 -n -r | head -20

# 看 image_update/ 路徑歷史
git log --all --oneline -- image_update/
```
